"""
__ConnectPPortPrototype_Back_CompositionType2ECU_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Aug 26 09:47:22 2013
____________________________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MatchModel import *
from MT_pre__ApplyModel import *
from MT_pre__ECU import *
from MT_pre__CompositionType import *
from MT_pre__paired_with import *
from MT_pre__match_contains import *
from MT_pre__apply_contains import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__paired_with import *
from graph_MT_pre__apply_contains import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__CompositionType import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_MT_pre__ApplyModel import *
from graph_MT_pre__ECU import *
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

def ConnectPPortPrototype_Back_CompositionType2ECU_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__GM2AUTOSAR_MM ---
    if( MT_pre__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_pre__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_pre__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_pre__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_pre__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('ConnectPPortPrototype_Back_CompositionType2ECU')
    # --- ASG attributes over ---


    self.obj47=MT_pre__MatchModel(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # MT_label__
    self.obj47.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj47.MT_pivotOut__.setValue('')
    self.obj47.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj47.MT_subtypeMatching__.setValue(('True', 0))
    self.obj47.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj47.MT_pivotIn__.setValue('')
    self.obj47.MT_pivotIn__.setNone()

    self.obj47.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(40.0,60.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=MT_pre__ApplyModel(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # MT_label__
    self.obj48.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj48.MT_pivotOut__.setValue('')
    self.obj48.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj48.MT_subtypeMatching__.setValue(('True', 0))
    self.obj48.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj48.MT_pivotIn__.setValue('')
    self.obj48.MT_pivotIn__.setNone()

    self.obj48.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(40.0,300.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=MT_pre__ECU(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj49.MT_pivotOut__.setValue('')
    self.obj49.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj49.MT_subtypeMatching__.setValue(('True', 0))
    self.obj49.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj49.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj49.MT_pivotIn__.setValue('')
    self.obj49.MT_pivotIn__.setNone()

    # MT_label__
    self.obj49.MT_label__.setValue('5')

    # MT_pre__cardinality
    self.obj49.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj49.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__name.setHeight(15)

    self.obj49.graphClass_= graph_MT_pre__ECU
    if self.genGraphics:
       new_obj = graph_MT_pre__ECU(240.0,120.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ECU", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=MT_pre__CompositionType(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj50.MT_pivotOut__.setValue('')
    self.obj50.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj50.MT_subtypeMatching__.setValue(('True', 0))
    self.obj50.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj50.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj50.MT_pivotIn__.setValue('')
    self.obj50.MT_pivotIn__.setNone()

    # MT_label__
    self.obj50.MT_label__.setValue('4')

    # MT_pre__cardinality
    self.obj50.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj50.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__name.setHeight(15)

    self.obj50.graphClass_= graph_MT_pre__CompositionType
    if self.genGraphics:
       new_obj = graph_MT_pre__CompositionType(240.0,260.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__CompositionType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj56=MT_pre__paired_with(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # MT_label__
    self.obj56.MT_label__.setValue('9')

    # MT_pivotOut__
    self.obj56.MT_pivotOut__.setValue('')
    self.obj56.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj56.MT_subtypeMatching__.setValue(('True', 0))
    self.obj56.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj56.MT_pivotIn__.setValue('')
    self.obj56.MT_pivotIn__.setNone()

    self.obj56.graphClass_= graph_MT_pre__paired_with
    if self.genGraphics:
       new_obj = graph_MT_pre__paired_with(203.5,253.5,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__paired_with", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj52=MT_pre__match_contains(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # MT_label__
    self.obj52.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj52.MT_pivotOut__.setValue('')
    self.obj52.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj52.MT_pivotIn__.setValue('')
    self.obj52.MT_pivotIn__.setNone()

    self.obj52.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(304.5,163.5,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=MT_pre__apply_contains(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # MT_label__
    self.obj53.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj53.MT_pivotOut__.setValue('')
    self.obj53.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj53.MT_subtypeMatching__.setValue(('True', 0))
    self.obj53.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj53.MT_pivotIn__.setValue('')
    self.obj53.MT_pivotIn__.setNone()

    self.obj53.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(308.0,353.5,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj57=MT_pre__trace_link(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # MT_label__
    self.obj57.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj57.MT_pivotOut__.setValue('')
    self.obj57.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj57.MT_subtypeMatching__.setValue(('True', 0))
    self.obj57.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj57.MT_pivotIn__.setValue('')
    self.obj57.MT_pivotIn__.setNone()

    self.obj57.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(409.0,263.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj55=LHS(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # constraint
    self.obj55.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj55.constraint.setHeight(15)

    self.obj55.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,40.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    # Connections for obj47 (graphObject_: Obj0) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj47,self.obj52,[199.0, 133.0, 304.5, 163.5],"true", 2),
(self.obj47,self.obj56,[199.0, 133.0, 203.5, 253.5],"true", 2) )
    # Connections for obj48 (graphObject_: Obj1) of type MT_pre__ApplyModel
    self.drawConnections(
(self.obj48,self.obj53,[208.0, 374.0, 308.0, 353.5],"true", 2) )
    # Connections for obj49 (graphObject_: Obj2) of type MT_pre__ECU
    self.drawConnections(
 )
    # Connections for obj50 (graphObject_: Obj3) of type MT_pre__CompositionType
    self.drawConnections(
(self.obj50,self.obj57,[408.0, 333.0, 409.0, 263.5],"true", 2) )
    # Connections for obj56 (graphObject_: Obj9) of type MT_pre__paired_with
    self.drawConnections(
(self.obj56,self.obj48,[203.5, 253.5, 208.0, 374.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj5) of type MT_pre__match_contains
    self.drawConnections(
(self.obj52,self.obj49,[304.5, 163.5, 410.0, 194.0],"true", 2) )
    # Connections for obj53 (graphObject_: Obj6) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj53,self.obj50,[308.0, 353.5, 408.0, 333.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj10) of type MT_pre__trace_link
    self.drawConnections(
(self.obj57,self.obj49,[409.0, 263.5, 410.0, 194.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj8) of type LHS
    self.drawConnections(
 )

newfunction = ConnectPPortPrototype_Back_CompositionType2ECU_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
