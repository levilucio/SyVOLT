"""
__MT_pre__FamiliesToPersonsMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Fri Apr 17 11:08:49 2015
_________________________________________________________________________________________
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

def MT_pre__FamiliesToPersonsMM_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('MT_pre__FamiliesToPersonsMM')

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
    self.obj28.Graphical_Appearance.setValue( ('MT_pre__MetaModelElement_S', self.obj28))

    # name
    self.obj28.name.setValue('MT_pre__MetaModelElement_S')

    # attributes
    self.obj28.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj28.attributes.setValue(lcobj2)

    # Abstract
    self.obj28.Abstract.setValue((None, 0))
    self.obj28.Abstract.config = 0

    # cardinality
    self.obj28.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__match_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__backward_link', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__indirectLink_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__indirectLink_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__directLink_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__directLink_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__trace_link', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj28.cardinality.setValue(lcobj2)

    # display
    self.obj28.display.setValue('Attributes:\n  - cardinality :: String\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From match_contains: 0 to N\n  - From backward_link: 0 to N\n  - To indirectLink_S: 0 to N\n  - From indirectLink_S: 0 to N\n  - To directLink_S: 0 to N\n  - From directLink_S: 0 to N\n  - From trace_link: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj28.display.setHeight(15)

    # Actions
    self.obj28.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj28.Actions.setValue(lcobj2)

    # Constraints
    self.obj28.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.Constraints.setValue(lcobj2)

    self.obj28.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,120.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.7901639344262295]
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
    self.obj29.Graphical_Appearance.setValue( ('MT_pre__HouseholdRoot', self.obj29))

    # name
    self.obj29.name.setValue('MT_pre__HouseholdRoot')

    # attributes
    self.obj29.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj29.attributes.setValue(lcobj2)

    # Abstract
    self.obj29.Abstract.setValue((None, 0))
    self.obj29.Abstract.config = 0

    # cardinality
    self.obj29.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj29.cardinality.setValue(lcobj2)

    # display
    self.obj29.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj29.display.setHeight(15)

    # Actions
    self.obj29.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj29.Actions.setValue(lcobj2)

    # Constraints
    self.obj29.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.Constraints.setValue(lcobj2)

    self.obj29.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,340.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj30.Graphical_Appearance.setValue( ('MT_pre__Family', self.obj30))

    # name
    self.obj30.name.setValue('MT_pre__Family')

    # attributes
    self.obj30.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj30.attributes.setValue(lcobj2)

    # Abstract
    self.obj30.Abstract.setValue((None, 0))
    self.obj30.Abstract.config = 0

    # cardinality
    self.obj30.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj30.cardinality.setValue(lcobj2)

    # display
    self.obj30.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj30.display.setHeight(15)

    # Actions
    self.obj30.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj30.Actions.setValue(lcobj2)

    # Constraints
    self.obj30.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj30.Constraints.setValue(lcobj2)

    self.obj30.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(500.0,340.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj31.Graphical_Appearance.setValue( ('MT_pre__Member', self.obj31))

    # name
    self.obj31.name.setValue('MT_pre__Member')

    # attributes
    self.obj31.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__cardinality', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj31.attributes.setValue(lcobj2)

    # Abstract
    self.obj31.Abstract.setValue((None, 0))
    self.obj31.Abstract.config = 0

    # cardinality
    self.obj31.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj31.cardinality.setValue(lcobj2)

    # display
    self.obj31.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj31.display.setHeight(15)

    # Actions
    self.obj31.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj31.Actions.setValue(lcobj2)

    # Constraints
    self.obj31.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj31.Constraints.setValue(lcobj2)

    self.obj31.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,340.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj32.Graphical_Appearance.setValue( ('MT_pre__MatchModel', self.obj32))

    # name
    self.obj32.name.setValue('MT_pre__MatchModel')

    # attributes
    self.obj32.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj32.attributes.setValue(lcobj2)

    # Abstract
    self.obj32.Abstract.setValue((None, 0))
    self.obj32.Abstract.config = 0

    # cardinality
    self.obj32.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__match_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__paired_with', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj32.cardinality.setValue(lcobj2)

    # display
    self.obj32.display.setValue('Multiplicities:\n  - To match_contains: 0 to N\n  - To paired_with: 1 to 1\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj32.display.setHeight(15)

    # Actions
    self.obj32.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj32.Actions.setValue(lcobj2)

    # Constraints
    self.obj32.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.Constraints.setValue(lcobj2)

    self.obj32.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,120.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj33.Graphical_Appearance.setValue( ('MT_pre__ApplyModel', self.obj33))

    # name
    self.obj33.name.setValue('MT_pre__ApplyModel')

    # attributes
    self.obj33.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj33.attributes.setValue(lcobj2)

    # Abstract
    self.obj33.Abstract.setValue((None, 0))
    self.obj33.Abstract.config = 0

    # cardinality
    self.obj33.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__apply_contains', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__paired_with', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj33.cardinality.setValue(lcobj2)

    # display
    self.obj33.display.setValue('Multiplicities:\n  - To apply_contains: 0 to N\n  - From paired_with: 1 to 1\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj33.display.setHeight(15)

    # Actions
    self.obj33.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj33.Actions.setValue(lcobj2)

    # Constraints
    self.obj33.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.Constraints.setValue(lcobj2)

    self.obj33.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,540.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.752
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj34.Graphical_Appearance.setValue( ('MT_pre__MetaModelElement_T', self.obj34))

    # name
    self.obj34.name.setValue('MT_pre__MetaModelElement_T')

    # attributes
    self.obj34.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj34.attributes.setValue(lcobj2)

    # Abstract
    self.obj34.Abstract.setValue((None, 0))
    self.obj34.Abstract.config = 0

    # cardinality
    self.obj34.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__apply_contains', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__backward_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__directLink_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__directLink_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__trace_link', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj34.cardinality.setValue(lcobj2)

    # display
    self.obj34.display.setValue('Attributes:\n  - classtype :: String\n  - name :: String\nMultiplicities:\n  - From apply_contains: 0 to N\n  - To backward_link: 0 to N\n  - To directLink_T: 0 to N\n  - From directLink_T: 0 to N\n  - To trace_link: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj34.display.setHeight(15)

    # Actions
    self.obj34.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj34.Actions.setValue(lcobj2)

    # Constraints
    self.obj34.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Constraints.setValue(lcobj2)

    self.obj34.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(520.0,540.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.672
       new_obj.layConstraints['scale'] = [1.3890624999999999, 1.290983606557377]
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
    self.obj35.Graphical_Appearance.setValue( ('MT_pre__CommunityRoot', self.obj35))

    # name
    self.obj35.name.setValue('MT_pre__CommunityRoot')

    # attributes
    self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj35.attributes.setValue(lcobj2)

    # Abstract
    self.obj35.Abstract.setValue((None, 0))
    self.obj35.Abstract.config = 0

    # cardinality
    self.obj35.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj35.cardinality.setValue(lcobj2)

    # display
    self.obj35.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj35.display.setHeight(15)

    # Actions
    self.obj35.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj35.Actions.setValue(lcobj2)

    # Constraints
    self.obj35.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Constraints.setValue(lcobj2)

    self.obj35.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(320.0,720.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj36.Graphical_Appearance.setValue( ('MT_pre__Person', self.obj36))

    # name
    self.obj36.name.setValue('MT_pre__Person')

    # attributes
    self.obj36.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj36.attributes.setValue(lcobj2)

    # Abstract
    self.obj36.Abstract.setValue((None, 0))
    self.obj36.Abstract.config = 0

    # cardinality
    self.obj36.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj36.cardinality.setValue(lcobj2)

    # display
    self.obj36.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj36.display.setHeight(15)

    # Actions
    self.obj36.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj36.Actions.setValue(lcobj2)

    # Constraints
    self.obj36.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Constraints.setValue(lcobj2)

    self.obj36.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(540.0,720.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj37.Graphical_Appearance.setValue( ('MT_pre__Man', self.obj37))

    # name
    self.obj37.name.setValue('MT_pre__Man')

    # attributes
    self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj37.attributes.setValue(lcobj2)

    # Abstract
    self.obj37.Abstract.setValue((None, 0))
    self.obj37.Abstract.config = 0

    # cardinality
    self.obj37.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj37.cardinality.setValue(lcobj2)

    # display
    self.obj37.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj37.display.setHeight(15)

    # Actions
    self.obj37.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj37.Actions.setValue(lcobj2)

    # Constraints
    self.obj37.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Constraints.setValue(lcobj2)

    self.obj37.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(760.0,720.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.5640625000000001, 1.0]
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
    self.obj38.Graphical_Appearance.setValue( ('MT_pre__Woman', self.obj38))

    # name
    self.obj38.name.setValue('MT_pre__Woman')

    # attributes
    self.obj38.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__classtype', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__name', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj38.attributes.setValue(lcobj2)

    # Abstract
    self.obj38.Abstract.setValue((None, 0))
    self.obj38.Abstract.config = 0

    # cardinality
    self.obj38.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj38.cardinality.setValue(lcobj2)

    # display
    self.obj38.display.setValue('Attributes:\nMultiplicities:\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj38.display.setHeight(15)

    # Actions
    self.obj38.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj38.Actions.setValue(lcobj2)

    # Constraints
    self.obj38.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.Constraints.setValue(lcobj2)

    self.obj38.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(560.0,920.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj54=CD_Class3(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # QOCA
    self.obj54.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj54.Graphical_Appearance.setValue( ('MT_pre__GenericNode_FamiliesToPersonsMM', self.obj54))

    # name
    self.obj54.name.setValue('MT_pre__GenericNode_FamiliesToPersonsMM')

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj54.attributes.setValue(lcobj2)

    # Abstract
    self.obj54.Abstract.setValue((None, 0))
    self.obj54.Abstract.config = 0

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericEdge_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj54.cardinality.setValue(lcobj2)

    # display
    self.obj54.display.setValue('Multiplicities:\n  - To GenericEdge_FamiliesToPersonsMM: 0 to N\n  - From GenericEdge_FamiliesToPersonsMM: 0 to N\n')
    self.obj54.display.setHeight(15)

    # Actions
    self.obj54.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj54.Actions.setValue(lcobj2)

    # Constraints
    self.obj54.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Constraints.setValue(lcobj2)

    self.obj54.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(0.0,0.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.05625, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj39=CD_Association3(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # QOCA
    self.obj39.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj39.Graphical_Appearance.setValue( ('MT_pre__match_contains', self.obj39))
    self.obj39.Graphical_Appearance.linkInfo=linkEditor(self,self.obj39.Graphical_Appearance.semObject, "match_contains")
    self.obj39.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('match_contains_1stLink', self.obj39.Graphical_Appearance.linkInfo.FirstLink))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('match_contains_1stSegment', self.obj39.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj39.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.Center.setValue( ('match_contains_Center', self.obj39.Graphical_Appearance.linkInfo))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('match_contains_2ndSegment', self.obj39.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('match_contains_2ndLink', self.obj39.Graphical_Appearance.linkInfo.SecondLink))
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.Center.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj39.Graphical_Appearance.semObject

    # name
    self.obj39.name.setValue('MT_pre__match_contains')

    # displaySelect
    self.obj39.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj39.displaySelect.config = 0

    # attributes
    self.obj39.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj39.attributes.setValue(lcobj2)

    # cardinality
    self.obj39.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MatchModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj39.cardinality.setValue(lcobj2)

    # display
    self.obj39.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MatchModel: 0 to N\n')
    self.obj39.display.setHeight(15)

    # Actions
    self.obj39.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj39.Actions.setValue(lcobj2)

    # Constraints
    self.obj39.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Constraints.setValue(lcobj2)

    self.obj39.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(361.8,199.8,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.3230000000000002, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=CD_Association3(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # QOCA
    self.obj40.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj40.Graphical_Appearance.setValue( ('MT_pre__apply_contains', self.obj40))
    self.obj40.Graphical_Appearance.linkInfo=linkEditor(self,self.obj40.Graphical_Appearance.semObject, "apply_contains")
    self.obj40.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('apply_contains_1stLink', self.obj40.Graphical_Appearance.linkInfo.FirstLink))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('apply_contains_1stSegment', self.obj40.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj40.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.Center.setValue( ('apply_contains_Center', self.obj40.Graphical_Appearance.linkInfo))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('apply_contains_2ndSegment', self.obj40.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('apply_contains_2ndLink', self.obj40.Graphical_Appearance.linkInfo.SecondLink))
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.Center.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj40.Graphical_Appearance.semObject

    # name
    self.obj40.name.setValue('MT_pre__apply_contains')

    # displaySelect
    self.obj40.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj40.displaySelect.config = 0

    # attributes
    self.obj40.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj40.attributes.setValue(lcobj2)

    # cardinality
    self.obj40.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__ApplyModel', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj40.cardinality.setValue(lcobj2)

    # display
    self.obj40.display.setValue('Multiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From ApplyModel: 0 to N\n')
    self.obj40.display.setHeight(15)

    # Actions
    self.obj40.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj40.Actions.setValue(lcobj2)

    # Constraints
    self.obj40.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Constraints.setValue(lcobj2)

    self.obj40.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(362.491532278,586.86445,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [1.316, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=CD_Association3(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # QOCA
    self.obj41.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj41.Graphical_Appearance.setValue( ('MT_pre__backward_link', self.obj41))
    self.obj41.Graphical_Appearance.linkInfo=linkEditor(self,self.obj41.Graphical_Appearance.semObject, "backward_link")
    self.obj41.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('backward_link_1stLink', self.obj41.Graphical_Appearance.linkInfo.FirstLink))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('grey', 20)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('backward_link_1stSegment', self.obj41.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj41.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.Center.setValue( ('backward_link_Center', self.obj41.Graphical_Appearance.linkInfo))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('grey', 20)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('backward_link_2ndSegment', self.obj41.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('backward_link_2ndLink', self.obj41.Graphical_Appearance.linkInfo.SecondLink))
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.Center.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj41.Graphical_Appearance.semObject

    # name
    self.obj41.name.setValue('MT_pre__backward_link')

    # displaySelect
    self.obj41.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj41.displaySelect.config = 0

    # attributes
    self.obj41.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj41.attributes.setValue(lcobj2)

    # cardinality
    self.obj41.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj41.cardinality.setValue(lcobj2)

    # display
    self.obj41.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj41.display.setHeight(15)

    # Actions
    self.obj41.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj41.Actions.setValue(lcobj2)

    # Constraints
    self.obj41.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Constraints.setValue(lcobj2)

    self.obj41.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1245.0,339.5,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=CD_Association3(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # QOCA
    self.obj42.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj42.Graphical_Appearance.setValue( ('MT_pre__indirectLink_S', self.obj42))
    self.obj42.Graphical_Appearance.linkInfo=linkEditor(self,self.obj42.Graphical_Appearance.semObject, "indirectLink_S")
    self.obj42.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('indirectLink_S_1stLink', self.obj42.Graphical_Appearance.linkInfo.FirstLink))
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('blue', 20)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('indirectLink_S_1stSegment', self.obj42.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj42.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.Center.setValue( ('indirectLink_S_Center', self.obj42.Graphical_Appearance.linkInfo))
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('blue', 20)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('indirectLink_S_2ndSegment', self.obj42.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('indirectLink_S_2ndLink', self.obj42.Graphical_Appearance.linkInfo.SecondLink))
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.Center.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj42.Graphical_Appearance.semObject

    # name
    self.obj42.name.setValue('MT_pre__indirectLink_S')

    # displaySelect
    self.obj42.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj42.displaySelect.config = 0

    # attributes
    self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj42.attributes.setValue(lcobj2)

    # cardinality
    self.obj42.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj42.cardinality.setValue(lcobj2)

    # display
    self.obj42.display.setValue('Multiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj42.display.setHeight(15)

    # Actions
    self.obj42.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj42.Actions.setValue(lcobj2)

    # Constraints
    self.obj42.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj42.Constraints.setValue(lcobj2)

    self.obj42.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1274.5,81.5,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.862, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=CD_Association3(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # QOCA
    self.obj43.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj43.Graphical_Appearance.setValue( ('MT_pre__directLink_T', self.obj43))
    self.obj43.Graphical_Appearance.linkInfo=linkEditor(self,self.obj43.Graphical_Appearance.semObject, "directLink_T")
    self.obj43.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_T_1stLink', self.obj43.Graphical_Appearance.linkInfo.FirstLink))
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_T_1stSegment', self.obj43.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj43.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_T_Center', self.obj43.Graphical_Appearance.linkInfo))
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_T_2ndSegment', self.obj43.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_T_2ndLink', self.obj43.Graphical_Appearance.linkInfo.SecondLink))
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.Center.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj43.Graphical_Appearance.semObject

    # name
    self.obj43.name.setValue('MT_pre__directLink_T')

    # displaySelect
    self.obj43.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj43.displaySelect.config = 0

    # attributes
    self.obj43.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__associationType', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj43.attributes.setValue(lcobj2)

    # cardinality
    self.obj43.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj43.cardinality.setValue(lcobj2)

    # display
    self.obj43.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_T: 0 to N\n  - From MetaModelElement_T: 0 to N\n')
    self.obj43.display.setHeight(15)

    # Actions
    self.obj43.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj43.Actions.setValue(lcobj2)

    # Constraints
    self.obj43.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.Constraints.setValue(lcobj2)

    self.obj43.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1193.0,684.5,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.185483870967742]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=CD_Association3(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # QOCA
    self.obj44.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj44.Graphical_Appearance.setValue( ('MT_pre__directLink_S', self.obj44))
    self.obj44.Graphical_Appearance.linkInfo=linkEditor(self,self.obj44.Graphical_Appearance.semObject, "directLink_S")
    self.obj44.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('directLink_S_1stLink', self.obj44.Graphical_Appearance.linkInfo.FirstLink))
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('yellow', 20)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('directLink_S_1stSegment', self.obj44.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj44.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.Center.setValue( ('directLink_S_Center', self.obj44.Graphical_Appearance.linkInfo))
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('yellow', 20)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('directLink_S_2ndSegment', self.obj44.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('directLink_S_2ndLink', self.obj44.Graphical_Appearance.linkInfo.SecondLink))
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.Center.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj44.Graphical_Appearance.semObject

    # name
    self.obj44.name.setValue('MT_pre__directLink_S')

    # displaySelect
    self.obj44.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj44.displaySelect.config = 0

    # attributes
    self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pre__associationType', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n', 80,15 )
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj44.attributes.setValue(lcobj2)

    # cardinality
    self.obj44.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj44.cardinality.setValue(lcobj2)

    # display
    self.obj44.display.setValue('Attributes:\n  - associationType :: String\nMultiplicities:\n  - To MetaModelElement_S: 0 to N\n  - From MetaModelElement_S: 0 to N\n')
    self.obj44.display.setHeight(15)

    # Actions
    self.obj44.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj44.Actions.setValue(lcobj2)

    # Constraints
    self.obj44.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj44.Constraints.setValue(lcobj2)

    self.obj44.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(950.5,86.5,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.862, 1.185483870967742]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=CD_Association3(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # QOCA
    self.obj45.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj45.Graphical_Appearance.setValue( ('MT_pre__paired_with', self.obj45))
    self.obj45.Graphical_Appearance.linkInfo=linkEditor(self,self.obj45.Graphical_Appearance.semObject, "paired_with")
    self.obj45.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('paired_with_1stLink', self.obj45.Graphical_Appearance.linkInfo.FirstLink))
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('paired_with_1stSegment', self.obj45.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj45.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.Center.setValue( ('paired_with_Center', self.obj45.Graphical_Appearance.linkInfo))
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('paired_with_2ndSegment', self.obj45.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('paired_with_2ndLink', self.obj45.Graphical_Appearance.linkInfo.SecondLink))
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.Center.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj45.Graphical_Appearance.semObject

    # name
    self.obj45.name.setValue('MT_pre__paired_with')

    # displaySelect
    self.obj45.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj45.displaySelect.config = 0

    # attributes
    self.obj45.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj45.attributes.setValue(lcobj2)

    # cardinality
    self.obj45.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__ApplyModel', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MatchModel', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj45.cardinality.setValue(lcobj2)

    # display
    self.obj45.display.setValue('Multiplicities:\n  - To ApplyModel: 1 to 1\n  - From MatchModel: 1 to 1\n')
    self.obj45.display.setHeight(15)

    # Actions
    self.obj45.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj45.Actions.setValue(lcobj2)

    # Constraints
    self.obj45.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.Constraints.setValue(lcobj2)

    self.obj45.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(136.0,401.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.344, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=CD_Association3(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # QOCA
    self.obj46.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj46.Graphical_Appearance.setValue( ('MT_pre__trace_link', self.obj46))
    self.obj46.Graphical_Appearance.linkInfo=linkEditor(self,self.obj46.Graphical_Appearance.semObject, "trace_link")
    self.obj46.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('trace_link_1stLink', self.obj46.Graphical_Appearance.linkInfo.FirstLink))
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('trace_link_1stSegment', self.obj46.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj46.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj46.Graphical_Appearance.linkInfo.Center.setValue( ('trace_link_Center', self.obj46.Graphical_Appearance.linkInfo))
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('trace_link_2ndSegment', self.obj46.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj46.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('trace_link_2ndLink', self.obj46.Graphical_Appearance.linkInfo.SecondLink))
    self.obj46.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj46.Graphical_Appearance.semObject
    self.obj46.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj46.Graphical_Appearance.semObject
    self.obj46.Graphical_Appearance.linkInfo.Center.semObject=self.obj46.Graphical_Appearance.semObject
    self.obj46.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj46.Graphical_Appearance.semObject
    self.obj46.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj46.Graphical_Appearance.semObject

    # name
    self.obj46.name.setValue('MT_pre__trace_link')

    # displaySelect
    self.obj46.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj46.displaySelect.config = 0

    # attributes
    self.obj46.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj46.attributes.setValue(lcobj2)

    # cardinality
    self.obj46.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_T', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj46.cardinality.setValue(lcobj2)

    # display
    self.obj46.display.setValue('Multiplicities:\n  - From MetaModelElement_T: 0 to N\n  - To MetaModelElement_S: 0 to N\n')
    self.obj46.display.setHeight(15)

    # Actions
    self.obj46.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj46.Actions.setValue(lcobj2)

    # Constraints
    self.obj46.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj46.Constraints.setValue(lcobj2)

    self.obj46.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1242.0,481.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.855, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj55=CD_Association3(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # QOCA
    self.obj55.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj55.Graphical_Appearance.setValue( ('MT_pre__GenericEdge_FamiliesToPersonsMM', self.obj55))
    self.obj55.Graphical_Appearance.linkInfo=linkEditor(self,self.obj55.Graphical_Appearance.semObject, "GenericEdge_FamiliesToPersonsMM")
    self.obj55.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_1stLink', self.obj55.Graphical_Appearance.linkInfo.FirstLink))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('purple', 20)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_1stSegment', self.obj55.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj55.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.Center.setValue( ('GenericEdge_FamiliesToPersonsMM_Center', self.obj55.Graphical_Appearance.linkInfo))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('purple', 20)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_2ndSegment', self.obj55.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('GenericEdge_FamiliesToPersonsMM_2ndLink', self.obj55.Graphical_Appearance.linkInfo.SecondLink))
    self.obj55.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.Center.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj55.Graphical_Appearance.semObject
    self.obj55.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj55.Graphical_Appearance.semObject

    # name
    self.obj55.name.setValue('MT_pre__GenericEdge_FamiliesToPersonsMM')

    # displaySelect
    self.obj55.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj55.displaySelect.config = 0

    # attributes
    self.obj55.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_pivotIn__', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('MT_subtypeMatching__', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('True', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj55.attributes.setValue(lcobj2)

    # cardinality
    self.obj55.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericNode_FamiliesToPersonsMM', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__GenericNode_FamiliesToPersonsMM', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_S', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__HouseholdRoot', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__Family', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__Member', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MatchModel', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__ApplyModel', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__MetaModelElement_T', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__CommunityRoot', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__Person', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__Man', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MT_pre__Woman', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj55.cardinality.setValue(lcobj2)

    # display
    self.obj55.display.setValue('Multiplicities:\n  - From GenericNode_FamiliesToPersonsMM: 0 to N\n  - To GenericNode_FamiliesToPersonsMM: 0 to N\n  - To MetaModelElement_S: 0 to N\n  - To HouseholdRoot: 0 to N\n  - To Family: 0 to N\n  - To Member: 0 to N\n  - To MatchModel: 0 to N\n  - To ApplyModel: 0 to N\n  - To MetaModelElement_T: 0 to N\n  - To CommunityRoot: 0 to N\n  - To Person: 0 to N\n  - To Man: 0 to N\n  - To Woman: 0 to N\n')
    self.obj55.display.setHeight(15)

    # Actions
    self.obj55.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('autoIncrLabel', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '\n#===============================================================================\n# Auto increment the label\n#===============================================================================\n\n# If there is already one, ignore\nif not self.MT_label__.isNone(): return\n\n# Get the maximum label of all MT_pre__ elements\nlabel = 0\nfor nt in self.parent.ASGroot.listNodes:\n    if nt.startswith(\'MT_pre__\'):\n        for node in self.parent.ASGroot.listNodes[nt]:\n            currLabel = 0\n            try:\n                currLabel = int(node.MT_label__.getValue())\n            except:\n                pass\n            if currLabel > label:\n                label = currLabel\n# The label of this instance will be the max label + 1\nself.MT_label__.setValue(str(label + 1))\n'))
    lcobj2.append(cobj2)
    self.obj55.Actions.setValue(lcobj2)

    # Constraints
    self.obj55.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Constraints.setValue(lcobj2)

    self.obj55.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(0.0,0.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [2.6390000000000002, 3.3193548387096774]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj47=CD_Inheritance3(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(641.4,303.6,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=CD_Inheritance3(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(754.6,277.8,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=CD_Inheritance3(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(468.4,303.6,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=CD_Inheritance3(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(609.891532278,704.0332,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=CD_Inheritance3(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    self.obj51.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(757.391532278,694.0332,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=CD_Inheritance3(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    self.obj52.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(502.391532278,694.0332,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=CD_Inheritance3(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    self.obj53.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(636.0,812.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named MT_pre__MetaModelElement_S
    self.drawConnections(
(self.obj28,self.obj42,[711.0, 195.02295081967213, 1026.0, 203.0, 1274.5, 81.5, 1274.5, 81.5],"true", 4),
(self.obj28,self.obj44,[711.0, 148.75409836065572, 950.5, 86.5, 950.5, 86.5],"true", 3) )
    # Connections for obj29 (graphObject_: Obj1) named MT_pre__HouseholdRoot
    self.drawConnections(
(self.obj29,self.obj49,[436.0, 341.0, 468.4, 303.6],"true", 2) )
    # Connections for obj30 (graphObject_: Obj2) named MT_pre__Family
    self.drawConnections(
(self.obj30,self.obj47,[656.0, 341.0, 641.4, 303.6],"true", 2) )
    # Connections for obj31 (graphObject_: Obj3) named MT_pre__Member
    self.drawConnections(
(self.obj31,self.obj48,[776.0, 341.0, 754.6, 277.8],"true", 2) )
    # Connections for obj32 (graphObject_: Obj4) named MT_pre__MatchModel
    self.drawConnections(
(self.obj32,self.obj39,[211.0, 189.0, 361.8, 199.8],"true", 2),
(self.obj32,self.obj45,[136.0, 261.0, 136.0, 401.0],"true", 2) )
    # Connections for obj33 (graphObject_: Obj5) named MT_pre__ApplyModel
    self.drawConnections(
(self.obj33,self.obj40,[211.0, 581.0, 362.491532278, 586.86445],"true", 2) )
    # Connections for obj34 (graphObject_: Obj6) named MT_pre__MetaModelElement_T
    self.drawConnections(
(self.obj34,self.obj41,[711.0, 569.811475409836, 1245.0, 424.5, 1245.0, 339.5],"true", 3),
(self.obj34,self.obj43,[711.0, 662.7622950819672, 1193.0, 684.5, 1193.0, 684.5],"true", 3),
(self.obj34,self.obj46,[711.0, 569.811475409836, 990.0, 584.0, 1242.0, 481.0],"true", 3) )
    # Connections for obj35 (graphObject_: Obj7) named MT_pre__CommunityRoot
    self.drawConnections(
(self.obj35,self.obj52,[476.0, 721.0, 502.3915322780172, 694.0332000000001],"true", 2) )
    # Connections for obj36 (graphObject_: Obj8) named MT_pre__Person
    self.drawConnections(
(self.obj36,self.obj50,[616.0, 721.0, 609.8915322780176, 704.0332],"true", 2) )
    # Connections for obj37 (graphObject_: Obj9) named MT_pre__Man
    self.drawConnections(
(self.obj37,self.obj51,[796.0, 721.0, 757.3915322780169, 694.0332000000001],"true", 2) )
    # Connections for obj38 (graphObject_: Obj10) named MT_pre__Woman
    self.drawConnections(
(self.obj38,self.obj53,[636.0, 921.0, 636.0, 812.5],"true", 2) )
    # Connections for obj54 (graphObject_: Obj41) named MT_pre__GenericNode_FamiliesToPersonsMM
    self.drawConnections(
(self.obj54,self.obj55,[1.0, 41.0, -3.0, 5.0], 0, 2) )
    # Connections for obj39 (graphObject_: Obj11) named MT_pre__match_contains
    self.drawConnections(
(self.obj39,self.obj28,[361.8, 199.8, 521.0, 214.85245901639345],"true", 2) )
    # Connections for obj40 (graphObject_: Obj13) named MT_pre__apply_contains
    self.drawConnections(
(self.obj40,self.obj34,[362.491532278, 586.86445, 521.0, 602.344262295082],"true", 2) )
    # Connections for obj41 (graphObject_: Obj15) named MT_pre__backward_link
    self.drawConnections(
(self.obj41,self.obj28,[1245.0, 339.5, 1245.0, 254.5, 711.0, 245.8360655737705],"true", 3) )
    # Connections for obj42 (graphObject_: Obj17) named MT_pre__indirectLink_S
    self.drawConnections(
(self.obj42,self.obj28,[1274.5, 81.5, 1274.5, 81.5, 711.0, 148.75409836065572],"true", 3) )
    # Connections for obj43 (graphObject_: Obj19) named MT_pre__directLink_T
    self.drawConnections(
(self.obj43,self.obj34,[1193.0, 684.5, 1193.0, 684.5, 711.0, 662.7622950819672],"true", 3) )
    # Connections for obj44 (graphObject_: Obj21) named MT_pre__directLink_S
    self.drawConnections(
(self.obj44,self.obj28,[950.5, 86.5, 950.5, 86.5, 711.0, 148.75409836065572],"true", 3) )
    # Connections for obj45 (graphObject_: Obj23) named MT_pre__paired_with
    self.drawConnections(
(self.obj45,self.obj33,[136.0, 401.0, 136.0, 541.0],"true", 2) )
    # Connections for obj46 (graphObject_: Obj25) named MT_pre__trace_link
    self.drawConnections(
(self.obj46,self.obj28,[1242.0, 481.0, 937.0, 308.0, 711.0, 280.95081967213116],"true", 3) )
    # Connections for obj55 (graphObject_: Obj42) named MT_pre__GenericEdge_FamiliesToPersonsMM
    self.drawConnections(
(self.obj55,self.obj54,[-2.0, 5.0, 192.625, 1.0], 0, 2),
(self.obj55,self.obj28,[-0.36099999999999977, 5.0, 521.0, 186.75409836065572], 0, 2),
(self.obj55,self.obj29,[-0.36099999999999977, 5.0, 316.0, 341.0], 0, 2),
(self.obj55,self.obj30,[-0.36099999999999977, 5.0, 536.0, 341.0], 0, 2),
(self.obj55,self.obj31,[-0.36099999999999977, 5.0, 741.0, 381.0], 0, 2),
(self.obj55,self.obj32,[-0.36099999999999977, 5.0, 176.0, 121.0], 0, 2),
(self.obj55,self.obj33,[-0.36099999999999977, 5.0, 176.0, 541.0], 0, 2),
(self.obj55,self.obj34,[-0.36099999999999977, 5.0, 556.0, 541.3360655737705], 0, 2),
(self.obj55,self.obj35,[-0.36099999999999977, 5.0, 356.0, 721.0], 0, 2),
(self.obj55,self.obj36,[-0.36099999999999977, 5.0, 576.0, 721.0], 0, 2),
(self.obj55,self.obj37,[-0.36099999999999977, 5.0, 796.0, 721.0], 0, 2),
(self.obj55,self.obj38,[-0.36099999999999977, 5.0, 596.0, 921.0], 0, 2),
(self.obj55,self.obj54,[-2.0, 5.0, 192.625, 1.0], 0, 2) )
    # Connections for obj47 (graphObject_: Obj27) of type CD_Inheritance3
    self.drawConnections(
(self.obj47,self.obj28,[641.4, 303.6, 636.0, 352.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj29) of type CD_Inheritance3
    self.drawConnections(
(self.obj48,self.obj28,[754.6, 277.8, 711.0, 277.6393442622951],"true", 2) )
    # Connections for obj49 (graphObject_: Obj31) of type CD_Inheritance3
    self.drawConnections(
(self.obj49,self.obj28,[468.4, 303.6, 521.0, 318.95081967213116],"true", 2) )
    # Connections for obj50 (graphObject_: Obj33) of type CD_Inheritance3
    self.drawConnections(
(self.obj50,self.obj34,[609.891532278, 704.0332, 596.0, 704.0],"true", 2) )
    # Connections for obj51 (graphObject_: Obj35) of type CD_Inheritance3
    self.drawConnections(
(self.obj51,self.obj34,[757.391532278, 694.0332, 711.0, 680.7622950819672],"true", 2) )
    # Connections for obj52 (graphObject_: Obj37) of type CD_Inheritance3
    self.drawConnections(
(self.obj52,self.obj34,[502.391532278, 694.0332, 521.0, 680.7622950819672],"true", 2) )
    # Connections for obj53 (graphObject_: Obj39) of type CD_Inheritance3
    self.drawConnections(
(self.obj53,self.obj34,[636.0, 812.5, 636.0, 704.0],"true", 2) )

newfunction = MT_pre__FamiliesToPersonsMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
