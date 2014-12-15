"""
__SF2SF_combine_1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Mon Dec 15 10:33:47 2014
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Station_S import *
from MT_pre__Female_S import *
from MT_pre__Station_T import *
from MT_pre__Female_T import *
from MT_pre__indirectLink_S import *
from MT_pre__trace_link import *
from RHS import *
from LHS import *
from MT_post__Attribute import *
from MT_post__Equation import *
from MT_post__indirectLink_S import *
from MT_post__hasAttr_S import *
from MT_post__Constant import *
from MT_post__directLink_T import *
from MT_post__Female_S import *
from MT_post__Female_T import *
from MT_post__Station_T import *
from MT_post__trace_link import *
from MT_post__rightExpr import *
from MT_post__Station_S import *
from MT_post__leftExpr import *
from graph_RHS import *
from graph_MT_post__indirectLink_S import *
from graph_MT_post__leftExpr import *
from graph_MT_post__Attribute import *
from graph_LHS import *
from graph_MT_post__Constant import *
from graph_MT_post__trace_link import *
from graph_MT_post__hasAttr_S import *
from graph_MT_pre__Station_S import *
from graph_MT_post__Equation import *
from graph_MT_post__Station_T import *
from graph_MT_pre__indirectLink_S import *
from graph_MT_post__directLink_T import *
from graph_MT_pre__Station_T import *
from graph_MT_post__Station_S import *
from graph_MT_post__Female_T import *
from graph_MT_post__rightExpr import *
from graph_MT_pre__Female_T import *
from graph_MT_pre__Female_S import *
from graph_MT_pre__trace_link import *
from graph_MT_post__Female_S import *
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

def SF2SF_combine_1_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MT_post__PoliceStationMMRootNode=None, MoTifRuleRootNode=None):

    # --- Generating attributes code for ASG MT_pre__PoliceStationMM ---
    if( MT_pre__PoliceStationMMRootNode ): 
        # author
        MT_pre__PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__PoliceStationMMRootNode.description.setValue('\n')
        MT_pre__PoliceStationMMRootNode.description.setHeight(15)

        # name
        MT_pre__PoliceStationMMRootNode.name.setValue('')
        MT_pre__PoliceStationMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MT_post__PoliceStationMM ---
    if( MT_post__PoliceStationMMRootNode ): 
        # author
        MT_post__PoliceStationMMRootNode.author.setValue('Annonymous')

        # description
        MT_post__PoliceStationMMRootNode.description.setValue('\n')
        MT_post__PoliceStationMMRootNode.description.setHeight(15)

        # name
        MT_post__PoliceStationMMRootNode.name.setValue('')
        MT_post__PoliceStationMMRootNode.name.setNone()
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('SF2SF_combine_1')
    # --- ASG attributes over ---


    self.obj59=MT_pre__Station_S(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj59.MT_pivotOut__.setValue('')
    self.obj59.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj59.MT_subtypeMatching__.setValue(('True', 0))
    self.obj59.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj59.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj59.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj59.MT_pivotIn__.setValue('')
    self.obj59.MT_pivotIn__.setNone()

    # MT_label__
    self.obj59.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj59.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj59.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj59.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj59.MT_pre__name.setHeight(15)

    self.obj59.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(600.0,220.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj92=MT_pre__Female_S(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj92.MT_pivotOut__.setValue('')
    self.obj92.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj92.MT_subtypeMatching__.setValue(('True', 0))
    self.obj92.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj92.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj92.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj92.MT_pivotIn__.setValue('')
    self.obj92.MT_pivotIn__.setNone()

    # MT_label__
    self.obj92.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj92.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj92.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj92.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj92.MT_pre__name.setHeight(15)

    self.obj92.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(800.0,220.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj63=MT_pre__Station_T(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj63.MT_pivotOut__.setValue('')
    self.obj63.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj63.MT_subtypeMatching__.setValue(('True', 0))
    self.obj63.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj63.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj63.MT_pivotIn__.setValue('')
    self.obj63.MT_pivotIn__.setNone()

    # MT_label__
    self.obj63.MT_label__.setValue('3')

    # MT_pre__name
    self.obj63.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj63.MT_pre__name.setHeight(15)

    self.obj63.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(600.0,400.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj93=MT_pre__Female_T(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj93.MT_pivotOut__.setValue('')
    self.obj93.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj93.MT_subtypeMatching__.setValue(('True', 0))
    self.obj93.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj93.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj93.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj93.MT_pivotIn__.setValue('')
    self.obj93.MT_pivotIn__.setNone()

    # MT_label__
    self.obj93.MT_label__.setValue('4')

    # MT_pre__name
    self.obj93.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj93.MT_pre__name.setHeight(15)

    self.obj93.graphClass_= graph_MT_pre__Female_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_T(800.0,400.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj5592=MT_pre__indirectLink_S(self)
    self.obj5592.isGraphObjectVisual = True

    if(hasattr(self.obj5592, '_setHierarchicalLink')):
      self.obj5592._setHierarchicalLink(False)

    # MT_label__
    self.obj5592.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj5592.MT_pivotOut__.setValue('')
    self.obj5592.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj5592.MT_subtypeMatching__.setValue(('True', 0))
    self.obj5592.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj5592.MT_pivotIn__.setValue('')
    self.obj5592.MT_pivotIn__.setNone()

    self.obj5592.graphClass_= graph_MT_pre__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__indirectLink_S(761.0,261.0,self.obj5592)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj5592.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj5592)
    self.globalAndLocalPostcondition(self.obj5592, rootNode)
    self.obj5592.postAction( rootNode.CREATE )

    self.obj66=MT_pre__trace_link(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # MT_label__
    self.obj66.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj66.MT_pivotOut__.setValue('')
    self.obj66.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj66.MT_subtypeMatching__.setValue(('True', 0))
    self.obj66.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj66.MT_pivotIn__.setValue('')
    self.obj66.MT_pivotIn__.setNone()

    self.obj66.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(661.0,351.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj105=MT_pre__trace_link(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # MT_label__
    self.obj105.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj105.MT_pivotOut__.setValue('')
    self.obj105.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj105.MT_subtypeMatching__.setValue(('True', 0))
    self.obj105.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj105.MT_pivotIn__.setValue('')
    self.obj105.MT_pivotIn__.setNone()

    self.obj105.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(861.0,351.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj89=RHS(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # action
    self.obj89.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj89.action.setHeight(15)

    self.obj89.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(1003.0,160.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=LHS(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # constraint
    self.obj90.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj90.constraint.setHeight(15)

    self.obj90.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(540.0,160.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj68=MT_post__Attribute(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # MT_label__
    self.obj68.MT_label__.setValue('12')

    # MT_pivotOut__
    self.obj68.MT_pivotOut__.setValue('')
    self.obj68.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj68.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "name"\n')
    self.obj68.MT_post__name.setHeight(15)

    self.obj68.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(1060.0,460.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=MT_post__Attribute(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # MT_label__
    self.obj69.MT_label__.setValue('16')

    # MT_pivotOut__
    self.obj69.MT_pivotOut__.setValue('')
    self.obj69.MT_pivotOut__.setNone()

    # MT_post__name
    self.obj69.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "name"\n')
    self.obj69.MT_post__name.setHeight(15)

    self.obj69.graphClass_= graph_MT_post__Attribute
    if self.genGraphics:
       new_obj = graph_MT_post__Attribute(1380.0,200.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Attribute", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=MT_post__Equation(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # MT_label__
    self.obj70.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj70.MT_pivotOut__.setValue('')
    self.obj70.MT_pivotOut__.setNone()

    self.obj70.graphClass_= graph_MT_post__Equation
    if self.genGraphics:
       new_obj = graph_MT_post__Equation(1140.0,460.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=MT_post__Equation(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # MT_label__
    self.obj71.MT_label__.setValue('17')

    # MT_pivotOut__
    self.obj71.MT_pivotOut__.setValue('')
    self.obj71.MT_pivotOut__.setNone()

    self.obj71.graphClass_= graph_MT_post__Equation
    if self.genGraphics:
       new_obj = graph_MT_post__Equation(1360.0,320.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Equation", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj177=MT_post__indirectLink_S(self)
    self.obj177.isGraphObjectVisual = True

    if(hasattr(self.obj177, '_setHierarchicalLink')):
      self.obj177._setHierarchicalLink(False)

    # MT_label__
    self.obj177.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj177.MT_pivotOut__.setValue('')
    self.obj177.MT_pivotOut__.setNone()

    self.obj177.graphClass_= graph_MT_post__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__indirectLink_S(1211.0,241.0,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)
    self.obj177.postAction( rootNode.CREATE )

    self.obj73=MT_post__hasAttr_S(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # MT_label__
    self.obj73.MT_label__.setValue('15')

    # MT_pivotOut__
    self.obj73.MT_pivotOut__.setValue('')
    self.obj73.MT_pivotOut__.setNone()

    self.obj73.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(1127.0,365.5,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj183=MT_post__hasAttr_S(self)
    self.obj183.isGraphObjectVisual = True

    if(hasattr(self.obj183, '_setHierarchicalLink')):
      self.obj183._setHierarchicalLink(False)

    # MT_label__
    self.obj183.MT_label__.setValue('25')

    # MT_pivotOut__
    self.obj183.MT_pivotOut__.setValue('')
    self.obj183.MT_pivotOut__.setNone()

    self.obj183.graphClass_= graph_MT_post__hasAttr_S
    if self.genGraphics:
       new_obj = graph_MT_post__hasAttr_S(1357.0,235.5,self.obj183)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__hasAttr_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj183.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj183)
    self.globalAndLocalPostcondition(self.obj183, rootNode)
    self.obj183.postAction( rootNode.CREATE )

    self.obj75=MT_post__Constant(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # MT_label__
    self.obj75.MT_label__.setValue('14')

    # MT_pivotOut__
    self.obj75.MT_pivotOut__.setValue('')
    self.obj75.MT_pivotOut__.setNone()

    # MT_post__value
    self.obj75.MT_post__value.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "somestation"\n')
    self.obj75.MT_post__value.setHeight(15)

    self.obj75.graphClass_= graph_MT_post__Constant
    if self.genGraphics:
       new_obj = graph_MT_post__Constant(1260.0,420.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=MT_post__Constant(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # MT_label__
    self.obj76.MT_label__.setValue('18')

    # MT_pivotOut__
    self.obj76.MT_pivotOut__.setValue('')
    self.obj76.MT_pivotOut__.setNone()

    # MT_post__value
    self.obj76.MT_post__value.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn "somemale"\n')
    self.obj76.MT_post__value.setHeight(15)

    self.obj76.graphClass_= graph_MT_post__Constant
    if self.genGraphics:
       new_obj = graph_MT_post__Constant(1380.0,460.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Constant", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj180=MT_post__directLink_T(self)
    self.obj180.isGraphObjectVisual = True

    if(hasattr(self.obj180, '_setHierarchicalLink')):
      self.obj180._setHierarchicalLink(False)

    # MT_label__
    self.obj180.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj180.MT_pivotOut__.setValue('')
    self.obj180.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj180.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj180.MT_post__associationType.setHeight(15)

    self.obj180.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(1251.0,361.0,self.obj180)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj180.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj180)
    self.globalAndLocalPostcondition(self.obj180, rootNode)
    self.obj180.postAction( rootNode.CREATE )

    self.obj164=MT_post__Female_S(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    # MT_label__
    self.obj164.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj164.MT_pivotOut__.setValue('')
    self.obj164.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj164.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj164.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj164.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj164.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj164.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj164.MT_post__name.setHeight(15)

    self.obj164.graphClass_= graph_MT_post__Female_S
    if self.genGraphics:
       new_obj = graph_MT_post__Female_S(1220.0,200.0,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=MT_post__Female_T(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    # MT_label__
    self.obj165.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj165.MT_pivotOut__.setValue('')
    self.obj165.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj165.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj165.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj165.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj165.MT_post__name.setHeight(15)

    self.obj165.graphClass_= graph_MT_post__Female_T
    if self.genGraphics:
       new_obj = graph_MT_post__Female_T(1260.0,320.0,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj78=MT_post__Station_T(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # MT_label__
    self.obj78.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj78.MT_pivotOut__.setValue('')
    self.obj78.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj78.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj78.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj78.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj78.MT_post__name.setHeight(15)

    self.obj78.graphClass_= graph_MT_post__Station_T
    if self.genGraphics:
       new_obj = graph_MT_post__Station_T(1120.0,320.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=MT_post__trace_link(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # MT_label__
    self.obj79.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj79.MT_pivotOut__.setValue('')
    self.obj79.MT_pivotOut__.setNone()

    self.obj79.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1161.0,301.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj170=MT_post__trace_link(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    # MT_label__
    self.obj170.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj170.MT_pivotOut__.setValue('')
    self.obj170.MT_pivotOut__.setNone()

    self.obj170.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1301.0,301.0,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj81=MT_post__rightExpr(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('20')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    self.obj81.graphClass_= graph_MT_post__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_post__rightExpr(1263.5,480.5,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=MT_post__rightExpr(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_label__
    self.obj82.MT_label__.setValue('23')

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    self.obj82.graphClass_= graph_MT_post__rightExpr
    if self.genGraphics:
       new_obj = graph_MT_post__rightExpr(1433.5,430.5,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__rightExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=MT_post__Station_S(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_label__
    self.obj83.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj83.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj83.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj83.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj83.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj83.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj83.MT_post__name.setHeight(15)

    self.obj83.graphClass_= graph_MT_post__Station_S
    if self.genGraphics:
       new_obj = graph_MT_post__Station_S(1080.0,200.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj86=MT_post__leftExpr(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # MT_label__
    self.obj86.MT_label__.setValue('19')

    # MT_pivotOut__
    self.obj86.MT_pivotOut__.setValue('')
    self.obj86.MT_pivotOut__.setNone()

    self.obj86.graphClass_= graph_MT_post__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_post__leftExpr(1162.5,496.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=MT_post__leftExpr(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('22')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    self.obj87.graphClass_= graph_MT_post__leftExpr
    if self.genGraphics:
       new_obj = graph_MT_post__leftExpr(1432.5,296.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__leftExpr", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    # Connections for obj59 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
(self.obj59,self.obj5592,[661.0, 261.0, 761.0, 261.0],"true", 2) )
    # Connections for obj92 (graphObject_: Obj33) of type MT_pre__Female_S
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj4) of type MT_pre__Station_T
    self.drawConnections(
(self.obj63,self.obj66,[661.0, 441.0, 661.0, 351.0],"true", 2) )
    # Connections for obj93 (graphObject_: Obj34) of type MT_pre__Female_T
    self.drawConnections(
(self.obj93,self.obj105,[861.0, 441.0, 861.0, 351.0],"true", 2) )
    # Connections for obj5592 (graphObject_: Obj48) of type MT_pre__indirectLink_S
    self.drawConnections(
(self.obj5592,self.obj92,[761.0, 261.0, 861.0, 261.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj7) of type MT_pre__trace_link
    self.drawConnections(
(self.obj66,self.obj59,[661.0, 351.0, 661.0, 261.0],"true", 2) )
    # Connections for obj105 (graphObject_: Obj35) of type MT_pre__trace_link
    self.drawConnections(
(self.obj105,self.obj92,[861.0, 351.0, 861.0, 261.0],"true", 2) )
    # Connections for obj89 (graphObject_: Obj30) of type RHS
    self.drawConnections(
 )
    # Connections for obj90 (graphObject_: Obj31) of type LHS
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj9) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj69 (graphObject_: Obj10) of type MT_post__Attribute
    self.drawConnections(
 )
    # Connections for obj70 (graphObject_: Obj11) of type MT_post__Equation
    self.drawConnections(
(self.obj70,self.obj86,[1212.0, 502.0, 1162.5, 496.0],"true", 2),
(self.obj70,self.obj81,[1212.0, 502.0, 1263.5, 480.5],"true", 2) )
    # Connections for obj71 (graphObject_: Obj12) of type MT_post__Equation
    self.drawConnections(
(self.obj71,self.obj87,[1432.0, 362.0, 1432.5, 296.0],"true", 2),
(self.obj71,self.obj82,[1432.0, 362.0, 1433.5, 430.5],"true", 2) )
    # Connections for obj177 (graphObject_: Obj45) of type MT_post__indirectLink_S
    self.drawConnections(
(self.obj177,self.obj164,[1211.0, 241.0, 1281.0, 241.0],"true", 2) )
    # Connections for obj73 (graphObject_: Obj14) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj73,self.obj68,[1127.0, 365.5, 1113.0, 490.0],"true", 2) )
    # Connections for obj183 (graphObject_: Obj47) of type MT_post__hasAttr_S
    self.drawConnections(
(self.obj183,self.obj69,[1357.0, 235.5, 1433.0, 230.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj16) of type MT_post__Constant
    self.drawConnections(
 )
    # Connections for obj76 (graphObject_: Obj17) of type MT_post__Constant
    self.drawConnections(
 )
    # Connections for obj180 (graphObject_: Obj46) of type MT_post__directLink_T
    self.drawConnections(
(self.obj180,self.obj165,[1251.0, 361.0, 1321.0, 361.0],"true", 2) )
    # Connections for obj164 (graphObject_: Obj42) of type MT_post__Female_S
    self.drawConnections(
(self.obj164,self.obj183,[1281.0, 241.0, 1357.0, 235.5],"true", 2) )
    # Connections for obj165 (graphObject_: Obj43) of type MT_post__Female_T
    self.drawConnections(
(self.obj165,self.obj170,[1321.0, 361.0, 1301.0, 301.0],"true", 2) )
    # Connections for obj78 (graphObject_: Obj19) of type MT_post__Station_T
    self.drawConnections(
(self.obj78,self.obj79,[1181.0, 361.0, 1161.0, 301.0],"true", 2),
(self.obj78,self.obj180,[1181.0, 361.0, 1251.0, 361.0],"true", 2) )
    # Connections for obj79 (graphObject_: Obj20) of type MT_post__trace_link
    self.drawConnections(
(self.obj79,self.obj83,[1161.0, 301.0, 1141.0, 241.0],"true", 2) )
    # Connections for obj170 (graphObject_: Obj44) of type MT_post__trace_link
    self.drawConnections(
(self.obj170,self.obj164,[1301.0, 301.0, 1281.0, 241.0],"true", 2) )
    # Connections for obj81 (graphObject_: Obj22) of type MT_post__rightExpr
    self.drawConnections(
(self.obj81,self.obj75,[1263.5, 480.5, 1315.0, 459.0],"true", 2) )
    # Connections for obj82 (graphObject_: Obj23) of type MT_post__rightExpr
    self.drawConnections(
(self.obj82,self.obj76,[1433.5, 430.5, 1435.0, 499.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj24) of type MT_post__Station_S
    self.drawConnections(
(self.obj83,self.obj73,[1141.0, 241.0, 1127.0, 365.5],"true", 2),
(self.obj83,self.obj177,[1141.0, 241.0, 1211.0, 241.0],"true", 2) )
    # Connections for obj86 (graphObject_: Obj27) of type MT_post__leftExpr
    self.drawConnections(
(self.obj86,self.obj68,[1162.5, 496.0, 1113.0, 490.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj28) of type MT_post__leftExpr
    self.drawConnections(
(self.obj87,self.obj69,[1432.5, 296.0, 1433.0, 230.0],"true", 2) )

newfunction = SF2SF_combine_1_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MT_post__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
