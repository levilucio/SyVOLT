"""
__SF2SF_combine_1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: levi
Modified: Thu Dec  4 14:31:26 2014
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
from MT_post__trace_link import *
from MT_post__directLink_T import *
from MT_post__indirectLink_S import *
from MT_post__Female_T import *
from MT_post__Female_S import *
from MT_post__Station_S import *
from MT_post__Station_T import *
from RHS import *
from LHS import *
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

def SF2SF_combine_1_MDL(self, rootNode, MT_pre__PoliceStationMMRootNode=None, MoTifRuleRootNode=None, MT_post__PoliceStationMMRootNode=None):

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


    self.obj49=MT_pre__Station_S(self)
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
    self.obj49.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj49.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj49.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj49.MT_pre__name.setHeight(15)

    self.obj49.graphClass_= graph_MT_pre__Station_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_S(560.0,220.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=MT_pre__Female_S(self)
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
    self.obj50.MT_label__.setValue('2')

    # MT_pre__cardinality
    self.obj50.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj50.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj50.MT_pre__name.setHeight(15)

    self.obj50.graphClass_= graph_MT_pre__Female_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_S(760.0,220.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=MT_pre__Station_T(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj51.MT_pivotOut__.setValue('')
    self.obj51.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj51.MT_subtypeMatching__.setValue(('True', 0))
    self.obj51.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj51.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj51.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj51.MT_pivotIn__.setValue('')
    self.obj51.MT_pivotIn__.setNone()

    # MT_label__
    self.obj51.MT_label__.setValue('3')

    # MT_pre__name
    self.obj51.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj51.MT_pre__name.setHeight(15)

    self.obj51.graphClass_= graph_MT_pre__Station_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Station_T(560.0,400.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=MT_pre__Female_T(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj52.MT_pivotOut__.setValue('')
    self.obj52.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj52.MT_subtypeMatching__.setValue(('True', 0))
    self.obj52.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj52.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj52.MT_pivotIn__.setValue('')
    self.obj52.MT_pivotIn__.setNone()

    # MT_label__
    self.obj52.MT_label__.setValue('4')

    # MT_pre__name
    self.obj52.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj52.MT_pre__name.setHeight(15)

    self.obj52.graphClass_= graph_MT_pre__Female_T
    if self.genGraphics:
       new_obj = graph_MT_pre__Female_T(760.0,400.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj66=MT_pre__indirectLink_S(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # MT_label__
    self.obj66.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj66.MT_pivotOut__.setValue('')
    self.obj66.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj66.MT_subtypeMatching__.setValue(('True', 0))
    self.obj66.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj66.MT_pivotIn__.setValue('')
    self.obj66.MT_pivotIn__.setNone()

    self.obj66.graphClass_= graph_MT_pre__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__indirectLink_S(721.0,261.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj54=MT_pre__trace_link(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # MT_label__
    self.obj54.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj54.MT_pivotOut__.setValue('')
    self.obj54.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj54.MT_subtypeMatching__.setValue(('True', 0))
    self.obj54.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj54.MT_pivotIn__.setValue('')
    self.obj54.MT_pivotIn__.setNone()

    self.obj54.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(621.0,351.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=MT_pre__trace_link(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # MT_label__
    self.obj55.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj55.MT_pivotOut__.setValue('')
    self.obj55.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj55.MT_subtypeMatching__.setValue(('True', 0))
    self.obj55.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj55.MT_pivotIn__.setValue('')
    self.obj55.MT_pivotIn__.setNone()

    self.obj55.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(821.0,351.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj58=MT_post__trace_link(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # MT_label__
    self.obj58.MT_label__.setValue('5')

    # MT_pivotOut__
    self.obj58.MT_pivotOut__.setValue('')
    self.obj58.MT_pivotOut__.setNone()

    self.obj58.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1143.0,348.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=MT_post__trace_link(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # MT_label__
    self.obj59.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj59.MT_pivotOut__.setValue('')
    self.obj59.MT_pivotOut__.setNone()

    self.obj59.graphClass_= graph_MT_post__trace_link
    if self.genGraphics:
       new_obj = graph_MT_post__trace_link(1341.0,351.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj61=MT_post__directLink_T(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # MT_label__
    self.obj61.MT_label__.setValue('8')

    # MT_pivotOut__
    self.obj61.MT_pivotOut__.setValue('')
    self.obj61.MT_pivotOut__.setNone()

    # MT_post__associationType
    self.obj61.MT_post__associationType.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj61.MT_post__associationType.setHeight(15)

    self.obj61.graphClass_= graph_MT_post__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_post__directLink_T(1242.0,438.5,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj67=MT_post__indirectLink_S(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # MT_label__
    self.obj67.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj67.MT_pivotOut__.setValue('')
    self.obj67.MT_pivotOut__.setNone()

    self.obj67.graphClass_= graph_MT_post__indirectLink_S
    if self.genGraphics:
       new_obj = graph_MT_post__indirectLink_S(1242.0,260.5,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj62=MT_post__Female_T(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # MT_label__
    self.obj62.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj62.MT_pivotOut__.setValue('')
    self.obj62.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj62.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj62.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj62.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj62.MT_post__name.setHeight(15)

    self.obj62.graphClass_= graph_MT_post__Female_T
    if self.genGraphics:
       new_obj = graph_MT_post__Female_T(1280.0,400.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=MT_post__Female_S(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # MT_label__
    self.obj63.MT_label__.setValue('2')

    # MT_pivotOut__
    self.obj63.MT_pivotOut__.setValue('')
    self.obj63.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj63.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj63.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj63.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj63.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj63.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj63.MT_post__name.setHeight(15)

    self.obj63.graphClass_= graph_MT_post__Female_S
    if self.genGraphics:
       new_obj = graph_MT_post__Female_S(1280.0,220.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Female_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=MT_post__Station_S(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # MT_label__
    self.obj64.MT_label__.setValue('1')

    # MT_pivotOut__
    self.obj64.MT_pivotOut__.setValue('')
    self.obj64.MT_pivotOut__.setNone()

    # MT_post__cardinality
    self.obj64.MT_post__cardinality.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj64.MT_post__cardinality.setHeight(15)

    # MT_post__classtype
    self.obj64.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj64.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj64.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj64.MT_post__name.setHeight(15)

    self.obj64.graphClass_= graph_MT_post__Station_S
    if self.genGraphics:
       new_obj = graph_MT_post__Station_S(1082.0,219.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=MT_post__Station_T(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # MT_label__
    self.obj65.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj65.MT_pivotOut__.setValue('')
    self.obj65.MT_pivotOut__.setNone()

    # MT_post__classtype
    self.obj65.MT_post__classtype.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj65.MT_post__classtype.setHeight(15)

    # MT_post__name
    self.obj65.MT_post__name.setValue('\n#===============================================================================\n# You can access the value of the current node\'s attribute value by: attr_value.\n# If the current node shall be created you MUST initialize it here!\n# You can access a node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# Note that the attribute values are those before the match is rewritten.\n# The order in which this code is executed depends on the label value\n# of the encapsulating node.\n# The given action must return the new value of the attribute.\n#===============================================================================\n\nreturn attr_value\n')
    self.obj65.MT_post__name.setHeight(15)

    self.obj65.graphClass_= graph_MT_post__Station_T
    if self.genGraphics:
       new_obj = graph_MT_post__Station_T(1082.0,395.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj56=RHS(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # action
    self.obj56.action.setValue('#===============================================================================\n# This code is executed after the rule has been applied.\n# You can access a node labelled n matched by this rule by: PostNode(\'n\').\n# To access attribute x of node n, use: PostNode(\'n\')[\'x\'].\n#===============================================================================\n\npass\n')
    self.obj56.action.setHeight(15)

    self.obj56.graphClass_= graph_RHS
    if self.genGraphics:
       new_obj = graph_RHS(940.0,140.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=LHS(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # constraint
    self.obj57.constraint.setValue('return True\n')
    self.obj57.constraint.setHeight(15)

    self.obj57.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(500.0,140.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    # Connections for obj49 (graphObject_: Obj0) of type MT_pre__Station_S
    self.drawConnections(
(self.obj49,self.obj66,[621.0, 261.0, 721.0, 261.0],"true", 2) )
    # Connections for obj50 (graphObject_: Obj1) of type MT_pre__Female_S
    self.drawConnections(
 )
    # Connections for obj51 (graphObject_: Obj2) of type MT_pre__Station_T
    self.drawConnections(
(self.obj51,self.obj54,[621.0, 441.0, 621.0, 351.0],"true", 2) )
    # Connections for obj52 (graphObject_: Obj3) of type MT_pre__Female_T
    self.drawConnections(
(self.obj52,self.obj55,[821.0, 441.0, 821.0, 351.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj17) of type MT_pre__indirectLink_S
    self.drawConnections(
(self.obj66,self.obj50,[721.0, 261.0, 821.0, 261.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj5) of type MT_pre__trace_link
    self.drawConnections(
(self.obj54,self.obj49,[621.0, 351.0, 621.0, 261.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj6) of type MT_pre__trace_link
    self.drawConnections(
(self.obj55,self.obj50,[821.0, 351.0, 821.0, 261.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj9) of type MT_post__trace_link
    self.drawConnections(
(self.obj58,self.obj64,[1143.0, 348.0, 1143.0, 260.0],"true", 2) )
    # Connections for obj59 (graphObject_: Obj10) of type MT_post__trace_link
    self.drawConnections(
(self.obj59,self.obj63,[1341.0, 351.0, 1341.0, 261.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj12) of type MT_post__directLink_T
    self.drawConnections(
(self.obj61,self.obj62,[1242.0, 438.5, 1341.0, 441.0],"true", 2) )
    # Connections for obj67 (graphObject_: Obj18) of type MT_post__indirectLink_S
    self.drawConnections(
(self.obj67,self.obj63,[1242.0, 260.5, 1341.0, 261.0],"true", 2) )
    # Connections for obj62 (graphObject_: Obj13) of type MT_post__Female_T
    self.drawConnections(
(self.obj62,self.obj59,[1341.0, 441.0, 1341.0, 351.0],"true", 2) )
    # Connections for obj63 (graphObject_: Obj14) of type MT_post__Female_S
    self.drawConnections(
 )
    # Connections for obj64 (graphObject_: Obj15) of type MT_post__Station_S
    self.drawConnections(
(self.obj64,self.obj67,[1143.0, 260.0, 1242.0, 260.5],"true", 2) )
    # Connections for obj65 (graphObject_: Obj16) of type MT_post__Station_T
    self.drawConnections(
(self.obj65,self.obj61,[1143.0, 436.0, 1242.0, 438.5],"true", 2),
(self.obj65,self.obj58,[1143.0, 436.0, 1143.0, 348.0],"true", 2) )
    # Connections for obj56 (graphObject_: Obj7) of type RHS
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj8) of type LHS
    self.drawConnections(
 )

newfunction = SF2SF_combine_1_MDL

loadedMMName = ['MT_pre__PoliceStationMM_META', 'MoTifRule_META', 'MT_post__PoliceStationMM_META']

atom3version = '0.3'
