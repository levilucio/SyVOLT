"""
__built_traceability_for_rule_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon May  4 15:07:39 2015
_________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_post__MatchModel import *
from MT_post__ApplyModel import *
from MT_post__MetaModelElement_S import *
from MT_post__MetaModelElement_T import *
from MT_post__match_contains import *
from MT_post__apply_contains import *
from MT_post__trace_link import *
from MT_pre__ApplyModel import *
from MT_pre__MatchModel import *
from MT_pre__match_contains import *
from MT_pre__apply_contains import *
from MT_pre__MetaModelElement_T import *
from MT_pre__MetaModelElement_S import *
from RHS import *
from LHS import *
from graph_MT_pre__MetaModelElement_S import *
from graph_MT_post__MetaModelElement_S import *
from graph_MT_post__match_contains import *
from graph_MT_pre__apply_contains import *
from graph_MT_post__MetaModelElement_T import *
from graph_LHS import *
from graph_MT_post__ApplyModel import *
from graph_MT_pre__match_contains import *
from graph_MT_pre__MatchModel import *
from graph_MT_pre__ApplyModel import *
from graph_MT_post__MatchModel import *
from graph_MT_post__apply_contains import *
from graph_MT_pre__MetaModelElement_T import *
from graph_RHS import *
from graph_MT_post__trace_link import *
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

def built_traceability_for_rule_MDL(self, rootNode, MT_post__GM2AUTOSAR_MMRootNode=None, MT_pre__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_post__GM2AUTOSAR_MM ---
    if( MT_post__GM2AUTOSAR_MMRootNode ): 
        # author
        MT_post__GM2AUTOSAR_MMRootNode.author.setValue('Annonymous')

        # description
        MT_post__GM2AUTOSAR_MMRootNode.description.setValue('\n')
        MT_post__GM2AUTOSAR_MMRootNode.description.setHeight(15)

        # name
        MT_post__GM2AUTOSAR_MMRootNode.name.setValue('')
        MT_post__GM2AUTOSAR_MMRootNode.name.setNone()
    # --- ASG attributes over ---


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
        MoTifRuleRootNode.name.setValue('BuildTraceabilityForRule')
    # --- ASG attributes over ---


    self.obj92=MT_post__MatchModel(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # MT_label__
    self.obj92.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj92.MT_pivotOut__.setValue('')
    self.obj92.MT_pivotOut__.setNone()

    self.obj92.graphClass_= graph_MT_post__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_post__MatchModel(680.0,200.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=MT_post__ApplyModel(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # MT_label__
    self.obj93.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj93.MT_pivotOut__.setValue('')
    self.obj93.MT_pivotOut__.setNone()

    self.obj93.graphClass_= graph_MT_post__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_post__ApplyModel(680.0,340.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj71=MT_post__MetaModelElement_S(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj71.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj71.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj71.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj71.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj71.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj71.MT_post__name.setHeight(15)

    self.obj71.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(856.0,232.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=MT_post__MetaModelElement_T(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # MT_label__
    self.obj72.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj72.MT_pivotOut__.setValue('')
    self.obj72.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj72.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj72.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj72.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj72.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj72.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj72.MT_post__name.setHeight(15)

    self.obj72.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(856.0,412.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj94=MT_post__match_contains(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # MT_label__
    self.obj94.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj94.MT_pivotOut__.setValue('')
    self.obj94.MT_pivotOut__.setNone()

    self.obj94.graphClass_= graph_MT_post__match_contains
    if self.genGraphics:
       new_obj = graph_MT_post__match_contains(934.0,289.5,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=MT_post__apply_contains(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # MT_label__
    self.obj95.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj95.MT_pivotOut__.setValue('')
    self.obj95.MT_pivotOut__.setNone()

    self.obj95.graphClass_= graph_MT_post__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_post__apply_contains(936.0,449.5,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj73=MT_post__trace_link(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_label__
    self.obj73.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('')
    self.obj73.MT_pivotOut__.setNone()

    self.obj73.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1025.0,395.5,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj89=MT_pre__ApplyModel(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # MT_label__
    self.obj89.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj89.MT_pivotOut__.setValue('')
    self.obj89.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj89.MT_subtypeMatching__.setValue(('True', 0))
    self.obj89.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj89.MT_pivotIn__.setValue('')
    self.obj89.MT_pivotIn__.setNone()

    self.obj89.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(160.0,300.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj87=MT_pre__MatchModel(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj87.MT_subtypeMatching__.setValue(('True', 0))
    self.obj87.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj87.MT_pivotIn__.setValue('')
    self.obj87.MT_pivotIn__.setNone()

    self.obj87.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(160.0,180.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj90=MT_pre__match_contains(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # MT_label__
    self.obj90.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj90.MT_pivotOut__.setValue('')
    self.obj90.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj90.MT_subtypeMatching__.setValue(('True', 0))
    self.obj90.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj90.MT_pivotIn__.setValue('')
    self.obj90.MT_pivotIn__.setNone()

    self.obj90.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(414.5,273.5,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=MT_pre__apply_contains(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # MT_label__
    self.obj91.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj91.MT_pivotOut__.setValue('')
    self.obj91.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj91.MT_subtypeMatching__.setValue(('True', 0))
    self.obj91.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj91.MT_pivotIn__.setValue('')
    self.obj91.MT_pivotIn__.setNone()

    self.obj91.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(418.0,423.5,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj74=MT_pre__MetaModelElement_T(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj74.MT_subtypeMatching__.setValue(('True', 1))
    self.obj74.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj74.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj74.MT_pivotIn__.setValue('')
    self.obj74.MT_pivotIn__.setNone()

    # MT_label__
    self.obj74.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj74.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj74.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj74.MT_pre__name.setHeight(15)

    self.obj74.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(340.0,400.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=MT_pre__MetaModelElement_S(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj75.MT_subtypeMatching__.setValue(('True', 1))
    self.obj75.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj75.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj75.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj75.MT_pivotIn__.setValue('')
    self.obj75.MT_pivotIn__.setNone()

    # MT_label__
    self.obj75.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj75.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj75.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj75.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj75.MT_pre__name.setHeight(15)

    self.obj75.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(340.0,220.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=RHS(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # action
    self.obj76.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj76.action.setHeight(15)

    self.obj76.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(560.0,160.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=LHS(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # constraint
    self.obj77.constraint.setValue('#if (len([i for i in graph.neighbors(PreNode(\'1\').index) if graph.vs[i][\'mm__\'] == \'backward_link\']) == 0) and (len([i for i in graph.neighbors(PreNode(\'2\').index) if graph.vs[i][\'mm__\'] == \'backward_link\']) == 0):\n#    return True\n\n#return False\nreturn True\n')
    self.obj77.constraint.setHeight(15)

    self.obj77.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(140.0,160.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    # Connections for obj92 (graphObject_: Obj17) of type MT_post__MatchModel
    self.drawConnections(
(self.obj92,self.obj94,[842.0, 273.0, 934.0, 289.5],"true", 2) )
    # Connections for obj93 (graphObject_: Obj18) of type MT_post__ApplyModel
    self.drawConnections(
(self.obj93,self.obj95,[848.0, 414.0, 936.0, 449.5],"true", 2) )
    # Connections for obj71 (graphObject_: Obj0) of type MT_post__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj72 (graphObject_: Obj1) of type MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj72,self.obj73,[1024.0, 485.0, 1025.0, 395.5],"true", 2) )
    # Connections for obj94 (graphObject_: Obj19) of type MT_post__match_contains
    self.drawConnections(
(self.obj94,self.obj71,[934.0, 289.5, 1026.0, 306.0],"true", 2) )
    # Connections for obj95 (graphObject_: Obj20) of type MT_post__apply_contains
    self.drawConnections(
(self.obj95,self.obj72,[936.0, 449.5, 1024.0, 485.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj2) of type MT_post__trace_link
    self.drawConnections(
(self.obj73,self.obj71,[1025.0, 395.5, 1026.0, 306.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj14) of type MT_pre__ApplyModel
    self.drawConnections(
(self.obj89,self.obj91,[328.0, 374.0, 418.0, 423.5],"true", 2) )
    # Connections for obj87 (graphObject_: Obj12) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj87,self.obj90,[319.0, 253.0, 414.5, 273.5],"true", 2) )
    # Connections for obj90 (graphObject_: Obj15) of type MT_pre__match_contains
    self.drawConnections(
(self.obj90,self.obj75,[414.5, 273.5, 510.0, 294.0],"true", 2) )
    # Connections for obj91 (graphObject_: Obj16) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj91,self.obj74,[418.0, 423.5, 508.0, 473.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj3) of type MT_pre__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj75 (graphObject_: Obj4) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj76 (graphObject_: Obj5) of type RHS
    self.drawConnections(
 )
    # Connections for obj77 (graphObject_: Obj6) of type LHS
    self.drawConnections(
 )

newfunction = built_traceability_for_rule_MDL

loadedMMName = ['MT_post__GM2AUTOSAR_MM_META', 'MT_pre__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
