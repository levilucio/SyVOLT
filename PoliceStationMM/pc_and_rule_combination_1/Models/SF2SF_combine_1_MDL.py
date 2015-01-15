"""
__SF2SF_combine_1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Jan 15 17:40:42 2015
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
from MT_post__indirectLink_S import *
from MT_post__directLink_T import *
from MT_post__Female_S import *
from MT_post__Female_T import *
from MT_post__Station_T import *
from MT_post__trace_link import *
from MT_post__Station_S import *
from graph_RHS import *
from graph_LHS import *
from graph_MT_pre__indirectLink_S import *
from graph_MT_post__trace_link import *
from graph_MT_pre__trace_link import *
from graph_MT_post__directLink_T import *
from graph_MT_post__Station_T import *
from graph_MT_pre__Station_S import *
from graph_MT_pre__Station_T import *
from graph_MT_post__Station_S import *
from graph_MT_post__Female_T import *
from graph_MT_post__indirectLink_S import *
from graph_MT_pre__Female_T import *
from graph_MT_pre__Female_S import *
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

    self.obj60=MT_pre__Female_S(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj60.MT_pivotOut__.setValue('')
    self.obj60.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj60.MT_subtypeMatching__.setValue(('True', 0))
    self.obj60.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj60.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj60.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj60.MT_pivotIn__.setValue('')
    self.obj60.MT_pivotIn__.setNone()

    # MT_label__
    self.obj60.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj60.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj60.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj60.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj60.MT_pre__name.setHeight(15)

    self.obj60.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(800.0,220.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=MT_pre__Station_T(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj61.MT_pivotOut__.setValue('')
    self.obj61.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj61.MT_subtypeMatching__.setValue(('True', 0))
    self.obj61.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj61.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj61.MT_pivotIn__.setValue('')
    self.obj61.MT_pivotIn__.setNone()

    # MT_label__
    self.obj61.MT_label__.setValue('3')

    # MT_pre__name
    self.obj61.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj61.MT_pre__name.setHeight(15)

    self.obj61.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(600.0,400.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=MT_pre__Female_T(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj62.MT_pivotOut__.setValue('')
    self.obj62.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj62.MT_subtypeMatching__.setValue(('True', 0))
    self.obj62.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj62.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj62.MT_pivotIn__.setValue('')
    self.obj62.MT_pivotIn__.setNone()

    # MT_label__
    self.obj62.MT_label__.setValue('4')

    # MT_pre__name
    self.obj62.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj62.MT_pre__name.setHeight(15)

    self.obj62.graphClass_= graph_MT_pre__Female_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_T(800.0,400.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj65=MT_pre__indirectLink_S(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # MT_label__
    self.obj65.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj65.MT_pivotOut__.setValue('')
    self.obj65.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj65.MT_subtypeMatching__.setValue(('True', 0))
    self.obj65.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj65.MT_pivotIn__.setValue('')
    self.obj65.MT_pivotIn__.setNone()

    self.obj65.graphClass_= graph_MT_pre__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__indirectLink_S(761.0,261.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

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

    self.obj67=MT_pre__trace_link(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # MT_label__
    self.obj67.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj67.MT_pivotOut__.setValue('')
    self.obj67.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj67.MT_subtypeMatching__.setValue(('True', 0))
    self.obj67.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj67.MT_pivotIn__.setValue('')
    self.obj67.MT_pivotIn__.setNone()

    self.obj67.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(861.0,351.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj90=RHS(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # action
    self.obj90.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj90.action.setHeight(15)

    self.obj90.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(960.0,140.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=LHS(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # constraint
    self.obj91.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj91.constraint.setHeight(15)

    self.obj91.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(520.0,140.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj74=MT_post__indirectLink_S(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # MT_label__
    self.obj74.MT_label__.setValue('10')

    # MT_pivotOut__
    self.obj74.MT_pivotOut__.setValue('')
    self.obj74.MT_pivotOut__.setNone()

    self.obj74.graphClass_= graph_MT_post__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__indirectLink_S(1211.0,241.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj79=MT_post__directLink_T(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # MT_label__
    self.obj79.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj79.MT_pivotOut__.setValue('')
    self.obj79.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj79.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj79.MT_post__associationType.setHeight(15)

    self.obj79.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(1251.0,361.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=MT_post__Female_S(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # MT_label__
    self.obj80.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj80.MT_pivotOut__.setValue('')
    self.obj80.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj80.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj80.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj80.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj80.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj80.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj80.MT_post__name.setHeight(15)

    self.obj80.graphClass_= graph_MT_post__Female_S
    if self.genGraphics:
       new_obj = graph_MT_post__Female_S(1220.0,200.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=MT_post__Female_T(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # MT_label__
    self.obj81.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj81.MT_pivotOut__.setValue('')
    self.obj81.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj81.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj81.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj81.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj81.MT_post__name.setHeight(15)

    self.obj81.graphClass_= graph_MT_post__Female_T
    if self.genGraphics:
       new_obj = graph_MT_post__Female_T(1260.0,320.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=MT_post__Station_T(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # MT_label__
    self.obj82.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj82.MT_pivotOut__.setValue('')
    self.obj82.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj82.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj82.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj82.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj82.MT_post__name.setHeight(15)

    self.obj82.graphClass_= graph_MT_post__Station_T
    if self.genGraphics:
       new_obj = graph_MT_post__Station_T(1120.0,320.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=MT_post__trace_link(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # MT_label__
    self.obj83.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj83.MT_pivotOut__.setValue('')
    self.obj83.MT_pivotOut__.setNone()

    self.obj83.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1161.0,301.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=MT_post__trace_link(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # MT_label__
    self.obj84.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj84.MT_pivotOut__.setValue('')
    self.obj84.MT_pivotOut__.setNone()

    self.obj84.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1301.0,301.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj87=MT_post__Station_S(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # MT_label__
    self.obj87.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj87.MT_pivotOut__.setValue('')
    self.obj87.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj87.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj87.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj87.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj87.MT_post__name.setHeight(15)

    self.obj87.graphClass_= graph_MT_post__Station_S
    if self.genGraphics:
       new_obj = graph_MT_post__Station_S(1080.0,200.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    # Connections for obj59 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
(self.obj59,self.obj65,[661.0, 261.0, 761.0, 261.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj1) of type MT_pre__Female_S
    self.drawConnections(
 )
    # Connections for obj61 (graphObject_: Obj2) of type MT_pre__Station_T
    self.drawConnections(
(self.obj61,self.obj66,[661.0, 441.0, 661.0, 351.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj3) of type MT_pre__Female_T
    self.drawConnections(
(self.obj62,self.obj67,[861.0, 441.0, 861.0, 351.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj6) of type MT_pre__indirectLink_S
    self.drawConnections(
(self.obj65,self.obj60,[761.0, 261.0, 861.0, 261.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj7) of type MT_pre__trace_link
    self.drawConnections(
(self.obj66,self.obj59,[661.0, 351.0, 661.0, 261.0],"true", 2) )
    # Connections for obj67 (graphObject_: Obj8) of type MT_pre__trace_link
    self.drawConnections(
(self.obj67,self.obj60,[861.0, 351.0, 861.0, 261.0],"true", 2) )
    # Connections for obj90 (graphObject_: Obj31) of type RHS
    self.drawConnections(
 )
    # Connections for obj91 (graphObject_: Obj32) of type LHS
    self.drawConnections(
 )
    # Connections for obj74 (graphObject_: Obj15) of type MT_post__indirectLink_S
    self.drawConnections(
(self.obj74,self.obj80,[1211.0, 241.0, 1281.0, 241.0],"true", 2) )
    # Connections for obj79 (graphObject_: Obj20) of type MT_post__directLink_T
    self.drawConnections(
(self.obj79,self.obj81,[1251.0, 361.0, 1321.0, 361.0],"true", 2) )
    # Connections for obj80 (graphObject_: Obj21) of type MT_post__Female_S
    self.drawConnections(
 )
    # Connections for obj81 (graphObject_: Obj22) of type MT_post__Female_T
    self.drawConnections(
(self.obj81,self.obj84,[1321.0, 361.0, 1301.0, 301.0],"true", 2) )
    # Connections for obj82 (graphObject_: Obj23) of type MT_post__Station_T
    self.drawConnections(
(self.obj82,self.obj83,[1181.0, 361.0, 1161.0, 301.0],"true", 2),
(self.obj82,self.obj79,[1181.0, 361.0, 1251.0, 361.0],"true", 2) )
    # Connections for obj83 (graphObject_: Obj24) of type MT_post__trace_link
    self.drawConnections(
(self.obj83,self.obj87,[1161.0, 301.0, 1141.0, 241.0],"true", 2) )
    # Connections for obj84 (graphObject_: Obj25) of type MT_post__trace_link
    self.drawConnections(
(self.obj84,self.obj80,[1301.0, 301.0, 1281.0, 241.0],"true", 2) )
    # Connections for obj87 (graphObject_: Obj28) of type MT_post__Station_S
    self.drawConnections(
(self.obj87,self.obj74,[1141.0, 241.0, 1211.0, 241.0],"true", 2) )

newfunction = SF2SF_combine_1_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MT_post__PoliceStationMM_META', 'MoTifRule_META']

atom3version = '0.3'
