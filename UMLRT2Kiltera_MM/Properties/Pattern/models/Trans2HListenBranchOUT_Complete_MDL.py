"""
__Trans2HListenBranchOUT_Complete_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: gehan
Modified: Mon Mar  9 12:45:57 2015
_____________________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from MT_pre__Trigger_S import *
from MT_pre__Signal import *
from MT_pre__Transition import *
from MT_pre__OUT2 import *
from MT_pre__Name import *
from MT_pre__ListenBranch import *
from MT_pre__Inst import *
from MT_pre__directLink_T import *
from MT_pre__directLink_S import *
from MT_pre__trace_link import *
from LHS import *
from graph_MT_pre__Trigger_S import *
from graph_MT_pre__Signal import *
from graph_LHS import *
from graph_MT_pre__trace_link import *
from graph_MT_pre__Name import *
from graph_MT_pre__Transition import *
from graph_MT_pre__ListenBranch import *
from graph_MT_pre__directLink_S import *
from graph_MT_pre__directLink_T import *
from graph_MT_pre__OUT2 import *
from graph_MT_pre__Inst import *
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

def Trans2HListenBranchOUT_Complete_MDL(self, rootNode, MoTifRuleRootNode=None, MT_pre__UMLRT2Kiltera_MMRootNode=None):

    # --- Generating attributes code for ASG MoTifRule ---
    if( MoTifRuleRootNode ): 
        # author
        MoTifRuleRootNode.author.setValue('Annonymous')

        # description
        MoTifRuleRootNode.description.setValue('\n')
        MoTifRuleRootNode.description.setHeight(15)

        # name
        MoTifRuleRootNode.name.setValue('Trans2HListenBranchOUT_Complete')
    # --- ASG attributes over ---


    # --- Generating attributes code for ASG MT_pre__UMLRT2Kiltera_MM ---
    if( MT_pre__UMLRT2Kiltera_MMRootNode ): 
        # author
        MT_pre__UMLRT2Kiltera_MMRootNode.author.setValue('Annonymous')

        # description
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setValue('\n')
        MT_pre__UMLRT2Kiltera_MMRootNode.description.setHeight(15)

        # name
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setValue('')
        MT_pre__UMLRT2Kiltera_MMRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj139=MT_pre__Trigger_S(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    # MT_label__
    self.obj139.MT_label__.setValue('3')

    # MT_pivotOut__
    self.obj139.MT_pivotOut__.setValue('element3')

    # MT_subtypeMatching__
    self.obj139.MT_subtypeMatching__.setValue(('True', 0))
    self.obj139.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj139.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj139.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj139.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj139.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj139.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj139.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj139.MT_pivotIn__.setValue('element3')

    self.obj139.graphClass_= graph_MT_pre__Trigger_S
    if self.genGraphics:
       new_obj = graph_MT_pre__Trigger_S(220.0,40.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Trigger_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj126=MT_pre__Signal(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # MT_label__
    self.obj126.MT_label__.setValue('4')

    # MT_pivotOut__
    self.obj126.MT_pivotOut__.setValue('element4')

    # MT_subtypeMatching__
    self.obj126.MT_subtypeMatching__.setValue(('True', 0))
    self.obj126.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj126.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj126.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj126.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj126.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj126.MT_pivotIn__.setValue('element4')

    self.obj126.graphClass_= graph_MT_pre__Signal
    if self.genGraphics:
       new_obj = graph_MT_pre__Signal(265.0,121.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Signal", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj137=MT_pre__Transition(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj137.MT_pivotOut__.setValue('element1')

    # MT_subtypeMatching__
    self.obj137.MT_subtypeMatching__.setValue(('True', 0))
    self.obj137.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj137.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj137.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj137.MT_pivotIn__.setValue('element1')

    # MT_label__
    self.obj137.MT_label__.setValue('1')

    # MT_pre__cardinality
    self.obj137.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj137.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj137.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj137.MT_pre__name.setHeight(15)

    self.obj137.graphClass_= graph_MT_pre__Transition
    if self.genGraphics:
       new_obj = graph_MT_pre__Transition(35.0,34.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Transition", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj125=MT_pre__OUT2(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # MT_label__
    self.obj125.MT_label__.setValue('33')

    # MT_pivotOut__
    self.obj125.MT_pivotOut__.setValue('element2')

    # MT_subtypeMatching__
    self.obj125.MT_subtypeMatching__.setValue(('True', 0))
    self.obj125.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj125.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj125.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj125.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj125.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj125.MT_pivotIn__.setValue('element2')

    self.obj125.graphClass_= graph_MT_pre__OUT2
    if self.genGraphics:
       new_obj = graph_MT_pre__OUT2(40.0,160.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__OUT2", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj121=MT_pre__Name(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj121.MT_pivotOut__.setValue('')
    self.obj121.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj121.MT_subtypeMatching__.setValue(('True', 0))
    self.obj121.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj121.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj121.MT_pivotIn__.setValue('')
    self.obj121.MT_pivotIn__.setNone()

    # MT_label__
    self.obj121.MT_label__.setValue('25')

    # MT_pre__cardinality
    self.obj121.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj121.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj121.MT_pre__name.setHeight(15)

    self.obj121.graphClass_= graph_MT_pre__Name
    if self.genGraphics:
       new_obj = graph_MT_pre__Name(38.0,120.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Name", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj138=MT_pre__ListenBranch(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # MT_pivotOut__
    self.obj138.MT_pivotOut__.setValue('')
    self.obj138.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj138.MT_subtypeMatching__.setValue(('True', 0))
    self.obj138.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj138.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj138.MT_pre__classtype.setHeight(15)

    # MT_pivotIn__
    self.obj138.MT_pivotIn__.setValue('')
    self.obj138.MT_pivotIn__.setNone()

    # MT_label__
    self.obj138.MT_label__.setValue('23')

    # MT_pre__cardinality
    self.obj138.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj138.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj138.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj138.MT_pre__name.setHeight(15)

    self.obj138.graphClass_= graph_MT_pre__ListenBranch
    if self.genGraphics:
       new_obj = graph_MT_pre__ListenBranch(40.0,220.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__ListenBranch", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj131=MT_pre__Inst(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # MT_label__
    self.obj131.MT_label__.setValue('11')

    # MT_pivotOut__
    self.obj131.MT_pivotOut__.setValue('')
    self.obj131.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj131.MT_subtypeMatching__.setValue(('True', 0))
    self.obj131.MT_subtypeMatching__.config = 0

    # MT_pre__classtype
    self.obj131.MT_pre__classtype.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj131.MT_pre__classtype.setHeight(15)

    # MT_pre__cardinality
    self.obj131.MT_pre__cardinality.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj131.MT_pre__cardinality.setHeight(15)

    # MT_pre__name
    self.obj131.MT_pre__name.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj131.MT_pre__name.setHeight(15)

    # MT_pivotIn__
    self.obj131.MT_pivotIn__.setValue('')
    self.obj131.MT_pivotIn__.setNone()

    self.obj131.graphClass_= graph_MT_pre__Inst
    if self.genGraphics:
       new_obj = graph_MT_pre__Inst(225.0,200.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__Inst", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=MT_pre__directLink_T(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # MT_label__
    self.obj132.MT_label__.setValue('24')

    # MT_pivotOut__
    self.obj132.MT_pivotOut__.setValue('')
    self.obj132.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj132.MT_subtypeMatching__.setValue(('True', 0))
    self.obj132.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj132.MT_pivotIn__.setValue('')
    self.obj132.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj132.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj132.MT_pre__associationType.setHeight(15)

    self.obj132.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(354.5,301.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=MT_pre__directLink_T(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # MT_label__
    self.obj133.MT_label__.setValue('26')

    # MT_pivotOut__
    self.obj133.MT_pivotOut__.setValue('')
    self.obj133.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj133.MT_subtypeMatching__.setValue(('True', 0))
    self.obj133.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj133.MT_pivotIn__.setValue('')
    self.obj133.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj133.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj133.MT_pre__associationType.setHeight(15)

    self.obj133.graphClass_= graph_MT_pre__directLink_T
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_T(353.5,261.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj128=MT_pre__directLink_S(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # MT_label__
    self.obj128.MT_label__.setValue('6')

    # MT_pivotOut__
    self.obj128.MT_pivotOut__.setValue('')
    self.obj128.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj128.MT_subtypeMatching__.setValue(('True', 0))
    self.obj128.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj128.MT_pivotIn__.setValue('')
    self.obj128.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj128.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj128.MT_pre__associationType.setHeight(15)

    self.obj128.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(327.0,135.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=MT_pre__directLink_S(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # MT_label__
    self.obj129.MT_label__.setValue('7')

    # MT_pivotOut__
    self.obj129.MT_pivotOut__.setValue('')
    self.obj129.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj129.MT_subtypeMatching__.setValue(('True', 0))
    self.obj129.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj129.MT_pivotIn__.setValue('')
    self.obj129.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj129.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj129.MT_pre__associationType.setHeight(15)

    self.obj129.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(427.0,215.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=MT_pre__directLink_S(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # MT_label__
    self.obj130.MT_label__.setValue('34')

    # MT_pivotOut__
    self.obj130.MT_pivotOut__.setValue('')
    self.obj130.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj130.MT_subtypeMatching__.setValue(('True', 0))
    self.obj130.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj130.MT_pivotIn__.setValue('')
    self.obj130.MT_pivotIn__.setNone()

    # MT_pre__associationType
    self.obj130.MT_pre__associationType.setValue('\n#===============================================================================\n# This code is executed when evaluating if a node shall be matched by this rule.\n# You can access the value of the current node\'s attribute value by: attr_value.\n# You can access any attribute x of this node by: this[\'x\'].\n# If the constraint relies on attribute values from other nodes,\n# use the LHS/NAC constraint instead.\n# The given constraint must evaluate to a boolean expression.\n#===============================================================================\n\nreturn True\n')
    self.obj130.MT_pre__associationType.setHeight(15)

    self.obj130.graphClass_= graph_MT_pre__directLink_S
    if self.genGraphics:
       new_obj = graph_MT_pre__directLink_S(237.0,172.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj127=MT_pre__trace_link(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # MT_label__
    self.obj127.MT_label__.setValue('13')

    # MT_pivotOut__
    self.obj127.MT_pivotOut__.setValue('')
    self.obj127.MT_pivotOut__.setNone()

    # MT_subtypeMatching__
    self.obj127.MT_subtypeMatching__.setValue(('True', 0))
    self.obj127.MT_subtypeMatching__.config = 0

    # MT_pivotIn__
    self.obj127.MT_pivotIn__.setValue('')
    self.obj127.MT_pivotIn__.setNone()

    self.obj127.graphClass_= graph_MT_pre__trace_link
    if self.genGraphics:
       new_obj = graph_MT_pre__trace_link(339.5,205.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj120=LHS(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # constraint
    self.obj120.constraint.setValue('#===============================================================================\n# This code is executed after the nodes in the LHS have been matched.\n# You can access a matched node labelled n by: PreNode(\'n\').\n# To access attribute x of node n, use: PreNode(\'n\')[\'x\'].\n# The given constraint must evaluate to a boolean expression:\n#    returning True enables the rule to be applied,\n#    returning False forbids the rule from being applied.\n#===============================================================================\n\nreturn True\n')
    self.obj120.constraint.setHeight(15)

    self.obj120.graphClass_= graph_LHS
    if self.genGraphics:
       new_obj = graph_LHS(20.0,20.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LHS", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    # Connections for obj139 (graphObject_: Obj19) of type MT_pre__Trigger_S
    self.drawConnections(
(self.obj139,self.obj129,[417.0, 115.0, 427.0, 215.0],"true", 2) )
    # Connections for obj126 (graphObject_: Obj6) of type MT_pre__Signal
    self.drawConnections(
 )
    # Connections for obj137 (graphObject_: Obj17) of type MT_pre__Transition
    self.drawConnections(
(self.obj137,self.obj128,[232.0, 109.0, 327.0, 135.0],"true", 2),
(self.obj137,self.obj130,[232.0, 109.0, 237.0, 172.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj5) of type MT_pre__OUT2
    self.drawConnections(
 )
    # Connections for obj121 (graphObject_: Obj1) of type MT_pre__Name
    self.drawConnections(
 )
    # Connections for obj138 (graphObject_: Obj18) of type MT_pre__ListenBranch
    self.drawConnections(
(self.obj138,self.obj132,[262.0, 321.0, 354.5, 301.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj11) of type MT_pre__Inst
    self.drawConnections(
(self.obj131,self.obj127,[447.0, 301.0, 339.5, 205.0],"true", 2),
(self.obj131,self.obj133,[447.0, 301.0, 353.5, 261.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj12) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj132,self.obj131,[354.5, 301.0, 447.0, 301.0],"true", 2) )
    # Connections for obj133 (graphObject_: Obj13) of type MT_pre__directLink_T
    self.drawConnections(
(self.obj133,self.obj121,[353.5, 261.0, 260.0, 221.0],"true", 2) )
    # Connections for obj128 (graphObject_: Obj8) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj128,self.obj139,[327.0, 135.0, 417.0, 115.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj9) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj129,self.obj126,[427.0, 215.0, 462.0, 196.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj10) of type MT_pre__directLink_S
    self.drawConnections(
(self.obj130,self.obj125,[237.0, 172.0, 242.0, 235.0],"true", 2) )
    # Connections for obj127 (graphObject_: Obj7) of type MT_pre__trace_link
    self.drawConnections(
(self.obj127,self.obj137,[339.5, 205.0, 232.0, 109.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj0) of type LHS
    self.drawConnections(
 )

newfunction = Trans2HListenBranchOUT_Complete_MDL

loadedMMName = ['MoTifRule_META', 'MT_pre__UMLRT2Kiltera_MM_META']

atom3version = '0.3'
