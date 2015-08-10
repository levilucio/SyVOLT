"""
__built_traceability_for_rule_v2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Sun Aug  9 22:25:17 2015
____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__MatchModel import *
from MT_pre__ApplyModel import *
from MT_pre__MetaModelElement_S import *
from MT_pre__MetaModelElement_T import *
from MT_pre__match_contains import *
from MT_pre__apply_contains import *
from MT_post__match_contains import *
from MT_post__MetaModelElement_S import *
from MT_post__MetaModelElement_T import *
from MT_post__MatchModel import *
from MT_post__ApplyModel import *
from MT_post__trace_link import *
from MT_post__apply_contains import *
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

def built_traceability_for_rule_v2_MDL(self, rootNode, MT_pre__GM2AUTOSAR_MMRootNode=None, MT_post__GM2AUTOSAR_MMRootNode=None, MoTifRuleRootNode=None):

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


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('BuildTraceabilityForRulev2')
    # --- ASG attributes over ---


    self.obj77=MT_pre__MatchModel(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # MT_label__
    self.obj77.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj77.MT_pivotOut__.setValue('')
    self.obj77.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj77.MT_subtypeMatching__.setValue(('True', 0))
    self.obj77.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj77.MT_pivotIn__.setValue('')
    self.obj77.MT_pivotIn__.setNone()

    self.obj77.graphClass_= graph_MT_pre__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_pre__MatchModel(220.0,160.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=MT_pre__ApplyModel(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # MT_label__
    self.obj78.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj78.MT_pivotOut__.setValue('')
    self.obj78.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj78.MT_subtypeMatching__.setValue(('True', 0))
    self.obj78.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj78.MT_pivotIn__.setValue('')
    self.obj78.MT_pivotIn__.setNone()

    self.obj78.graphClass_= graph_MT_pre__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_pre__ApplyModel(220.0,300.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=MT_pre__MetaModelElement_S(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj79.MT_pivotOut__.setValue('')
    self.obj79.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj79.MT_subtypeMatching__.setValue(('True', 0))
    self.obj79.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj79.MT_pivotIn__.setValue('')
    self.obj79.MT_pivotIn__.setNone()

    # MT_label__
    self.obj79.MT_label__.setValue('3')

    # MT_pre__attr2
    self.obj79.MT_pre__attr2.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj79.MT_pre__attr2.setHeight(15)

    # MT_pre__attr1
    self.obj79.MT_pre__attr1.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj79.MT_pre__attr1.setHeight(15)

    self.obj79.graphClass_= graph_MT_pre__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_S(400.0,200.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=MT_pre__MetaModelElement_T(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj80.MT_pivotOut__.setValue('')
    self.obj80.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj80.MT_subtypeMatching__.setValue(('True', 0))
    self.obj80.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj80.MT_pivotIn__.setValue('')
    self.obj80.MT_pivotIn__.setNone()

    # MT_label__
    self.obj80.MT_label__.setValue('4')

    # MT_pre__attr2
    self.obj80.MT_pre__attr2.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj80.MT_pre__attr2.setHeight(15)

    # MT_pre__attr1
    self.obj80.MT_pre__attr1.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj80.MT_pre__attr1.setHeight(15)

    self.obj80.graphClass_= graph_MT_pre__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_pre__MetaModelElement_T(400.0,340.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=MT_pre__match_contains(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj81.MT_subtypeMatching__.setValue(('True', 0))
    self.obj81.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj81.MT_pivotIn__.setValue('')
    self.obj81.MT_pivotIn__.setNone()

    self.obj81.graphClass_= graph_MT_pre__match_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__match_contains(474.5,253.5,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=MT_pre__apply_contains(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_label__
    self.obj82.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj82.MT_subtypeMatching__.setValue(('True', 0))
    self.obj82.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj82.MT_pivotIn__.setValue('')
    self.obj82.MT_pivotIn__.setNone()

    self.obj82.graphClass_= graph_MT_pre__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_pre__apply_contains(478.0,393.5,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj87=MT_post__match_contains(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    self.obj87.graphClass_= graph_MT_post__match_contains
    if self.genGraphics:
       new_obj = graph_MT_post__match_contains(976.0,263.5,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__match_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj85=MT_post__MetaModelElement_S(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # MT_label__
    self.obj85.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj85.MT_pivotOut__.setValue('')
    self.obj85.MT_pivotOut__.setNone()

    # MT_post__attr2
    self.obj85.MT_post__attr2.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj85.MT_post__attr2.setHeight(15)

    # MT_post__attr1
    self.obj85.MT_post__attr1.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj85.MT_post__attr1.setHeight(15)

    self.obj85.graphClass_= graph_MT_post__MetaModelElement_S
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_S(900.0,220.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=MT_post__MetaModelElement_T(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # MT_label__
    self.obj86.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj86.MT_pivotOut__.setValue('')
    self.obj86.MT_pivotOut__.setNone()

    # MT_post__attr2
    self.obj86.MT_post__attr2.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj86.MT_post__attr2.setHeight(15)

    # MT_post__attr1
    self.obj86.MT_post__attr1.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj86.MT_post__attr1.setHeight(15)

    self.obj86.graphClass_= graph_MT_post__MetaModelElement_T
    if self.genGraphics:
       new_obj = graph_MT_post__MetaModelElement_T(900.0,360.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj83=MT_post__MatchModel(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_label__
    self.obj83.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    self.obj83.graphClass_= graph_MT_post__MatchModel
    if self.genGraphics:
       new_obj = graph_MT_post__MatchModel(720.0,160.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__MatchModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=MT_post__ApplyModel(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # MT_label__
    self.obj84.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj84.MT_pivotOut__.setValue('')
    self.obj84.MT_pivotOut__.setNone()

    self.obj84.graphClass_= graph_MT_post__ApplyModel
    if self.genGraphics:
       new_obj = graph_MT_post__ApplyModel(720.0,300.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj95=MT_post__trace_link(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # MT_label__
    self.obj95.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj95.MT_pivotOut__.setValue('')
    self.obj95.MT_pivotOut__.setNone()

    self.obj95.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1069.0,363.5,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj88=MT_post__apply_contains(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # MT_label__
    self.obj88.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj88.MT_pivotOut__.setValue('')
    self.obj88.MT_pivotOut__.setNone()

    self.obj88.graphClass_= graph_MT_post__apply_contains
    if self.genGraphics:
       new_obj = graph_MT_post__apply_contains(978.0,403.5,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj75=RHS(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # action
    self.obj75.action.setValue('if set([i for i in graph.neighbors(PreNode(\'1\').index) if graph.vs[i][\'mm__\'] == \'trace_link\']).intersection(set([i for i in graph.neighbors(PreNode(\'2\').index) if graph.vs[i][\'mm__\'] == \'trace_link\'])) == set():\n    return True\n\nreturn False\n')
    self.obj75.action.setHeight(15)

    self.obj75.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(600.0,120.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj74=LHS(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # constraint
    self.obj74.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj74.constraint.setHeight(15)

    self.obj74.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(180.0,120.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    # Connections for obj77 (graphObject_: Obj3) of type MT_pre__MatchModel
    self.drawConnections(
(self.obj77,self.obj81,[379.0, 233.0, 474.5, 253.5],"true", 2) )
    # Connections for obj78 (graphObject_: Obj4) of type MT_pre__ApplyModel
    self.drawConnections(
(self.obj78,self.obj82,[388.0, 374.0, 478.0, 393.5],"true", 2) )
    # Connections for obj79 (graphObject_: Obj5) of type MT_pre__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj80 (graphObject_: Obj6) of type MT_pre__MetaModelElement_T
    self.drawConnections(
 )
    # Connections for obj81 (graphObject_: Obj7) of type MT_pre__match_contains
    self.drawConnections(
(self.obj81,self.obj79,[474.5, 253.5, 570.0, 274.0],"true", 2) )
    # Connections for obj82 (graphObject_: Obj8) of type MT_pre__apply_contains
    self.drawConnections(
(self.obj82,self.obj80,[478.0, 393.5, 568.0, 413.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj13) of type MT_post__match_contains
    self.drawConnections(
(self.obj87,self.obj85,[976.0, 263.5, 1070.0, 294.0],"true", 2) )
    # Connections for obj85 (graphObject_: Obj11) of type MT_post__MetaModelElement_S
    self.drawConnections(
 )
    # Connections for obj86 (graphObject_: Obj12) of type MT_post__MetaModelElement_T
    self.drawConnections(
(self.obj86,self.obj95,[1068.0, 433.0, 1069.0, 363.5],"true", 2) )
    # Connections for obj83 (graphObject_: Obj9) of type MT_post__MatchModel
    self.drawConnections(
(self.obj83,self.obj87,[882.0, 233.0, 976.0, 263.5],"true", 2) )
    # Connections for obj84 (graphObject_: Obj10) of type MT_post__ApplyModel
    self.drawConnections(
(self.obj84,self.obj88,[888.0, 374.0, 978.0, 403.5],"true", 2) )
    # Connections for obj95 (graphObject_: Obj17) of type MT_post__trace_link
    self.drawConnections(
(self.obj95,self.obj85,[1069.0, 363.5, 1070.0, 294.0],"true", 2) )
    # Connections for obj88 (graphObject_: Obj14) of type MT_post__apply_contains
    self.drawConnections(
(self.obj88,self.obj86,[978.0, 403.5, 1068.0, 433.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj1) of type RHS
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = built_traceability_for_rule_v2_MDL

loadedMMName = ['MT_pre__GM2AUTOSAR_MM_META', 'MT_post__GM2AUTOSAR_MM_META', 'MoTifRule_META']

atom3version = '0.3'
