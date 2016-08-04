from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True

                super(HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS, self).__init__(name='HGlobalVarGetsCorrectFunctionAddressAtInit_CompleteLHS', num_nodes=0, edges=[])

                # Set the graph attributes
                self["mm__"] = []

                self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
                self["name"] = """"""
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'GlobalVarGetsCorrectFunctionAddressAtInit')
        
                # Nodes that represent match classes
                # match class ComponentInstance() node
                self.add_node()
                self.vs[0]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[0]["MT_label__"] = """1"""
                self.vs[0]["MT_dirty__"] = False
                self.vs[0]["mm__"] = """MT_pre__ComponentInstance"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Operation() node
                self.add_node()
                self.vs[1]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[1]["MT_label__"] = """2"""
                self.vs[1]["MT_dirty__"] = False
                self.vs[1]["mm__"] = """MT_pre__Operation"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class OperationTrigger() node
                self.add_node()
                self.vs[2]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[2]["MT_label__"] = """3"""
                self.vs[2]["MT_dirty__"] = False
                self.vs[2]["mm__"] = """MT_pre__OperationTrigger"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Executable() node
                self.add_node()
                self.vs[3]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[3]["MT_label__"] = """4"""
                self.vs[3]["MT_dirty__"] = False
                self.vs[3]["mm__"] = """MT_pre__Executable"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ProvidedPort() node
                self.add_node()
                self.vs[4]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[4]["MT_label__"] = """5"""
                self.vs[4]["MT_dirty__"] = False
                self.vs[4]["mm__"] = """MT_pre__ProvidedPort"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class InstanceConfiguration() node
                self.add_node()
                self.vs[5]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[5]["MT_label__"] = """6"""
                self.vs[5]["MT_dirty__"] = False
                self.vs[5]["mm__"] = """MT_pre__InstanceConfiguration"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ClientServerInterface() node
                self.add_node()
                self.vs[6]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[6]["MT_label__"] = """7"""
                self.vs[6]["MT_dirty__"] = False
                self.vs[6]["mm__"] = """MT_pre__ClientServerInterface"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class AtomicComponent() node
                self.add_node()
                self.vs[7]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[7]["MT_label__"] = """8"""
                self.vs[7]["MT_dirty__"] = False
                self.vs[7]["mm__"] = """MT_pre__AtomicComponent"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        #Nodes that represent apply classes
        # match class StatementList() node
                self.add_node()
                self.vs[8]["MT_subtypeMatching__"] = False
                self.vs[8]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[8]["MT_label__"] = """9"""
                self.vs[8]["MT_subtypes__"] = []
                self.vs[8]["MT_dirty__"] = False
                self.vs[8]["mm__"] = """MT_pre__StatementList"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionCall() node
                self.add_node()
                self.vs[9]["MT_subtypeMatching__"] = False
                self.vs[9]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[9]["MT_label__"] = """10"""
                self.vs[9]["MT_subtypes__"] = []
                self.vs[9]["MT_dirty__"] = False
                self.vs[9]["mm__"] = """MT_pre__FunctionCall"""
                self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GenericMemberRef() node
                self.add_node()
                self.vs[10]["MT_subtypeMatching__"] = False
                self.vs[10]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[10]["MT_label__"] = """11"""
                self.vs[10]["MT_subtypes__"] = []
                self.vs[10]["MT_dirty__"] = False
                self.vs[10]["mm__"] = """MT_pre__GenericMemberRef"""
                self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class AssignmentExpr() node
                self.add_node()
                self.vs[11]["MT_subtypeMatching__"] = False
                self.vs[11]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[11]["MT_label__"] = """12"""
                self.vs[11]["MT_subtypes__"] = []
                self.vs[11]["MT_dirty__"] = False
                self.vs[11]["mm__"] = """MT_pre__AssignmentExpr"""
                self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ExpressionStatement() node
                self.add_node()
                self.vs[12]["MT_subtypeMatching__"] = False
                self.vs[12]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[12]["MT_label__"] = """13"""
                self.vs[12]["MT_subtypes__"] = []
                self.vs[12]["MT_dirty__"] = False
                self.vs[12]["mm__"] = """MT_pre__ExpressionStatement"""
                self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StatementList() node
                self.add_node()
                self.vs[13]["MT_subtypeMatching__"] = False
                self.vs[13]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[13]["MT_label__"] = """14"""
                self.vs[13]["MT_subtypes__"] = []
                self.vs[13]["MT_dirty__"] = False
                self.vs[13]["mm__"] = """MT_pre__StatementList"""
                self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionPrototype() node
                self.add_node()
                self.vs[14]["MT_subtypeMatching__"] = False
                self.vs[14]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[14]["MT_label__"] = """15"""
                self.vs[14]["MT_subtypes__"] = []
                self.vs[14]["MT_dirty__"] = False
                self.vs[14]["mm__"] = """MT_pre__FunctionPrototype"""
                self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ExpressionStatement() node
                self.add_node()
                self.vs[15]["MT_subtypeMatching__"] = False
                self.vs[15]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[15]["MT_label__"] = """16"""
                self.vs[15]["MT_subtypes__"] = []
                self.vs[15]["MT_dirty__"] = False
                self.vs[15]["mm__"] = """MT_pre__ExpressionStatement"""
                self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Function() node
                self.add_node()
                self.vs[16]["MT_subtypeMatching__"] = False
                self.vs[16]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[16]["MT_label__"] = """17"""
                self.vs[16]["MT_subtypes__"] = []
                self.vs[16]["MT_dirty__"] = False
                self.vs[16]["mm__"] = """MT_pre__Function"""
                self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionRefExpr() node
                self.add_node()
                self.vs[17]["MT_subtypeMatching__"] = False
                self.vs[17]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[17]["MT_label__"] = """18"""
                self.vs[17]["MT_subtypes__"] = []
                self.vs[17]["MT_dirty__"] = False
                self.vs[17]["mm__"] = """MT_pre__FunctionRefExpr"""
                self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GlobalVarRef() node
                self.add_node()
                self.vs[18]["MT_subtypeMatching__"] = False
                self.vs[18]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[18]["MT_label__"] = """19"""
                self.vs[18]["MT_subtypes__"] = []
                self.vs[18]["MT_dirty__"] = False
                self.vs[18]["mm__"] = """MT_pre__GlobalVarRef"""
                self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ReferenceExpr() node
                self.add_node()
                self.vs[19]["MT_subtypeMatching__"] = False
                self.vs[19]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[19]["MT_label__"] = """20"""
                self.vs[19]["MT_subtypes__"] = []
                self.vs[19]["MT_dirty__"] = False
                self.vs[19]["mm__"] = """MT_pre__ReferenceExpr"""
                self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GenericDotExpression() node
                self.add_node()
                self.vs[20]["MT_subtypeMatching__"] = False
                self.vs[20]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[20]["MT_label__"] = """21"""
                self.vs[20]["MT_subtypes__"] = []
                self.vs[20]["MT_dirty__"] = False
                self.vs[20]["mm__"] = """MT_pre__GenericDotExpression"""
                self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Function() node
                self.add_node()
                self.vs[21]["MT_subtypeMatching__"] = False
                self.vs[21]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[21]["MT_label__"] = """22"""
                self.vs[21]["MT_subtypes__"] = []
                self.vs[21]["MT_dirty__"] = False
                self.vs[21]["mm__"] = """MT_pre__Function"""
                self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionPrototype() node
                self.add_node()
                self.vs[22]["MT_subtypeMatching__"] = False
                self.vs[22]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[22]["MT_label__"] = """23"""
                self.vs[22]["MT_subtypes__"] = []
                self.vs[22]["MT_dirty__"] = False
                self.vs[22]["mm__"] = """MT_pre__FunctionPrototype"""
                self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GlobalVariableDeclaration() node
                self.add_node()
                self.vs[23]["MT_subtypeMatching__"] = False
                self.vs[23]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[23]["MT_label__"] = """24"""
                self.vs[23]["MT_subtypes__"] = []
                self.vs[23]["MT_dirty__"] = False
                self.vs[23]["mm__"] = """MT_pre__GlobalVariableDeclaration"""
                self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StructDeclaration() node
                self.add_node()
                self.vs[24]["MT_subtypeMatching__"] = False
                self.vs[24]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[24]["MT_label__"] = """25"""
                self.vs[24]["MT_subtypes__"] = []
                self.vs[24]["MT_dirty__"] = False
                self.vs[24]["mm__"] = """MT_pre__StructDeclaration"""
                self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class CFunctionPointerStructMember() node
                self.add_node()
                self.vs[25]["MT_subtypeMatching__"] = False
                self.vs[25]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[25]["MT_label__"] = """26"""
                self.vs[25]["MT_subtypes__"] = []
                self.vs[25]["MT_dirty__"] = False
                self.vs[25]["mm__"] = """MT_pre__CFunctionPointerStructMember"""
                self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
                
        # Nodes that represent the match associations of the property.
        # match association InstanceConfiguration--contents-->ComponentInstance node
                self.add_node()
                self.vs[26]["MT_subtypeMatching__"] = False
                self.vs[26]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "contents"
"""
                self.vs[26]["MT_label__"] = """27"""
                self.vs[26]["MT_subtypes__"] = []
                self.vs[26]["MT_dirty__"] = False
                self.vs[26]["mm__"] = """MT_pre__directLink_S"""
                self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc26')
        # match association AtomicComponent--contents-->ProvidedPort node
                self.add_node()
                self.vs[27]["MT_subtypeMatching__"] = False
                self.vs[27]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "contents"
"""
                self.vs[27]["MT_label__"] = """28"""
                self.vs[27]["MT_subtypes__"] = []
                self.vs[27]["MT_dirty__"] = False
                self.vs[27]["mm__"] = """MT_pre__directLink_S"""
                self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc27')
        # match association ComponentInstance--component-->AtomicComponent node
                self.add_node()
                self.vs[28]["MT_subtypeMatching__"] = False
                self.vs[28]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "component"
"""
                self.vs[28]["MT_label__"] = """29"""
                self.vs[28]["MT_subtypes__"] = []
                self.vs[28]["MT_dirty__"] = False
                self.vs[28]["mm__"] = """MT_pre__directLink_S"""
                self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc28')
        # match association AtomicComponent--contents-->Executable node
                self.add_node()
                self.vs[29]["MT_subtypeMatching__"] = False
                self.vs[29]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "contents"
"""
                self.vs[29]["MT_label__"] = """30"""
                self.vs[29]["MT_subtypes__"] = []
                self.vs[29]["MT_dirty__"] = False
                self.vs[29]["mm__"] = """MT_pre__directLink_S"""
                self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc29')
        # match association Executable--trigger-->OperationTrigger node
                self.add_node()
                self.vs[30]["MT_subtypeMatching__"] = False
                self.vs[30]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "trigger"
"""
                self.vs[30]["MT_label__"] = """31"""
                self.vs[30]["MT_subtypes__"] = []
                self.vs[30]["MT_dirty__"] = False
                self.vs[30]["mm__"] = """MT_pre__directLink_S"""
                self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc30')
        # match association OperationTrigger--calledOperation-->Operation node
                self.add_node()
                self.vs[31]["MT_subtypeMatching__"] = False
                self.vs[31]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "calledOperation"
"""
                self.vs[31]["MT_label__"] = """32"""
                self.vs[31]["MT_subtypes__"] = []
                self.vs[31]["MT_dirty__"] = False
                self.vs[31]["mm__"] = """MT_pre__directLink_S"""
                self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc31')
        # match association ProvidedPort--intf-->ClientServerInterface node
                self.add_node()
                self.vs[32]["MT_subtypeMatching__"] = False
                self.vs[32]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "intf"
"""
                self.vs[32]["MT_label__"] = """33"""
                self.vs[32]["MT_subtypes__"] = []
                self.vs[32]["MT_dirty__"] = False
                self.vs[32]["mm__"] = """MT_pre__directLink_S"""
                self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc32')
        # match association ClientServerInterface--contents-->Operation node
                self.add_node()
                self.vs[33]["MT_subtypeMatching__"] = False
                self.vs[33]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "contents"
"""
                self.vs[33]["MT_label__"] = """34"""
                self.vs[33]["MT_subtypes__"] = []
                self.vs[33]["MT_dirty__"] = False
                self.vs[33]["mm__"] = """MT_pre__directLink_S"""
                self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc33')
        # match association OperationTrigger--providedPort-->ProvidedPort node
                self.add_node()
                self.vs[34]["MT_subtypeMatching__"] = False
                self.vs[34]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "providedPort"
"""
                self.vs[34]["MT_label__"] = """35"""
                self.vs[34]["MT_subtypes__"] = []
                self.vs[34]["MT_dirty__"] = False
                self.vs[34]["mm__"] = """MT_pre__directLink_S"""
                self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc34')
        
        
        # Nodes that represent the apply associations of the property.
        # apply association FunctionCall--function-->FunctionPrototype node
                self.add_node()
                self.vs[35]["MT_subtypeMatching__"] = False
                self.vs[35]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "function"
"""
                self.vs[35]["MT_label__"] = """36"""
                self.vs[35]["MT_subtypes__"] = []
                self.vs[35]["MT_dirty__"] = False
                self.vs[35]["mm__"] = """MT_pre__directLink_T"""
                self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc35')
        # apply association Function--body-->StatementList node
                self.add_node()
                self.vs[36]["MT_subtypeMatching__"] = False
                self.vs[36]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "body"
"""
                self.vs[36]["MT_label__"] = """37"""
                self.vs[36]["MT_subtypes__"] = []
                self.vs[36]["MT_dirty__"] = False
                self.vs[36]["mm__"] = """MT_pre__directLink_T"""
                self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc36')
        # apply association StatementList--statements-->ExpressionStatement node
                self.add_node()
                self.vs[37]["MT_subtypeMatching__"] = False
                self.vs[37]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "statements"
"""
                self.vs[37]["MT_label__"] = """38"""
                self.vs[37]["MT_subtypes__"] = []
                self.vs[37]["MT_dirty__"] = False
                self.vs[37]["mm__"] = """MT_pre__directLink_T"""
                self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc37')
        # apply association ExpressionStatement--expr-->FunctionCall node
                self.add_node()
                self.vs[38]["MT_subtypeMatching__"] = False
                self.vs[38]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "expr"
"""
                self.vs[38]["MT_label__"] = """39"""
                self.vs[38]["MT_subtypes__"] = []
                self.vs[38]["MT_dirty__"] = False
                self.vs[38]["mm__"] = """MT_pre__directLink_T"""
                self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc38')
        # apply association Function--body-->StatementList node
                self.add_node()
                self.vs[39]["MT_subtypeMatching__"] = False
                self.vs[39]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "body"
"""
                self.vs[39]["MT_label__"] = """40"""
                self.vs[39]["MT_subtypes__"] = []
                self.vs[39]["MT_dirty__"] = False
                self.vs[39]["mm__"] = """MT_pre__directLink_T"""
                self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc39')
        # apply association StatementList--statements-->ExpressionStatement node
                self.add_node()
                self.vs[40]["MT_subtypeMatching__"] = False
                self.vs[40]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "statements"
"""
                self.vs[40]["MT_label__"] = """41"""
                self.vs[40]["MT_subtypes__"] = []
                self.vs[40]["MT_dirty__"] = False
                self.vs[40]["mm__"] = """MT_pre__directLink_T"""
                self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc40')
        # apply association ExpressionStatement--expr-->AssignmentExpr node
                self.add_node()
                self.vs[41]["MT_subtypeMatching__"] = False
                self.vs[41]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "expr"
"""
                self.vs[41]["MT_label__"] = """42"""
                self.vs[41]["MT_subtypes__"] = []
                self.vs[41]["MT_dirty__"] = False
                self.vs[41]["mm__"] = """MT_pre__directLink_T"""
                self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc41')
        # apply association AssignmentExpr--left-->GenericDotExpression node
                self.add_node()
                self.vs[42]["MT_subtypeMatching__"] = False
                self.vs[42]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "left"
"""
                self.vs[42]["MT_label__"] = """43"""
                self.vs[42]["MT_subtypes__"] = []
                self.vs[42]["MT_dirty__"] = False
                self.vs[42]["mm__"] = """MT_pre__directLink_T"""
                self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc42')
        # apply association AssignmentExpr--right-->ReferenceExpr node
                self.add_node()
                self.vs[43]["MT_subtypeMatching__"] = False
                self.vs[43]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "right"
"""
                self.vs[43]["MT_label__"] = """44"""
                self.vs[43]["MT_subtypes__"] = []
                self.vs[43]["MT_dirty__"] = False
                self.vs[43]["mm__"] = """MT_pre__directLink_T"""
                self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc43')
        # apply association GenericDotExpression--expression-->GlobalVarRef node
                self.add_node()
                self.vs[44]["MT_subtypeMatching__"] = False
                self.vs[44]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "expression"
"""
                self.vs[44]["MT_label__"] = """45"""
                self.vs[44]["MT_subtypes__"] = []
                self.vs[44]["MT_dirty__"] = False
                self.vs[44]["mm__"] = """MT_pre__directLink_T"""
                self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc44')
        # apply association GenericDotExpression--target-->GenericMemberRef node
                self.add_node()
                self.vs[45]["MT_subtypeMatching__"] = False
                self.vs[45]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "target"
"""
                self.vs[45]["MT_label__"] = """46"""
                self.vs[45]["MT_subtypes__"] = []
                self.vs[45]["MT_dirty__"] = False
                self.vs[45]["mm__"] = """MT_pre__directLink_T"""
                self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc45')
        # apply association ReferenceExpr--expression-->FunctionRefExpr node
                self.add_node()
                self.vs[46]["MT_subtypeMatching__"] = False
                self.vs[46]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "expression"
"""
                self.vs[46]["MT_label__"] = """47"""
                self.vs[46]["MT_subtypes__"] = []
                self.vs[46]["MT_dirty__"] = False
                self.vs[46]["mm__"] = """MT_pre__directLink_T"""
                self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc46')
        # apply association FunctionRefExpr--function-->FunctionPrototype node
                self.add_node()
                self.vs[47]["MT_subtypeMatching__"] = False
                self.vs[47]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "function"
"""
                self.vs[47]["MT_label__"] = """48"""
                self.vs[47]["MT_subtypes__"] = []
                self.vs[47]["MT_dirty__"] = False
                self.vs[47]["mm__"] = """MT_pre__directLink_T"""
                self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc47')
        # apply association StructDeclaration--members-->CFunctionPointerStructMember node
                self.add_node()
                self.vs[48]["MT_subtypeMatching__"] = False
                self.vs[48]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "members"
"""
                self.vs[48]["MT_label__"] = """49"""
                self.vs[48]["MT_subtypes__"] = []
                self.vs[48]["MT_dirty__"] = False
                self.vs[48]["mm__"] = """MT_pre__directLink_T"""
                self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc48')
        # apply association GenericMemberRef--member-->CFunctionPointerStructMember node
                self.add_node()
                self.vs[49]["MT_subtypeMatching__"] = False
                self.vs[49]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "member"
"""
                self.vs[49]["MT_label__"] = """50"""
                self.vs[49]["MT_subtypes__"] = []
                self.vs[49]["MT_dirty__"] = False
                self.vs[49]["mm__"] = """MT_pre__directLink_T"""
                self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc49')
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
                self.add_node()
                self.vs[50]["MT_subtypeMatching__"] = False
                self.vs[50]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "var"
"""
                self.vs[50]["MT_label__"] = """51"""
                self.vs[50]["MT_subtypes__"] = []
                self.vs[50]["MT_dirty__"] = False
                self.vs[50]["mm__"] = """MT_pre__directLink_T"""
                self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc50')
        
                # Nodes that represent trace relations
                # backward association InstanceConfiguration---->Function node
                self.add_node()
                self.vs[51]["MT_subtypeMatching__"] = False
                self.vs[51]["MT_label__"] = """52"""
                self.vs[51]["MT_subtypes__"] = []
                self.vs[51]["MT_dirty__"] = False
                self.vs[51]["mm__"] = """MT_pre__trace_link"""
                self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink51')
                # backward association ComponentInstance---->FunctionPrototype node
                self.add_node()
                self.vs[52]["MT_subtypeMatching__"] = False
                self.vs[52]["MT_label__"] = """53"""
                self.vs[52]["MT_subtypes__"] = []
                self.vs[52]["MT_dirty__"] = False
                self.vs[52]["mm__"] = """MT_pre__trace_link"""
                self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink52')
                # backward association ComponentInstance---->Function node
                self.add_node()
                self.vs[53]["MT_subtypeMatching__"] = False
                self.vs[53]["MT_label__"] = """54"""
                self.vs[53]["MT_subtypes__"] = []
                self.vs[53]["MT_dirty__"] = False
                self.vs[53]["mm__"] = """MT_pre__trace_link"""
                self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink53')
                # backward association Executable---->FunctionPrototype node
                self.add_node()
                self.vs[54]["MT_subtypeMatching__"] = False
                self.vs[54]["MT_label__"] = """55"""
                self.vs[54]["MT_subtypes__"] = []
                self.vs[54]["MT_dirty__"] = False
                self.vs[54]["mm__"] = """MT_pre__trace_link"""
                self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink54')
                # backward association ComponentInstance---->GlobalVariableDeclaration node
                self.add_node()
                self.vs[55]["MT_subtypeMatching__"] = False
                self.vs[55]["MT_label__"] = """56"""
                self.vs[55]["MT_subtypes__"] = []
                self.vs[55]["MT_dirty__"] = False
                self.vs[55]["mm__"] = """MT_pre__trace_link"""
                self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink55')
                # backward association ClientServerInterface---->StructDeclaration node
                self.add_node()
                self.vs[56]["MT_subtypeMatching__"] = False
                self.vs[56]["MT_label__"] = """57"""
                self.vs[56]["MT_subtypes__"] = []
                self.vs[56]["MT_dirty__"] = False
                self.vs[56]["mm__"] = """MT_pre__trace_link"""
                self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink56')
                # backward association Operation---->CFunctionPointerStructMember node
                self.add_node()
                self.vs[57]["MT_subtypeMatching__"] = False
                self.vs[57]["MT_label__"] = """58"""
                self.vs[57]["MT_subtypes__"] = []
                self.vs[57]["MT_dirty__"] = False
                self.vs[57]["mm__"] = """MT_pre__trace_link"""
                self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink57')


        
        
        
        
        
                # Add the edges
                self.add_edges([
                (16,51), # apply_class Function() -> backward_association
                (51,5), #  backward_association -> apply_class InstanceConfiguration()
                (14,52), # apply_class FunctionPrototype() -> backward_association
                (52,0), #  backward_association -> apply_class ComponentInstance()
                (21,53), # apply_class Function() -> backward_association
                (53,0), #  backward_association -> apply_class ComponentInstance()
                (22,54), # apply_class FunctionPrototype() -> backward_association
                (54,3), #  backward_association -> apply_class Executable()
                (23,55), # apply_class GlobalVariableDeclaration() -> backward_association
                (55,0), #  backward_association -> apply_class ComponentInstance()
                (24,56), # apply_class StructDeclaration() -> backward_association
                (56,6), #  backward_association -> apply_class ClientServerInterface()
                (25,57), # apply_class CFunctionPointerStructMember() -> backward_association
                (57,1), #  backward_association -> apply_class Operation()
                (9,35), # apply_class FunctionCall() -> association function
                (35,14), # association function  -> apply_class FunctionPrototype()
                (16,36), # apply_class Function() -> association body
                (36,13), # association body  -> apply_class StatementList()
                (13,37), # apply_class StatementList() -> association statements
                (37,15), # association statements  -> apply_class ExpressionStatement()
                (15,38), # apply_class ExpressionStatement() -> association expr
                (38,9), # association expr  -> apply_class FunctionCall()
                (21,39), # apply_class Function() -> association body
                (39,8), # association body  -> apply_class StatementList()
                (8,40), # apply_class StatementList() -> association statements
                (40,12), # association statements  -> apply_class ExpressionStatement()
                (12,41), # apply_class ExpressionStatement() -> association expr
                (41,11), # association expr  -> apply_class AssignmentExpr()
                (11,42), # apply_class AssignmentExpr() -> association left
                (42,20), # association left  -> apply_class GenericDotExpression()
                (11,43), # apply_class AssignmentExpr() -> association right
                (43,19), # association right  -> apply_class ReferenceExpr()
                (20,44), # apply_class GenericDotExpression() -> association expression
                (44,18), # association expression  -> apply_class GlobalVarRef()
                (20,45), # apply_class GenericDotExpression() -> association target
                (45,10), # association target  -> apply_class GenericMemberRef()
                (19,46), # apply_class ReferenceExpr() -> association expression
                (46,17), # association expression  -> apply_class FunctionRefExpr()
                (17,47), # apply_class FunctionRefExpr() -> association function
                (47,22), # association function  -> apply_class FunctionPrototype()
                (24,48), # apply_class StructDeclaration() -> association members
                (48,25), # association members  -> apply_class CFunctionPointerStructMember()
                (10,49), # apply_class GenericMemberRef() -> association member
                (49,25), # association member  -> apply_class CFunctionPointerStructMember()
                (18,50), # apply_class GlobalVarRef() -> association var
                (50,23), # association var  -> apply_class GlobalVariableDeclaration()
                (5,26), # match_class InstanceConfiguration() -> association contents
                (26,0), # association contents  -> match_class ComponentInstance()
                (7,27), # match_class AtomicComponent() -> association contents
                (27,4), # association contents  -> match_class ProvidedPort()
                (0,28), # match_class ComponentInstance() -> association component
                (28,7), # association component  -> match_class AtomicComponent()
                (7,29), # match_class AtomicComponent() -> association contents
                (29,3), # association contents  -> match_class Executable()
                (3,30), # match_class Executable() -> association trigger
                (30,2), # association trigger  -> match_class OperationTrigger()
                (2,31), # match_class OperationTrigger() -> association calledOperation
                (31,1), # association calledOperation  -> match_class Operation()
                (4,32), # match_class ProvidedPort() -> association intf
                (32,6), # association intf  -> match_class ClientServerInterface()
                (6,33), # match_class ClientServerInterface() -> association contents
                (33,1), # association contents  -> match_class Operation()
                (2,34), # match_class OperationTrigger() -> association providedPort
                (34,4) # association providedPort  -> match_class ProvidedPort()
                ])
        
                # Add the attribute equations
                self["equations"] = [((14,'name'),('concat',(('wildcard'),('constant','__wire')))), ((16,'name'),('concat',(('wildcard'),('constant','__init')))), ((21,'name'),('concat',(('wildcard'),('constant','__wire')))), ((22,'name'),('concat',(('wildcard'),(3,'name')))), ((23,'name'),('concat',(('wildcard'),('constant','__ops')))), ((24,'name'),('concat',(('wildcard'),('constant','__idata')))), ((25,'name'),(1,'name')), ]
        
        def eval_attr11(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr12(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr13(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr14(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr15(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr16(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr17(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr18(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        
        def eval_attr127(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr128(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr129(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "component"


        def eval_attr130(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr131(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "trigger"


        def eval_attr132(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "calledOperation"


        def eval_attr133(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "intf"


        def eval_attr134(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr135(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "providedPort"


        
        def eval_attr19(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr110(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr111(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr112(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr113(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr114(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr115(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr116(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr117(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr118(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr119(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr120(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr121(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr122(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr123(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr124(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr125(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr126(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr136(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "function"


        def eval_attr137(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr138(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr139(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expr"


        def eval_attr140(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr141(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr142(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expr"


        def eval_attr143(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "left"


        def eval_attr144(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "right"


        def eval_attr145(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expression"


        def eval_attr146(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "target"


        def eval_attr147(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expression"


        def eval_attr148(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "function"


        def eval_attr149(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "members"


        def eval_attr150(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "member"


        def eval_attr151(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "var"


        
        def constraint(self, PreNode, graph):
                """
                Executable constraint code.
                @param PreNode: Function taking an integer as parameter
                                                and returns the node corresponding to that label.
                """
                        #===============================================================================
                        # This code is executed after the nodes in the LHS have been matched.
                        # You can access a matched node labelled n by: PreNode('n').
                        # To access attribute x of node n, use: PreNode('n')['x'].
                        # The given constraint must evaluate to a boolean expression:
                        #    returning True enables the rule to be applied,
                        #    returning False forbids the rule from being applied.
                        #===============================================================================

                return True

