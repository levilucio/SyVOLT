"""
__MT_post__FamiliesToPersonsMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Apr 17 14:22:58 2015
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


    self.obj83=CD_Class3(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # QOCA
    self.obj83.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj83.Graphical_Appearance.setValue( ('MT_post__MetaModelElement_S', self.obj83))

    # name
    self.obj83.name.setValue('MT_post__MetaModelElement_S')

    # attributes
    self.obj83.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj83.attributes.setValue(lcobj2)

    # Abstract
    self.obj83.Abstract.setValue((None, 0))
    self.obj83.Abstract.config = 0

    # cardinality
    self.obj83.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj83.cardinality.setValue(lcobj2)

    # display
    self.obj83.display.setValue('Attributes:\n  - cardinality :: String\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From match_contains: 0 to N\n  - From backward_link: 0 to N\n  - To indirectLink_S: 0 to N\n  - From indirectLink_S: 0 to N\n  - To directLink_S: 0 to N\n  - From directLink_S: 0 to N\n  - From trace_link: 0 to N\n  - To hasAttr_S: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(520.0,120.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.9278688524590166]
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
    self.obj84.Graphical_Appearance.setValue( ('MT_post__HouseholdRoot', self.obj84))

    # name
    self.obj84.name.setValue('MT_post__HouseholdRoot')

    # attributes
    self.obj84.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj84.attributes.setValue(lcobj2)

    # Abstract
    self.obj84.Abstract.setValue((None, 0))
    self.obj84.Abstract.config = 0

    # cardinality
    self.obj84.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj84.cardinality.setValue(lcobj2)

    # display
    self.obj84.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(280.0,340.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj85.Graphical_Appearance.setValue( ('MT_post__Family', self.obj85))

    # name
    self.obj85.name.setValue('MT_post__Family')

    # attributes
    self.obj85.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj85.attributes.setValue(lcobj2)

    # Abstract
    self.obj85.Abstract.setValue((None, 0))
    self.obj85.Abstract.config = 0

    # cardinality
    self.obj85.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj85.cardinality.setValue(lcobj2)

    # display
    self.obj85.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(500.0,340.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj86.Graphical_Appearance.setValue( ('MT_post__Member', self.obj86))

    # name
    self.obj86.name.setValue('MT_post__Member')

    # attributes
    self.obj86.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj86.attributes.setValue(lcobj2)

    # Abstract
    self.obj86.Abstract.setValue((None, 0))
    self.obj86.Abstract.config = 0

    # cardinality
    self.obj86.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj86.cardinality.setValue(lcobj2)

    # display
    self.obj86.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(740.0,340.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj87.Graphical_Appearance.setValue( ('MT_post__MatchModel', self.obj87))

    # name
    self.obj87.name.setValue('MT_post__MatchModel')

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
    cobj2.setValue(('MT_post__match_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__paired_with', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj87.cardinality.setValue(lcobj2)

    # display
    self.obj87.display.setValue('Multiplicities:\n  - To match_contains: 0 to N\n  - To paired_with: 1 to 1\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(20.0,120.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj88.Graphical_Appearance.setValue( ('MT_post__ApplyModel', self.obj88))

    # name
    self.obj88.name.setValue('MT_post__ApplyModel')

    # attributes
    self.obj88.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj88.attributes.setValue(lcobj2)

    # Abstract
    self.obj88.Abstract.setValue((None, 0))
    self.obj88.Abstract.config = 0

    # cardinality
    self.obj88.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj88.cardinality.setValue(lcobj2)

    # display
    self.obj88.display.setValue('Multiplicities:\n  - To apply_contains: 0 to N\n  - From paired_with: 1 to 1\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(20.0,540.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.752
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj89.Graphical_Appearance.setValue( ('MT_post__MetaModelElement_T', self.obj89))

    # name
    self.obj89.name.setValue('MT_post__MetaModelElement_T')

    # attributes
    self.obj89.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj89.attributes.setValue(lcobj2)

    # Abstract
    self.obj89.Abstract.setValue((None, 0))
    self.obj89.Abstract.config = 0

    # cardinality
    self.obj89.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj89.cardinality.setValue(lcobj2)

    # display
    self.obj89.display.setValue('Attributes:\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From apply_contains: 0 to N\n  - To backward_link: 0 to N\n  - To directLink_T: 0 to N\n  - From directLink_T: 0 to N\n  - To trace_link: 0 to N\n  - To hasAttr_T: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(520.0,540.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.672
       new_obj.layConstraints['scale'] = [1.3890624999999999, 1.4200819672131149]
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
    self.obj90.Graphical_Appearance.setValue( ('MT_post__CommunityRoot', self.obj90))

    # name
    self.obj90.name.setValue('MT_post__CommunityRoot')

    # attributes
    self.obj90.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj90.attributes.setValue(lcobj2)

    # Abstract
    self.obj90.Abstract.setValue((None, 0))
    self.obj90.Abstract.config = 0

    # cardinality
    self.obj90.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj90.cardinality.setValue(lcobj2)

    # display
    self.obj90.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj90.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(320.0,720.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj91.Graphical_Appearance.setValue( ('MT_post__Person', self.obj91))

    # name
    self.obj91.name.setValue('MT_post__Person')

    # attributes
    self.obj91.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj91.attributes.setValue(lcobj2)

    # Abstract
    self.obj91.Abstract.setValue((None, 0))
    self.obj91.Abstract.config = 0

    # cardinality
    self.obj91.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj91.cardinality.setValue(lcobj2)

    # display
    self.obj91.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj91.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,720.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj92.Graphical_Appearance.setValue( ('MT_post__Man', self.obj92))

    # name
    self.obj92.name.setValue('MT_post__Man')

    # attributes
    self.obj92.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj92.attributes.setValue(lcobj2)

    # Abstract
    self.obj92.Abstract.setValue((None, 0))
    self.obj92.Abstract.config = 0

    # cardinality
    self.obj92.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj92.cardinality.setValue(lcobj2)

    # display
    self.obj92.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj92.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(760.0,720.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj93.Graphical_Appearance.setValue( ('MT_post__Attribute', self.obj93))

    # name
    self.obj93.name.setValue('MT_post__Attribute')

    # attributes
    self.obj93.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj93.attributes.setValue(lcobj2)

    # Abstract
    self.obj93.Abstract.setValue((None, 0))
    self.obj93.Abstract.config = 0

    # cardinality
    self.obj93.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__hasAttr_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__hasAttr_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj93.cardinality.setValue(lcobj2)

    # display
    self.obj93.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From hasAttr_S: 0 to N\n  - From hasAttr_T: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj93.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1480.0,500.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [2.05625, 1.0844262295081968]
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
    self.obj94.Graphical_Appearance.setValue( ('MT_post__Equation', self.obj94))

    # name
    self.obj94.name.setValue('MT_post__Equation')

    # attributes
    self.obj94.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj94.attributes.setValue(lcobj2)

    # Abstract
    self.obj94.Abstract.setValue((None, 0))
    self.obj94.Abstract.config = 0

    # cardinality
    self.obj94.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__leftExpr', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__rightExpr', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj94.cardinality.setValue(lcobj2)

    # display
    self.obj94.display.setValue('Multiplicities:\n  - To leftExpr: 0 to N\n  - To rightExpr: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj94.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1640.0,0.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
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
    self.obj95.Graphical_Appearance.setValue( ('MT_post__Expression', self.obj95))

    # name
    self.obj95.name.setValue('MT_post__Expression')

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
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj95.cardinality.setValue(lcobj2)

    # display
    self.obj95.display.setValue('Multiplicities:\n  - From leftExpr: 0 to N\n  - From rightExpr: 0 to N\n  - From arg_1: 0 to N\n  - From arg_2: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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
       new_obj = graph_CD_Class3(1640.0,280.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [2.05625, 1.0844262295081968]
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
    self.obj96.Graphical_Appearance.setValue( ('MT_post__Constant', self.obj96))

    # name
    self.obj96.name.setValue('MT_post__Constant')

    # attributes
    self.obj96.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj96.attributes.setValue(lcobj2)

    # Abstract
    self.obj96.Abstract.setValue((None, 0))
    self.obj96.Abstract.config = 0

    # cardinality
    self.obj96.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj96.cardinality.setValue(lcobj2)

    # display
    self.obj96.display.setValue('Attributes:\n  - value :: String\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj96.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(2040.0,280.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
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
    self.obj97.Graphical_Appearance.setValue( ('MT_post__Concat', self.obj97))

    # name
    self.obj97.name.setValue('MT_post__Concat')

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

    # Abstract
    self.obj97.Abstract.setValue((None, 0))
    self.obj97.Abstract.config = 0

    # cardinality
    self.obj97.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__arg_1', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__arg_2', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj97.cardinality.setValue(lcobj2)

    # display
    self.obj97.display.setValue('Multiplicities:\n  - To arg_1: 0 to N\n  - To arg_2: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj97.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1820.0,720.0,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
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
    self.obj98.Graphical_Appearance.setValue( ('MT_post__Woman', self.obj98))

    # name
    self.obj98.name.setValue('MT_post__Woman')

    # attributes
    self.obj98.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj98.attributes.setValue(lcobj2)

    # Abstract
    self.obj98.Abstract.setValue((None, 0))
    self.obj98.Abstract.config = 0

    # cardinality
    self.obj98.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj98.cardinality.setValue(lcobj2)

    # display
    self.obj98.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
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

    self.obj98.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,920.0,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj123=CD_Class3(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # QOCA
    self.obj123.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj123.Graphical_Appearance.setValue( ('MT_post__GenericNode_FamiliesToPersonsMM', self.obj123))

    # name
    self.obj123.name.setValue('MT_post__GenericNode_FamiliesToPersonsMM')

    # attributes
    self.obj123.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj123.attributes.setValue(lcobj2)

    # Abstract
    self.obj123.Abstract.setValue((None, 0))
    self.obj123.Abstract.config = 0

    # cardinality
    self.obj123.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj123.cardinality.setValue(lcobj2)

    # display
    self.obj123.display.setValue('Multiplicities:\n  - To GenericEdge_FamiliesToPersonsMM: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj123.display.setHeight(15)

    # Actions
    self.obj123.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj123.Actions.setValue(lcobj2)

    # Constraints
    self.obj123.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Constraints.setValue(lcobj2)

    self.obj123.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(0.0,0.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj99=CD_Association3(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # QOCA
    self.obj99.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj99.Graphical_Appearance.setValue( ('MT_post__match_contains', self.obj99))
    self.obj99.Graphical_Appearance.linkInfo=linkEditor(self,self.obj99.Graphical_Appearance.semObject, "match_contains")
    self.obj99.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('match_contains_1stLink', self.obj99.Graphical_Appearance.linkInfo.FirstLink))
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('match_contains_1stSegment', self.obj99.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj99.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.Center.setValue( ('match_contains_Center', self.obj99.Graphical_Appearance.linkInfo))
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('match_contains_2ndSegment', self.obj99.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('match_contains_2ndLink', self.obj99.Graphical_Appearance.linkInfo.SecondLink))
    self.obj99.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.Center.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj99.Graphical_Appearance.semObject
    self.obj99.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj99.Graphical_Appearance.semObject

    # name
    self.obj99.name.setValue('MT_post__match_contains')

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
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj99.cardinality.setValue(lcobj2)

    # display
    self.obj99.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MatchModel: 0 to N\n')
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
       new_obj = graph_CD_Association3(361.8,199.8,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.3230000000000002, 1.0]
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
    self.obj100.Graphical_Appearance.setValue( ('MT_post__apply_contains', self.obj100))
    self.obj100.Graphical_Appearance.linkInfo=linkEditor(self,self.obj100.Graphical_Appearance.semObject, "apply_contains")
    self.obj100.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('apply_contains_1stLink', self.obj100.Graphical_Appearance.linkInfo.FirstLink))
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('apply_contains_1stSegment', self.obj100.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj100.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.Center.setValue( ('apply_contains_Center', self.obj100.Graphical_Appearance.linkInfo))
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('apply_contains_2ndSegment', self.obj100.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('apply_contains_2ndLink', self.obj100.Graphical_Appearance.linkInfo.SecondLink))
    self.obj100.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.Center.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj100.Graphical_Appearance.semObject
    self.obj100.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj100.Graphical_Appearance.semObject

    # name
    self.obj100.name.setValue('MT_post__apply_contains')

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
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj100.cardinality.setValue(lcobj2)

    # display
    self.obj100.display.setValue('Multiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From ApplyModel: 0 to N\n')
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
       new_obj = graph_CD_Association3(362.491532278,586.86445,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.316, 1.0]
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
    self.obj101.Graphical_Appearance.setValue( ('MT_post__backward_link', self.obj101))
    self.obj101.Graphical_Appearance.linkInfo=linkEditor(self,self.obj101.Graphical_Appearance.semObject, "backward_link")
    self.obj101.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('backward_link_1stLink', self.obj101.Graphical_Appearance.linkInfo.FirstLink))
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('backward_link_1stSegment', self.obj101.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj101.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.Center.setValue( ('backward_link_Center', self.obj101.Graphical_Appearance.linkInfo))
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('backward_link_2ndSegment', self.obj101.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('backward_link_2ndLink', self.obj101.Graphical_Appearance.linkInfo.SecondLink))
    self.obj101.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.Center.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj101.Graphical_Appearance.semObject
    self.obj101.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj101.Graphical_Appearance.semObject

    # name
    self.obj101.name.setValue('MT_post__backward_link')

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
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj101.cardinality.setValue(lcobj2)

    # display
    self.obj101.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
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
       new_obj = graph_CD_Association3(1245.0,339.5,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
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
    self.obj102.Graphical_Appearance.setValue( ('MT_post__indirectLink_S', self.obj102))
    self.obj102.Graphical_Appearance.linkInfo=linkEditor(self,self.obj102.Graphical_Appearance.semObject, "indirectLink_S")
    self.obj102.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('indirectLink_S_1stLink', self.obj102.Graphical_Appearance.linkInfo.FirstLink))
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('blue', 20)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('indirectLink_S_1stSegment', self.obj102.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj102.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.Center.setValue( ('indirectLink_S_Center', self.obj102.Graphical_Appearance.linkInfo))
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('blue', 20)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('indirectLink_S_2ndSegment', self.obj102.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('indirectLink_S_2ndLink', self.obj102.Graphical_Appearance.linkInfo.SecondLink))
    self.obj102.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.Center.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj102.Graphical_Appearance.semObject
    self.obj102.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj102.Graphical_Appearance.semObject

    # name
    self.obj102.name.setValue('MT_post__indirectLink_S')

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
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj102.cardinality.setValue(lcobj2)

    # display
    self.obj102.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
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
       new_obj = graph_CD_Association3(1274.5,81.5,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.862, 1.0]
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
    self.obj103.Graphical_Appearance.setValue( ('MT_post__directLink_T', self.obj103))
    self.obj103.Graphical_Appearance.linkInfo=linkEditor(self,self.obj103.Graphical_Appearance.semObject, "directLink_T")
    self.obj103.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_T_1stLink', self.obj103.Graphical_Appearance.linkInfo.FirstLink))
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_T_1stSegment', self.obj103.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj103.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_T_Center', self.obj103.Graphical_Appearance.linkInfo))
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_T_2ndSegment', self.obj103.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_T_2ndLink', self.obj103.Graphical_Appearance.linkInfo.SecondLink))
    self.obj103.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.Center.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj103.Graphical_Appearance.semObject
    self.obj103.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj103.Graphical_Appearance.semObject

    # name
    self.obj103.name.setValue('MT_post__directLink_T')

    # displaySelect
    self.obj103.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj103.displaySelect.config = 0

    # attributes
    self.obj103.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj103.attributes.setValue(lcobj2)

    # cardinality
    self.obj103.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj103.cardinality.setValue(lcobj2)

    # display
    self.obj103.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
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
       new_obj = graph_CD_Association3(1193.0,684.5,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.185483870967742]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=CD_Association3(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # QOCA
    self.obj104.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj104.Graphical_Appearance.setValue( ('MT_post__directLink_S', self.obj104))
    self.obj104.Graphical_Appearance.linkInfo=linkEditor(self,self.obj104.Graphical_Appearance.semObject, "directLink_S")
    self.obj104.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_S_1stLink', self.obj104.Graphical_Appearance.linkInfo.FirstLink))
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_S_1stSegment', self.obj104.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj104.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj104.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_S_Center', self.obj104.Graphical_Appearance.linkInfo))
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_S_2ndSegment', self.obj104.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj104.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_S_2ndLink', self.obj104.Graphical_Appearance.linkInfo.SecondLink))
    self.obj104.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj104.Graphical_Appearance.semObject
    self.obj104.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj104.Graphical_Appearance.semObject
    self.obj104.Graphical_Appearance.linkInfo.Center.semObject=self.obj104.Graphical_Appearance.semObject
    self.obj104.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj104.Graphical_Appearance.semObject
    self.obj104.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj104.Graphical_Appearance.semObject

    # name
    self.obj104.name.setValue('MT_post__directLink_S')

    # displaySelect
    self.obj104.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj104.displaySelect.config = 0

    # attributes
    self.obj104.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj104.attributes.setValue(lcobj2)

    # cardinality
    self.obj104.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj104.cardinality.setValue(lcobj2)

    # display
    self.obj104.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj104.display.setHeight(15)

    # Actions
    self.obj104.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj104.Actions.setValue(lcobj2)

    # Constraints
    self.obj104.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj104.Constraints.setValue(lcobj2)

    self.obj104.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(950.5,86.5,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.862, 1.185483870967742]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=CD_Association3(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # QOCA
    self.obj105.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj105.Graphical_Appearance.setValue( ('MT_post__paired_with', self.obj105))
    self.obj105.Graphical_Appearance.linkInfo=linkEditor(self,self.obj105.Graphical_Appearance.semObject, "paired_with")
    self.obj105.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('paired_with_1stLink', self.obj105.Graphical_Appearance.linkInfo.FirstLink))
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('paired_with_1stSegment', self.obj105.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj105.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj105.Graphical_Appearance.linkInfo.Center.setValue( ('paired_with_Center', self.obj105.Graphical_Appearance.linkInfo))
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('paired_with_2ndSegment', self.obj105.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj105.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('paired_with_2ndLink', self.obj105.Graphical_Appearance.linkInfo.SecondLink))
    self.obj105.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj105.Graphical_Appearance.semObject
    self.obj105.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj105.Graphical_Appearance.semObject
    self.obj105.Graphical_Appearance.linkInfo.Center.semObject=self.obj105.Graphical_Appearance.semObject
    self.obj105.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj105.Graphical_Appearance.semObject
    self.obj105.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj105.Graphical_Appearance.semObject

    # name
    self.obj105.name.setValue('MT_post__paired_with')

    # displaySelect
    self.obj105.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj105.displaySelect.config = 0

    # attributes
    self.obj105.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj105.attributes.setValue(lcobj2)

    # cardinality
    self.obj105.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__ApplyModel', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MatchModel', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj105.cardinality.setValue(lcobj2)

    # display
    self.obj105.display.setValue('Multiplicities:\n  - To ApplyModel: 1 to 1\n  - From MatchModel: 1 to 1\n')
    self.obj105.display.setHeight(15)

    # Actions
    self.obj105.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj105.Actions.setValue(lcobj2)

    # Constraints
    self.obj105.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj105.Constraints.setValue(lcobj2)

    self.obj105.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(136.0,401.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.344, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=CD_Association3(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # QOCA
    self.obj106.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj106.Graphical_Appearance.setValue( ('MT_post__trace_link', self.obj106))
    self.obj106.Graphical_Appearance.linkInfo=linkEditor(self,self.obj106.Graphical_Appearance.semObject, "trace_link")
    self.obj106.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('trace_link_1stLink', self.obj106.Graphical_Appearance.linkInfo.FirstLink))
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('trace_link_1stSegment', self.obj106.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj106.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj106.Graphical_Appearance.linkInfo.Center.setValue( ('trace_link_Center', self.obj106.Graphical_Appearance.linkInfo))
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('trace_link_2ndSegment', self.obj106.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj106.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('trace_link_2ndLink', self.obj106.Graphical_Appearance.linkInfo.SecondLink))
    self.obj106.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj106.Graphical_Appearance.semObject
    self.obj106.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj106.Graphical_Appearance.semObject
    self.obj106.Graphical_Appearance.linkInfo.Center.semObject=self.obj106.Graphical_Appearance.semObject
    self.obj106.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj106.Graphical_Appearance.semObject
    self.obj106.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj106.Graphical_Appearance.semObject

    # name
    self.obj106.name.setValue('MT_post__trace_link')

    # displaySelect
    self.obj106.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj106.displaySelect.config = 0

    # attributes
    self.obj106.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj106.attributes.setValue(lcobj2)

    # cardinality
    self.obj106.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj106.cardinality.setValue(lcobj2)

    # display
    self.obj106.display.setValue('Multiplicities:\n  - From MetaModelElement_T: 0 to N\n  - To MetaModelElement_S: 0 to N\n')
    self.obj106.display.setHeight(15)

    # Actions
    self.obj106.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj106.Actions.setValue(lcobj2)

    # Constraints
    self.obj106.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj106.Constraints.setValue(lcobj2)

    self.obj106.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1242.0,481.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=CD_Association3(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # QOCA
    self.obj107.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj107.Graphical_Appearance.setValue( ('MT_post__hasAttr_S', self.obj107))
    self.obj107.Graphical_Appearance.linkInfo=linkEditor(self,self.obj107.Graphical_Appearance.semObject, "hasAttr_S")
    self.obj107.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasAttr_S_1stLink', self.obj107.Graphical_Appearance.linkInfo.FirstLink))
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasAttr_S_1stSegment', self.obj107.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj107.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj107.Graphical_Appearance.linkInfo.Center.setValue( ('hasAttr_S_Center', self.obj107.Graphical_Appearance.linkInfo))
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasAttr_S_2ndSegment', self.obj107.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj107.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasAttr_S_2ndLink', self.obj107.Graphical_Appearance.linkInfo.SecondLink))
    self.obj107.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj107.Graphical_Appearance.semObject
    self.obj107.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj107.Graphical_Appearance.semObject
    self.obj107.Graphical_Appearance.linkInfo.Center.semObject=self.obj107.Graphical_Appearance.semObject
    self.obj107.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj107.Graphical_Appearance.semObject
    self.obj107.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj107.Graphical_Appearance.semObject

    # name
    self.obj107.name.setValue('MT_post__hasAttr_S')

    # displaySelect
    self.obj107.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj107.displaySelect.config = 0

    # attributes
    self.obj107.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj107.attributes.setValue(lcobj2)

    # cardinality
    self.obj107.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj107.cardinality.setValue(lcobj2)

    # display
    self.obj107.display.setValue('Multiplicities:\n  - To Attribute: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj107.display.setHeight(15)

    # Actions
    self.obj107.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj107.Actions.setValue(lcobj2)

    # Constraints
    self.obj107.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj107.Constraints.setValue(lcobj2)

    self.obj107.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1346.0,240.975409836,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.862, 1.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=CD_Association3(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # QOCA
    self.obj108.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj108.Graphical_Appearance.setValue( ('MT_post__hasAttr_T', self.obj108))
    self.obj108.Graphical_Appearance.linkInfo=linkEditor(self,self.obj108.Graphical_Appearance.semObject, "hasAttr_T")
    self.obj108.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasAttr_T_1stLink', self.obj108.Graphical_Appearance.linkInfo.FirstLink))
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasAttr_T_1stSegment', self.obj108.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj108.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj108.Graphical_Appearance.linkInfo.Center.setValue( ('hasAttr_T_Center', self.obj108.Graphical_Appearance.linkInfo))
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasAttr_T_2ndSegment', self.obj108.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj108.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasAttr_T_2ndLink', self.obj108.Graphical_Appearance.linkInfo.SecondLink))
    self.obj108.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj108.Graphical_Appearance.semObject
    self.obj108.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj108.Graphical_Appearance.semObject
    self.obj108.Graphical_Appearance.linkInfo.Center.semObject=self.obj108.Graphical_Appearance.semObject
    self.obj108.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj108.Graphical_Appearance.semObject
    self.obj108.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj108.Graphical_Appearance.semObject

    # name
    self.obj108.name.setValue('MT_post__hasAttr_T')

    # displaySelect
    self.obj108.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj108.displaySelect.config = 0

    # attributes
    self.obj108.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj108.attributes.setValue(lcobj2)

    # cardinality
    self.obj108.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Attribute', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj108.cardinality.setValue(lcobj2)

    # display
    self.obj108.display.setValue('Multiplicities:\n  - To Attribute: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj108.display.setHeight(15)

    # Actions
    self.obj108.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj108.Actions.setValue(lcobj2)

    # Constraints
    self.obj108.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj108.Constraints.setValue(lcobj2)

    self.obj108.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1292.49804688,838.905737705,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=CD_Association3(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # QOCA
    self.obj109.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj109.Graphical_Appearance.setValue( ('MT_post__leftExpr', self.obj109))
    self.obj109.Graphical_Appearance.linkInfo=linkEditor(self,self.obj109.Graphical_Appearance.semObject, "leftExpr")
    self.obj109.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('leftExpr_1stLink', self.obj109.Graphical_Appearance.linkInfo.FirstLink))
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('leftExpr_1stSegment', self.obj109.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj109.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj109.Graphical_Appearance.linkInfo.Center.setValue( ('leftExpr_Center', self.obj109.Graphical_Appearance.linkInfo))
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('leftExpr_2ndSegment', self.obj109.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj109.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('leftExpr_2ndLink', self.obj109.Graphical_Appearance.linkInfo.SecondLink))
    self.obj109.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj109.Graphical_Appearance.semObject
    self.obj109.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj109.Graphical_Appearance.semObject
    self.obj109.Graphical_Appearance.linkInfo.Center.semObject=self.obj109.Graphical_Appearance.semObject
    self.obj109.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj109.Graphical_Appearance.semObject
    self.obj109.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj109.Graphical_Appearance.semObject

    # name
    self.obj109.name.setValue('MT_post__leftExpr')

    # displaySelect
    self.obj109.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj109.displaySelect.config = 0

    # attributes
    self.obj109.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj109.attributes.setValue(lcobj2)

    # cardinality
    self.obj109.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Equation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj109.cardinality.setValue(lcobj2)

    # display
    self.obj109.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Equation: 0 to N\n')
    self.obj109.display.setHeight(15)

    # Actions
    self.obj109.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj109.Actions.setValue(lcobj2)

    # Constraints
    self.obj109.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj109.Constraints.setValue(lcobj2)

    self.obj109.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1618.0,211.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.204, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=CD_Association3(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # QOCA
    self.obj110.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj110.Graphical_Appearance.setValue( ('MT_post__rightExpr', self.obj110))
    self.obj110.Graphical_Appearance.linkInfo=linkEditor(self,self.obj110.Graphical_Appearance.semObject, "rightExpr")
    self.obj110.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('rightExpr_1stLink', self.obj110.Graphical_Appearance.linkInfo.FirstLink))
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('rightExpr_1stSegment', self.obj110.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj110.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj110.Graphical_Appearance.linkInfo.Center.setValue( ('rightExpr_Center', self.obj110.Graphical_Appearance.linkInfo))
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('rightExpr_2ndSegment', self.obj110.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj110.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('rightExpr_2ndLink', self.obj110.Graphical_Appearance.linkInfo.SecondLink))
    self.obj110.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj110.Graphical_Appearance.semObject
    self.obj110.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj110.Graphical_Appearance.semObject
    self.obj110.Graphical_Appearance.linkInfo.Center.semObject=self.obj110.Graphical_Appearance.semObject
    self.obj110.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj110.Graphical_Appearance.semObject
    self.obj110.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj110.Graphical_Appearance.semObject

    # name
    self.obj110.name.setValue('MT_post__rightExpr')

    # displaySelect
    self.obj110.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj110.displaySelect.config = 0

    # attributes
    self.obj110.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj110.attributes.setValue(lcobj2)

    # cardinality
    self.obj110.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Equation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj110.cardinality.setValue(lcobj2)

    # display
    self.obj110.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Equation: 0 to N\n')
    self.obj110.display.setHeight(15)

    # Actions
    self.obj110.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj110.Actions.setValue(lcobj2)

    # Constraints
    self.obj110.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj110.Constraints.setValue(lcobj2)

    self.obj110.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1866.15625,208.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.204, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=CD_Association3(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # QOCA
    self.obj111.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj111.Graphical_Appearance.setValue( ('MT_post__arg_1', self.obj111))
    self.obj111.Graphical_Appearance.linkInfo=linkEditor(self,self.obj111.Graphical_Appearance.semObject, "arg_1")
    self.obj111.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('arg_1_1stLink', self.obj111.Graphical_Appearance.linkInfo.FirstLink))
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('arg_1_1stSegment', self.obj111.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj111.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj111.Graphical_Appearance.linkInfo.Center.setValue( ('arg_1_Center', self.obj111.Graphical_Appearance.linkInfo))
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('arg_1_2ndSegment', self.obj111.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj111.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('arg_1_2ndLink', self.obj111.Graphical_Appearance.linkInfo.SecondLink))
    self.obj111.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj111.Graphical_Appearance.semObject
    self.obj111.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj111.Graphical_Appearance.semObject
    self.obj111.Graphical_Appearance.linkInfo.Center.semObject=self.obj111.Graphical_Appearance.semObject
    self.obj111.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj111.Graphical_Appearance.semObject
    self.obj111.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj111.Graphical_Appearance.semObject

    # name
    self.obj111.name.setValue('MT_post__arg_1')

    # displaySelect
    self.obj111.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj111.displaySelect.config = 0

    # attributes
    self.obj111.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj111.attributes.setValue(lcobj2)

    # cardinality
    self.obj111.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Concat', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj111.cardinality.setValue(lcobj2)

    # display
    self.obj111.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Concat: 0 to N\n')
    self.obj111.display.setHeight(15)

    # Actions
    self.obj111.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj111.Actions.setValue(lcobj2)

    # Constraints
    self.obj111.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj111.Constraints.setValue(lcobj2)

    self.obj111.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1780.0,551.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.19, 1.0]
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
    self.obj112.Graphical_Appearance.setValue( ('MT_post__arg_2', self.obj112))
    self.obj112.Graphical_Appearance.linkInfo=linkEditor(self,self.obj112.Graphical_Appearance.semObject, "arg_2")
    self.obj112.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('arg_2_1stLink', self.obj112.Graphical_Appearance.linkInfo.FirstLink))
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
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('arg_2_1stSegment', self.obj112.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj112.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.Center.setValue( ('arg_2_Center', self.obj112.Graphical_Appearance.linkInfo))
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
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('arg_2_2ndSegment', self.obj112.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('arg_2_2ndLink', self.obj112.Graphical_Appearance.linkInfo.SecondLink))
    self.obj112.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.Center.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj112.Graphical_Appearance.semObject
    self.obj112.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj112.Graphical_Appearance.semObject

    # name
    self.obj112.name.setValue('MT_post__arg_2')

    # displaySelect
    self.obj112.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj112.displaySelect.config = 0

    # attributes
    self.obj112.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj112.attributes.setValue(lcobj2)

    # cardinality
    self.obj112.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Expression', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Concat', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj112.cardinality.setValue(lcobj2)

    # display
    self.obj112.display.setValue('Multiplicities:\n  - To Expression: 0 to N\n  - From Concat: 0 to N\n')
    self.obj112.display.setHeight(15)

    # Actions
    self.obj112.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj112.Actions.setValue(lcobj2)

    # Constraints
    self.obj112.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj112.Constraints.setValue(lcobj2)

    self.obj112.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1965.53125,535.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.19, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj124=CD_Association3(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # QOCA
    self.obj124.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj124.Graphical_Appearance.setValue( ('MT_post__GenericEdge_FamiliesToPersonsMM', self.obj124))
    self.obj124.Graphical_Appearance.linkInfo=linkEditor(self,self.obj124.Graphical_Appearance.semObject, "GenericEdge_FamiliesToPersonsMM")
    self.obj124.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_1stLink', self.obj124.Graphical_Appearance.linkInfo.FirstLink))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('purple', 20)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_1stSegment', self.obj124.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj124.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.Center.setValue( ('GenericEdge_FamiliesToPersonsMM_Center', self.obj124.Graphical_Appearance.linkInfo))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('purple', 20)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_2ndSegment', self.obj124.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_2ndLink', self.obj124.Graphical_Appearance.linkInfo.SecondLink))
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.Center.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj124.Graphical_Appearance.semObject

    # name
    self.obj124.name.setValue('MT_post__GenericEdge_FamiliesToPersonsMM')

    # displaySelect
    self.obj124.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj124.displaySelect.config = 0

    # attributes
    self.obj124.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj124.attributes.setValue(lcobj2)

    # cardinality
    self.obj124.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_post__Woman', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj124.cardinality.setValue(lcobj2)

    # display
    self.obj124.display.setValue('Multiplicities:\n  - From GenericNode_FamiliesToPersonsMM: 0 to N\n  - To GenericNode_FamiliesToPersonsMM: 0 to N\n  - To MetaModelElement_S: 0 to N\n  - To HouseholdRoot: 0 to N\n  - To Family: 0 to N\n  - To Member: 0 to N\n  - To MatchModel: 0 to N\n  - To ApplyModel: 0 to N\n  - To MetaModelElement_T: 0 to N\n  - To CommunityRoot: 0 to N\n  - To Person: 0 to N\n  - To Man: 0 to N\n  - To Attribute: 0 to N\n  - To Equation: 0 to N\n  - To Expression: 0 to N\n  - To Constant: 0 to N\n  - To Concat: 0 to N\n  - To Woman: 0 to N\n')
    self.obj124.display.setHeight(15)

    # Actions
    self.obj124.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_post__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj124.Actions.setValue(lcobj2)

    # Constraints
    self.obj124.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Constraints.setValue(lcobj2)

    self.obj124.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(0.0,0.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.6390000000000002, 4.504838709677419]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj113=CD_Inheritance3(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    self.obj113.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(641.4,303.6,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=CD_Inheritance3(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    self.obj114.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(754.6,277.8,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=CD_Inheritance3(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    self.obj115.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(468.4,303.6,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=CD_Inheritance3(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    self.obj116.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(609.891532278,704.0332,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=CD_Inheritance3(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    self.obj117.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(757.391532278,694.0332,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=CD_Inheritance3(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    self.obj118.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(502.391532278,694.0332,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=CD_Inheritance3(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    self.obj119.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1656.0,461.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=CD_Inheritance3(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    self.obj120.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1926.0,405.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=CD_Inheritance3(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    self.obj121.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1831.0,571.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=CD_Inheritance3(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    self.obj122.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(646.0,821.5,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    # Connections for obj83 (graphObject_: Obj67) named MT_post__MetaModelElement_S
    self.drawConnections(
(self.obj83,self.obj102,[711.0, 192.98360655737704, 1026.0, 203.0, 1274.5, 81.5, 1274.5, 81.5],"true", 4),
(self.obj83,self.obj104,[711.0, 192.98360655737704, 950.5, 86.5, 950.5, 86.5],"true", 3),
(self.obj83,self.obj107,[711.0, 243.1081967213115, 1346.0, 240.975409836],"true", 2) )
    # Connections for obj84 (graphObject_: Obj68) named MT_post__HouseholdRoot
    self.drawConnections(
(self.obj84,self.obj115,[436.0, 341.0, 468.4, 303.6],"true", 2) )
    # Connections for obj85 (graphObject_: Obj69) named MT_post__Family
    self.drawConnections(
(self.obj85,self.obj113,[656.0, 341.0, 641.4, 303.6],"true", 2) )
    # Connections for obj86 (graphObject_: Obj70) named MT_post__Member
    self.drawConnections(
(self.obj86,self.obj114,[776.0, 341.0, 754.6, 277.8],"true", 2) )
    # Connections for obj87 (graphObject_: Obj71) named MT_post__MatchModel
    self.drawConnections(
(self.obj87,self.obj99,[211.0, 189.0, 361.8, 199.8],"true", 2),
(self.obj87,self.obj105,[136.0, 261.0, 136.0, 401.0],"true", 2) )
    # Connections for obj88 (graphObject_: Obj72) named MT_post__ApplyModel
    self.drawConnections(
(self.obj88,self.obj100,[211.0, 581.0, 362.491532278, 586.86445],"true", 2) )
    # Connections for obj89 (graphObject_: Obj73) named MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj89,self.obj101,[711.0, 592.9016393442623, 1245.0, 424.5, 1245.0, 339.5],"true", 3),
(self.obj89,self.obj103,[711.0, 696.1803278688525, 1193.0, 684.5, 1193.0, 684.5],"true", 3),
(self.obj89,self.obj106,[711.0, 592.9016393442623, 990.0, 584.0, 1242.0, 481.0],"true", 3),
(self.obj89,self.obj108,[711.0, 696.1803278688525, 1292.49804688, 838.905737705],"true", 2) )
    # Connections for obj90 (graphObject_: Obj74) named MT_post__CommunityRoot
    self.drawConnections(
(self.obj90,self.obj118,[476.0, 721.0, 502.3915322780172, 694.0332000000001],"true", 2) )
    # Connections for obj91 (graphObject_: Obj75) named MT_post__Person
    self.drawConnections(
(self.obj91,self.obj116,[616.0, 721.0, 609.8915322780176, 704.0332],"true", 2) )
    # Connections for obj92 (graphObject_: Obj76) named MT_post__Man
    self.drawConnections(
(self.obj92,self.obj117,[796.0, 721.0, 757.3915322780169, 694.0332000000001],"true", 2) )
    # Connections for obj93 (graphObject_: Obj77) named MT_post__Attribute
    self.drawConnections(
(self.obj93,self.obj119,[1636.0, 501.0, 1656.0, 461.0],"true", 2) )
    # Connections for obj94 (graphObject_: Obj78) named MT_post__Equation
    self.drawConnections(
(self.obj94,self.obj109,[1676.0, 141.0, 1618.0, 211.0],"true", 2),
(self.obj94,self.obj110,[1831.0, 121.0, 1866.15625, 208.0],"true", 2) )
    # Connections for obj95 (graphObject_: Obj79) named MT_post__Expression
    self.drawConnections(
 )
    # Connections for obj96 (graphObject_: Obj80) named MT_post__Constant
    self.drawConnections(
(self.obj96,self.obj120,[2041.0, 401.0, 1926.0, 405.0],"true", 2) )
    # Connections for obj97 (graphObject_: Obj81) named MT_post__Concat
    self.drawConnections(
(self.obj97,self.obj111,[1859.0, 721.0, 1780.0, 551.0],"true", 2),
(self.obj97,self.obj112,[1979.0, 721.0, 1965.53125, 535.0],"true", 2),
(self.obj97,self.obj121,[1859.0, 721.0, 1831.0, 571.0],"true", 2) )
    # Connections for obj98 (graphObject_: Obj82) named MT_post__Woman
    self.drawConnections(
(self.obj98,self.obj122,[656.0, 921.0, 646.0, 821.5],"true", 2) )
    # Connections for obj123 (graphObject_: Obj131) named MT_post__GenericNode_FamiliesToPersonsMM
    self.drawConnections(
(self.obj123,self.obj124,[1.0, 41.0, -3.0, 5.0], 0, 2) )
    # Connections for obj99 (graphObject_: Obj83) named MT_post__match_contains
    self.drawConnections(
(self.obj99,self.obj83,[361.8, 199.8, 521.0, 192.98360655737704],"true", 2) )
    # Connections for obj100 (graphObject_: Obj85) named MT_post__apply_contains
    self.drawConnections(
(self.obj100,self.obj89,[362.491532278, 586.86445, 521.0, 592.9016393442623],"true", 2) )
    # Connections for obj101 (graphObject_: Obj87) named MT_post__backward_link
    self.drawConnections(
(self.obj101,self.obj83,[1245.0, 339.5, 1245.0, 254.5, 711.0, 243.1081967213115],"true", 3) )
    # Connections for obj102 (graphObject_: Obj89) named MT_post__indirectLink_S
    self.drawConnections(
(self.obj102,self.obj83,[1274.5, 81.5, 1274.5, 81.5, 711.0, 192.98360655737704],"true", 3) )
    # Connections for obj103 (graphObject_: Obj91) named MT_post__directLink_T
    self.drawConnections(
(self.obj103,self.obj89,[1193.0, 684.5, 1193.0, 684.5, 711.0, 696.1803278688525],"true", 3) )
    # Connections for obj104 (graphObject_: Obj93) named MT_post__directLink_S
    self.drawConnections(
(self.obj104,self.obj83,[950.5, 86.5, 950.5, 86.5, 711.0, 192.98360655737704],"true", 3) )
    # Connections for obj105 (graphObject_: Obj95) named MT_post__paired_with
    self.drawConnections(
(self.obj105,self.obj88,[136.0, 401.0, 136.0, 541.0],"true", 2) )
    # Connections for obj106 (graphObject_: Obj97) named MT_post__trace_link
    self.drawConnections(
(self.obj106,self.obj83,[1242.0, 481.0, 937.0, 308.0, 711.0, 291.44262295081967],"true", 3) )
    # Connections for obj107 (graphObject_: Obj99) named MT_post__hasAttr_S
    self.drawConnections(
(self.obj107,self.obj93,[1346.0, 240.97540983606558, 1516.0, 501.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj101) named MT_post__hasAttr_T
    self.drawConnections(
(self.obj108,self.obj93,[1292.49804688, 838.905737705, 1481.0, 621.0],"true", 2) )
    # Connections for obj109 (graphObject_: Obj103) named MT_post__leftExpr
    self.drawConnections(
(self.obj109,self.obj95,[1618.0, 211.0, 1683.0, 281.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj105) named MT_post__rightExpr
    self.drawConnections(
(self.obj110,self.obj95,[1866.15625, 208.0, 1803.0, 281.0],"true", 2) )
    # Connections for obj111 (graphObject_: Obj107) named MT_post__arg_1
    self.drawConnections(
(self.obj111,self.obj95,[1780.0, 551.0, 1763.0, 421.0],"true", 2) )
    # Connections for obj112 (graphObject_: Obj109) named MT_post__arg_2
    self.drawConnections(
(self.obj112,self.obj95,[1965.53125, 535.0, 1838.0, 401.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj132) named MT_post__GenericEdge_FamiliesToPersonsMM
    self.drawConnections(
(self.obj124,self.obj123,[-2.0, 5.0, 192.625, 1.0], 0, 2),
(self.obj124,self.obj83,[-0.36099999999999977, 5.0, 521.0, 192.98360655737704], 0, 2),
(self.obj124,self.obj84,[-0.36099999999999977, 5.0, 316.0, 341.0], 0, 2),
(self.obj124,self.obj85,[-0.36099999999999977, 5.0, 536.0, 341.0], 0, 2),
(self.obj124,self.obj86,[-0.36099999999999977, 5.0, 741.0, 381.0], 0, 2),
(self.obj124,self.obj87,[-0.36099999999999977, 5.0, 176.0, 121.0], 0, 2),
(self.obj124,self.obj88,[-0.36099999999999977, 5.0, 176.0, 541.0], 0, 2),
(self.obj124,self.obj89,[-0.36099999999999977, 5.0, 556.0, 541.2622950819672], 0, 2),
(self.obj124,self.obj90,[-0.36099999999999977, 5.0, 356.0, 721.0], 0, 2),
(self.obj124,self.obj91,[-0.36099999999999977, 5.0, 576.0, 721.0], 0, 2),
(self.obj124,self.obj92,[-0.36099999999999977, 5.0, 796.0, 721.0], 0, 2),
(self.obj124,self.obj93,[-0.36099999999999977, 5.0, 1481.0, 541.0], 0, 2),
(self.obj124,self.obj94,[-0.36099999999999977, 5.0, 1641.0, 69.0], 0, 2),
(self.obj124,self.obj95,[-0.36099999999999977, 5.0, 1641.0, 321.0], 0, 2),
(self.obj124,self.obj96,[-0.36099999999999977, 5.0, 2041.0, 321.0], 0, 2),
(self.obj124,self.obj97,[-0.36099999999999977, 5.0, 1821.0, 761.0], 0, 2),
(self.obj124,self.obj98,[-0.36099999999999977, 5.0, 576.0, 921.0], 0, 2),
(self.obj124,self.obj123,[-2.0, 5.0, 192.625, 1.0], 0, 2) )
    # Connections for obj113 (graphObject_: Obj111) of type CD_Inheritance3
    self.drawConnections(
(self.obj113,self.obj83,[641.4, 303.6, 636.0, 372.0],"true", 2) )
    # Connections for obj114 (graphObject_: Obj113) of type CD_Inheritance3
    self.drawConnections(
(self.obj114,self.obj83,[754.6, 277.8, 711.0, 291.44262295081967],"true", 2) )
    # Connections for obj115 (graphObject_: Obj115) of type CD_Inheritance3
    self.drawConnections(
(self.obj115,self.obj83,[468.4, 303.6, 521.0, 291.44262295081967],"true", 2) )
    # Connections for obj116 (graphObject_: Obj117) of type CD_Inheritance3
    self.drawConnections(
(self.obj116,self.obj89,[609.891532278, 704.0332, 596.0, 722.0],"true", 2) )
    # Connections for obj117 (graphObject_: Obj119) of type CD_Inheritance3
    self.drawConnections(
(self.obj117,self.obj89,[757.391532278, 694.0332, 711.0, 696.1803278688525],"true", 2) )
    # Connections for obj118 (graphObject_: Obj121) of type CD_Inheritance3
    self.drawConnections(
(self.obj118,self.obj89,[502.391532278, 694.0332, 521.0, 696.1803278688525],"true", 2) )
    # Connections for obj119 (graphObject_: Obj123) of type CD_Inheritance3
    self.drawConnections(
(self.obj119,self.obj95,[1656.0, 461.0, 1683.0, 421.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj125) of type CD_Inheritance3
    self.drawConnections(
(self.obj120,self.obj95,[1926.0, 405.0, 1838.0, 401.0],"true", 2) )
    # Connections for obj121 (graphObject_: Obj127) of type CD_Inheritance3
    self.drawConnections(
(self.obj121,self.obj95,[1831.0, 571.0, 1803.0, 421.0],"true", 2) )
    # Connections for obj122 (graphObject_: Obj129) of type CD_Inheritance3
    self.drawConnections(
(self.obj122,self.obj89,[646.0, 821.5, 636.0, 722.0],"true", 2) )

newfunction = MT_post__FamiliesToPersonsMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
