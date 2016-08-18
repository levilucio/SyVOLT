from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HSimple_CompleteLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HSimple_CompleteLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True

                super(HSimple_CompleteLHS, self).__init__(name='HSimple_CompleteLHS', num_nodes=0, edges=[])

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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Simple')
        
                # Nodes that represent match classes
                # match class ImplementationModule() node
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
                self.vs[0]["mm__"] = """MT_pre__ImplementationModule"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Function() node
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
                self.vs[1]["mm__"] = """MT_pre__Function"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ComponentInstance() node
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
                self.vs[2]["mm__"] = """MT_pre__ComponentInstance"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class InstanceConfiguration() node
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
                self.vs[3]["mm__"] = """MT_pre__InstanceConfiguration"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class TestCase() node
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
                self.vs[4]["mm__"] = """MT_pre__TestCase"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class StatementList() node
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
                self.vs[5]["mm__"] = """MT_pre__StatementList"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class InitializeConfiguration() node
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
                self.vs[6]["mm__"] = """MT_pre__InitializeConfiguration"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class StatementList() node
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
                self.vs[7]["mm__"] = """MT_pre__StatementList"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ExecuteTestExpression() node
                self.add_node()
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
                self.vs[8]["MT_dirty__"] = False
                self.vs[8]["mm__"] = """MT_pre__ExecuteTestExpression"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class TestCaseRef() node
                self.add_node()
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
                self.vs[9]["MT_dirty__"] = False
                self.vs[9]["mm__"] = """MT_pre__TestCaseRef"""
                self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ReturnStatement() node
                self.add_node()
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
                self.vs[10]["MT_dirty__"] = False
                self.vs[10]["mm__"] = """MT_pre__ReturnStatement"""
                self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        #Nodes that represent apply classes
        # match class Function() node
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
                self.vs[11]["mm__"] = """MT_pre__Function"""
                self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionPrototype() node
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
                self.vs[12]["mm__"] = """MT_pre__FunctionPrototype"""
                self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ImplementationModule() node
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
                self.vs[13]["mm__"] = """MT_pre__ImplementationModule"""
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
        # match class FunctionPrototype() node
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
                self.vs[15]["mm__"] = """MT_pre__FunctionPrototype"""
                self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StatementList() node
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
                self.vs[16]["mm__"] = """MT_pre__StatementList"""
                self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Function() node
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
                self.vs[17]["mm__"] = """MT_pre__Function"""
                self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ExpressionStatement() node
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
                self.vs[18]["mm__"] = """MT_pre__ExpressionStatement"""
                self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionCall() node
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
                self.vs[19]["mm__"] = """MT_pre__FunctionCall"""
                self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionCall() node
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
                self.vs[20]["mm__"] = """MT_pre__FunctionCall"""
                self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ExpressionStatement() node
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
                self.vs[21]["mm__"] = """MT_pre__ExpressionStatement"""
                self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StatementList() node
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
                self.vs[22]["mm__"] = """MT_pre__StatementList"""
                self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Function() node
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
                self.vs[23]["mm__"] = """MT_pre__Function"""
                self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Function() node
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
                self.vs[24]["mm__"] = """MT_pre__Function"""
                self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ExpressionStatement() node
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
                self.vs[25]["mm__"] = """MT_pre__ExpressionStatement"""
                self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StatementList() node
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

return True
"""
                self.vs[26]["MT_label__"] = """27"""
                self.vs[26]["MT_subtypes__"] = []
                self.vs[26]["MT_dirty__"] = False
                self.vs[26]["mm__"] = """MT_pre__StatementList"""
                self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Function() node
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

return True
"""
                self.vs[27]["MT_label__"] = """28"""
                self.vs[27]["MT_subtypes__"] = []
                self.vs[27]["MT_dirty__"] = False
                self.vs[27]["mm__"] = """MT_pre__Function"""
                self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionCall() node
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

return True
"""
                self.vs[28]["MT_label__"] = """29"""
                self.vs[28]["MT_subtypes__"] = []
                self.vs[28]["MT_dirty__"] = False
                self.vs[28]["mm__"] = """MT_pre__FunctionCall"""
                self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StatementList() node
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

return True
"""
                self.vs[29]["MT_label__"] = """30"""
                self.vs[29]["MT_subtypes__"] = []
                self.vs[29]["MT_dirty__"] = False
                self.vs[29]["mm__"] = """MT_pre__StatementList"""
                self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ExpressionStatement() node
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

return True
"""
                self.vs[30]["MT_label__"] = """31"""
                self.vs[30]["MT_subtypes__"] = []
                self.vs[30]["MT_dirty__"] = False
                self.vs[30]["mm__"] = """MT_pre__ExpressionStatement"""
                self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionCall() node
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

return True
"""
                self.vs[31]["MT_label__"] = """32"""
                self.vs[31]["MT_subtypes__"] = []
                self.vs[31]["MT_dirty__"] = False
                self.vs[31]["mm__"] = """MT_pre__FunctionCall"""
                self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class FunctionPrototype() node
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

return True
"""
                self.vs[32]["MT_label__"] = """33"""
                self.vs[32]["MT_subtypes__"] = []
                self.vs[32]["MT_dirty__"] = False
                self.vs[32]["mm__"] = """MT_pre__FunctionPrototype"""
                self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
                
        # Nodes that represent the match associations of the property.
        # match association InstanceConfiguration--contents-->ComponentInstance node
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
        # match association ImplementationModule--contents-->Function node
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

return attr_value == "contents"
"""
                self.vs[34]["MT_label__"] = """35"""
                self.vs[34]["MT_subtypes__"] = []
                self.vs[34]["MT_dirty__"] = False
                self.vs[34]["mm__"] = """MT_pre__directLink_S"""
                self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc34')
        # match association ImplementationModule--contents-->InstanceConfiguration node
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

return attr_value == "contents"
"""
                self.vs[35]["MT_label__"] = """36"""
                self.vs[35]["MT_subtypes__"] = []
                self.vs[35]["MT_dirty__"] = False
                self.vs[35]["mm__"] = """MT_pre__directLink_S"""
                self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc35')
        # match association ImplementationModule--contents-->TestCase node
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

return attr_value == "contents"
"""
                self.vs[36]["MT_label__"] = """37"""
                self.vs[36]["MT_subtypes__"] = []
                self.vs[36]["MT_dirty__"] = False
                self.vs[36]["mm__"] = """MT_pre__directLink_S"""
                self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc36')
        # match association TestCase--body-->StatementList node
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

return attr_value == "body"
"""
                self.vs[37]["MT_label__"] = """38"""
                self.vs[37]["MT_subtypes__"] = []
                self.vs[37]["MT_dirty__"] = False
                self.vs[37]["mm__"] = """MT_pre__directLink_S"""
                self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc37')
        # match association StatementList--statements-->InitializeConfiguration node
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

return attr_value == "statements"
"""
                self.vs[38]["MT_label__"] = """39"""
                self.vs[38]["MT_subtypes__"] = []
                self.vs[38]["MT_dirty__"] = False
                self.vs[38]["mm__"] = """MT_pre__directLink_S"""
                self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc38')
        # match association InitializeConfiguration--config-->InstanceConfiguration node
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

return attr_value == "config"
"""
                self.vs[39]["MT_label__"] = """40"""
                self.vs[39]["MT_subtypes__"] = []
                self.vs[39]["MT_dirty__"] = False
                self.vs[39]["mm__"] = """MT_pre__directLink_S"""
                self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc39')
        # match association Function--body-->StatementList node
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

return attr_value == "body"
"""
                self.vs[40]["MT_label__"] = """41"""
                self.vs[40]["MT_subtypes__"] = []
                self.vs[40]["MT_dirty__"] = False
                self.vs[40]["mm__"] = """MT_pre__directLink_S"""
                self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc40')
        # match association StatementList--statements-->ReturnStatement node
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

return attr_value == "statements"
"""
                self.vs[41]["MT_label__"] = """42"""
                self.vs[41]["MT_subtypes__"] = []
                self.vs[41]["MT_dirty__"] = False
                self.vs[41]["mm__"] = """MT_pre__directLink_S"""
                self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc41')
        # match association ReturnStatement--expression-->ExecuteTestExpression node
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

return attr_value == "expression"
"""
                self.vs[42]["MT_label__"] = """43"""
                self.vs[42]["MT_subtypes__"] = []
                self.vs[42]["MT_dirty__"] = False
                self.vs[42]["mm__"] = """MT_pre__directLink_S"""
                self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc42')
        # match association ExecuteTestExpression--tests-->TestCaseRef node
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

return attr_value == "tests"
"""
                self.vs[43]["MT_label__"] = """44"""
                self.vs[43]["MT_subtypes__"] = []
                self.vs[43]["MT_dirty__"] = False
                self.vs[43]["mm__"] = """MT_pre__directLink_S"""
                self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc43')
        # match association TestCaseRef--testcase-->TestCase node
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

return attr_value == "testcase"
"""
                self.vs[44]["MT_label__"] = """45"""
                self.vs[44]["MT_subtypes__"] = []
                self.vs[44]["MT_dirty__"] = False
                self.vs[44]["mm__"] = """MT_pre__directLink_S"""
                self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc44')
        
        
        # Nodes that represent the apply associations of the property.
        # apply association ImplementationModule--contents-->Function node
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

return attr_value == "contents"
"""
                self.vs[45]["MT_label__"] = """46"""
                self.vs[45]["MT_subtypes__"] = []
                self.vs[45]["MT_dirty__"] = False
                self.vs[45]["mm__"] = """MT_pre__directLink_T"""
                self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc45')
        # apply association ImplementationModule--contents-->FunctionPrototype node
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

return attr_value == "contents"
"""
                self.vs[46]["MT_label__"] = """47"""
                self.vs[46]["MT_subtypes__"] = []
                self.vs[46]["MT_dirty__"] = False
                self.vs[46]["mm__"] = """MT_pre__directLink_T"""
                self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc46')
        # apply association ImplementationModule--contents-->FunctionPrototype node
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

return attr_value == "contents"
"""
                self.vs[47]["MT_label__"] = """48"""
                self.vs[47]["MT_subtypes__"] = []
                self.vs[47]["MT_dirty__"] = False
                self.vs[47]["mm__"] = """MT_pre__directLink_T"""
                self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc47')
        # apply association StatementList--statements-->ExpressionStatement node
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

return attr_value == "statements"
"""
                self.vs[48]["MT_label__"] = """49"""
                self.vs[48]["MT_subtypes__"] = []
                self.vs[48]["MT_dirty__"] = False
                self.vs[48]["mm__"] = """MT_pre__directLink_T"""
                self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc48')
        # apply association ImplementationModule--contents-->FunctionPrototype node
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

return attr_value == "contents"
"""
                self.vs[49]["MT_label__"] = """50"""
                self.vs[49]["MT_subtypes__"] = []
                self.vs[49]["MT_dirty__"] = False
                self.vs[49]["mm__"] = """MT_pre__directLink_T"""
                self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc49')
        # apply association Function--body-->StatementList node
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

return attr_value == "body"
"""
                self.vs[50]["MT_label__"] = """51"""
                self.vs[50]["MT_subtypes__"] = []
                self.vs[50]["MT_dirty__"] = False
                self.vs[50]["mm__"] = """MT_pre__directLink_T"""
                self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc50')
        # apply association ImplementationModule--contents-->Function node
                self.add_node()
                self.vs[51]["MT_subtypeMatching__"] = False
                self.vs[51]["MT_pre__attr1"] = """
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
                self.vs[51]["MT_label__"] = """52"""
                self.vs[51]["MT_subtypes__"] = []
                self.vs[51]["MT_dirty__"] = False
                self.vs[51]["mm__"] = """MT_pre__directLink_T"""
                self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc51')
        # apply association ExpressionStatement--expr-->FunctionCall node
                self.add_node()
                self.vs[52]["MT_subtypeMatching__"] = False
                self.vs[52]["MT_pre__attr1"] = """
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
                self.vs[52]["MT_label__"] = """53"""
                self.vs[52]["MT_subtypes__"] = []
                self.vs[52]["MT_dirty__"] = False
                self.vs[52]["mm__"] = """MT_pre__directLink_T"""
                self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc52')
        # apply association FunctionCall--function-->FunctionPrototype node
                self.add_node()
                self.vs[53]["MT_subtypeMatching__"] = False
                self.vs[53]["MT_pre__attr1"] = """
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
                self.vs[53]["MT_label__"] = """54"""
                self.vs[53]["MT_subtypes__"] = []
                self.vs[53]["MT_dirty__"] = False
                self.vs[53]["mm__"] = """MT_pre__directLink_T"""
                self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc53')
        # apply association ImplementationModule--contents-->Function node
                self.add_node()
                self.vs[54]["MT_subtypeMatching__"] = False
                self.vs[54]["MT_pre__attr1"] = """
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
                self.vs[54]["MT_label__"] = """55"""
                self.vs[54]["MT_subtypes__"] = []
                self.vs[54]["MT_dirty__"] = False
                self.vs[54]["mm__"] = """MT_pre__directLink_T"""
                self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc54')
        # apply association Function--body-->StatementList node
                self.add_node()
                self.vs[55]["MT_subtypeMatching__"] = False
                self.vs[55]["MT_pre__attr1"] = """
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
                self.vs[55]["MT_label__"] = """56"""
                self.vs[55]["MT_subtypes__"] = []
                self.vs[55]["MT_dirty__"] = False
                self.vs[55]["mm__"] = """MT_pre__directLink_T"""
                self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc55')
        # apply association StatementList--statements-->ExpressionStatement node
                self.add_node()
                self.vs[56]["MT_subtypeMatching__"] = False
                self.vs[56]["MT_pre__attr1"] = """
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
                self.vs[56]["MT_label__"] = """57"""
                self.vs[56]["MT_subtypes__"] = []
                self.vs[56]["MT_dirty__"] = False
                self.vs[56]["mm__"] = """MT_pre__directLink_T"""
                self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc56')
        # apply association ExpressionStatement--expr-->FunctionCall node
                self.add_node()
                self.vs[57]["MT_subtypeMatching__"] = False
                self.vs[57]["MT_pre__attr1"] = """
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
                self.vs[57]["MT_label__"] = """58"""
                self.vs[57]["MT_subtypes__"] = []
                self.vs[57]["MT_dirty__"] = False
                self.vs[57]["mm__"] = """MT_pre__directLink_T"""
                self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc57')
        # apply association FunctionCall--function-->FunctionPrototype node
                self.add_node()
                self.vs[58]["MT_subtypeMatching__"] = False
                self.vs[58]["MT_pre__attr1"] = """
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
                self.vs[58]["MT_label__"] = """59"""
                self.vs[58]["MT_subtypes__"] = []
                self.vs[58]["MT_dirty__"] = False
                self.vs[58]["mm__"] = """MT_pre__directLink_T"""
                self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc58')
        # apply association ImplementationModule--contents-->Function node
                self.add_node()
                self.vs[59]["MT_subtypeMatching__"] = False
                self.vs[59]["MT_pre__attr1"] = """
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
                self.vs[59]["MT_label__"] = """60"""
                self.vs[59]["MT_subtypes__"] = []
                self.vs[59]["MT_dirty__"] = False
                self.vs[59]["mm__"] = """MT_pre__directLink_T"""
                self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc59')
        # apply association ImplementationModule--contents-->Function node
                self.add_node()
                self.vs[60]["MT_subtypeMatching__"] = False
                self.vs[60]["MT_pre__attr1"] = """
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
                self.vs[60]["MT_label__"] = """61"""
                self.vs[60]["MT_subtypes__"] = []
                self.vs[60]["MT_dirty__"] = False
                self.vs[60]["mm__"] = """MT_pre__directLink_T"""
                self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc60')
        # apply association FunctionCall--function-->FunctionPrototype node
                self.add_node()
                self.vs[61]["MT_subtypeMatching__"] = False
                self.vs[61]["MT_pre__attr1"] = """
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
                self.vs[61]["MT_label__"] = """62"""
                self.vs[61]["MT_subtypes__"] = []
                self.vs[61]["MT_dirty__"] = False
                self.vs[61]["mm__"] = """MT_pre__directLink_T"""
                self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc61')
        # apply association Function--body-->StatementList node
                self.add_node()
                self.vs[62]["MT_subtypeMatching__"] = False
                self.vs[62]["MT_pre__attr1"] = """
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
                self.vs[62]["MT_label__"] = """63"""
                self.vs[62]["MT_subtypes__"] = []
                self.vs[62]["MT_dirty__"] = False
                self.vs[62]["mm__"] = """MT_pre__directLink_T"""
                self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc62')
        # apply association Function--body-->StatementList node
                self.add_node()
                self.vs[63]["MT_subtypeMatching__"] = False
                self.vs[63]["MT_pre__attr1"] = """
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
                self.vs[63]["MT_label__"] = """64"""
                self.vs[63]["MT_subtypes__"] = []
                self.vs[63]["MT_dirty__"] = False
                self.vs[63]["mm__"] = """MT_pre__directLink_T"""
                self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc63')
        # apply association StatementList--statements-->ExpressionStatement node
                self.add_node()
                self.vs[64]["MT_subtypeMatching__"] = False
                self.vs[64]["MT_pre__attr1"] = """
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
                self.vs[64]["MT_label__"] = """65"""
                self.vs[64]["MT_subtypes__"] = []
                self.vs[64]["MT_dirty__"] = False
                self.vs[64]["mm__"] = """MT_pre__directLink_T"""
                self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc64')
        # apply association ExpressionStatement--expr-->FunctionCall node
                self.add_node()
                self.vs[65]["MT_subtypeMatching__"] = False
                self.vs[65]["MT_pre__attr1"] = """
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
                self.vs[65]["MT_label__"] = """66"""
                self.vs[65]["MT_subtypes__"] = []
                self.vs[65]["MT_dirty__"] = False
                self.vs[65]["mm__"] = """MT_pre__directLink_T"""
                self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc65')
        # apply association StatementList--statements-->ExpressionStatement node
                self.add_node()
                self.vs[66]["MT_subtypeMatching__"] = False
                self.vs[66]["MT_pre__attr1"] = """
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
                self.vs[66]["MT_label__"] = """67"""
                self.vs[66]["MT_subtypes__"] = []
                self.vs[66]["MT_dirty__"] = False
                self.vs[66]["mm__"] = """MT_pre__directLink_T"""
                self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc66')
        # apply association ExpressionStatement--expr-->FunctionCall node
                self.add_node()
                self.vs[67]["MT_subtypeMatching__"] = False
                self.vs[67]["MT_pre__attr1"] = """
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
                self.vs[67]["MT_label__"] = """68"""
                self.vs[67]["MT_subtypes__"] = []
                self.vs[67]["MT_dirty__"] = False
                self.vs[67]["mm__"] = """MT_pre__directLink_T"""
                self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc67')
        # apply association ImplementationModule--contents-->FunctionPrototype node
                self.add_node()
                self.vs[68]["MT_subtypeMatching__"] = False
                self.vs[68]["MT_pre__attr1"] = """
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
                self.vs[68]["MT_label__"] = """69"""
                self.vs[68]["MT_subtypes__"] = []
                self.vs[68]["MT_dirty__"] = False
                self.vs[68]["mm__"] = """MT_pre__directLink_T"""
                self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc68')
        # apply association FunctionCall--function-->FunctionPrototype node
                self.add_node()
                self.vs[69]["MT_subtypeMatching__"] = False
                self.vs[69]["MT_pre__attr1"] = """
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
                self.vs[69]["MT_label__"] = """70"""
                self.vs[69]["MT_subtypes__"] = []
                self.vs[69]["MT_dirty__"] = False
                self.vs[69]["mm__"] = """MT_pre__directLink_T"""
                self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc69')
        
                # Nodes that represent trace relations
                # backward association InstanceConfiguration---->FunctionPrototype node
                self.add_node()
                self.vs[70]["MT_subtypeMatching__"] = False
                self.vs[70]["MT_label__"] = """71"""
                self.vs[70]["MT_subtypes__"] = []
                self.vs[70]["MT_dirty__"] = False
                self.vs[70]["mm__"] = """MT_pre__trace_link"""
                self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink70')
                # backward association InstanceConfiguration---->Function node
                self.add_node()
                self.vs[71]["MT_subtypeMatching__"] = False
                self.vs[71]["MT_label__"] = """72"""
                self.vs[71]["MT_subtypes__"] = []
                self.vs[71]["MT_dirty__"] = False
                self.vs[71]["mm__"] = """MT_pre__trace_link"""
                self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink71')
                # backward association ImplementationModule---->ImplementationModule node
                self.add_node()
                self.vs[72]["MT_subtypeMatching__"] = False
                self.vs[72]["MT_label__"] = """73"""
                self.vs[72]["MT_subtypes__"] = []
                self.vs[72]["MT_dirty__"] = False
                self.vs[72]["mm__"] = """MT_pre__trace_link"""
                self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink72')
                # backward association ComponentInstance---->FunctionPrototype node
                self.add_node()
                self.vs[73]["MT_subtypeMatching__"] = False
                self.vs[73]["MT_label__"] = """74"""
                self.vs[73]["MT_subtypes__"] = []
                self.vs[73]["MT_dirty__"] = False
                self.vs[73]["mm__"] = """MT_pre__trace_link"""
                self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink73')
                # backward association Function---->FunctionPrototype node
                self.add_node()
                self.vs[74]["MT_subtypeMatching__"] = False
                self.vs[74]["MT_label__"] = """75"""
                self.vs[74]["MT_subtypes__"] = []
                self.vs[74]["MT_dirty__"] = False
                self.vs[74]["mm__"] = """MT_pre__trace_link"""
                self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink74')
                # backward association ComponentInstance---->Function node
                self.add_node()
                self.vs[75]["MT_subtypeMatching__"] = False
                self.vs[75]["MT_label__"] = """76"""
                self.vs[75]["MT_subtypes__"] = []
                self.vs[75]["MT_dirty__"] = False
                self.vs[75]["mm__"] = """MT_pre__trace_link"""
                self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink75')
                # backward association TestCase---->Function node
                self.add_node()
                self.vs[76]["MT_subtypeMatching__"] = False
                self.vs[76]["MT_label__"] = """77"""
                self.vs[76]["MT_subtypes__"] = []
                self.vs[76]["MT_dirty__"] = False
                self.vs[76]["mm__"] = """MT_pre__trace_link"""
                self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink76')
                # backward association InitializeConfiguration---->FunctionCall node
                self.add_node()
                self.vs[77]["MT_subtypeMatching__"] = False
                self.vs[77]["MT_label__"] = """78"""
                self.vs[77]["MT_subtypes__"] = []
                self.vs[77]["MT_dirty__"] = False
                self.vs[77]["mm__"] = """MT_pre__trace_link"""
                self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink77')
                # backward association Function---->Function node
                self.add_node()
                self.vs[78]["MT_subtypeMatching__"] = False
                self.vs[78]["MT_label__"] = """79"""
                self.vs[78]["MT_subtypes__"] = []
                self.vs[78]["MT_dirty__"] = False
                self.vs[78]["mm__"] = """MT_pre__trace_link"""
                self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink78')
                # backward association Function---->Function node
                self.add_node()
                self.vs[79]["MT_subtypeMatching__"] = False
                self.vs[79]["MT_label__"] = """80"""
                self.vs[79]["MT_subtypes__"] = []
                self.vs[79]["MT_dirty__"] = False
                self.vs[79]["mm__"] = """MT_pre__trace_link"""
                self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink79')
                # backward association TestCaseRef---->FunctionCall node
                self.add_node()
                self.vs[80]["MT_subtypeMatching__"] = False
                self.vs[80]["MT_label__"] = """81"""
                self.vs[80]["MT_subtypes__"] = []
                self.vs[80]["MT_dirty__"] = False
                self.vs[80]["mm__"] = """MT_pre__trace_link"""
                self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink80')
                # backward association TestCase---->FunctionPrototype node
                self.add_node()
                self.vs[81]["MT_subtypeMatching__"] = False
                self.vs[81]["MT_label__"] = """82"""
                self.vs[81]["MT_subtypes__"] = []
                self.vs[81]["MT_dirty__"] = False
                self.vs[81]["mm__"] = """MT_pre__trace_link"""
                self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink81')


        
        
        
        
        
                # Add the edges
                self.add_edges([
                (12,70), # apply_class FunctionPrototype() -> backward_association
                (70,3), #  backward_association -> apply_class InstanceConfiguration()
                (11,71), # apply_class Function() -> backward_association
                (71,3), #  backward_association -> apply_class InstanceConfiguration()
                (13,72), # apply_class ImplementationModule() -> backward_association
                (72,0), #  backward_association -> apply_class ImplementationModule()
                (15,73), # apply_class FunctionPrototype() -> backward_association
                (73,2), #  backward_association -> apply_class ComponentInstance()
                (14,74), # apply_class FunctionPrototype() -> backward_association
                (74,1), #  backward_association -> apply_class Function()
                (17,75), # apply_class Function() -> backward_association
                (75,2), #  backward_association -> apply_class ComponentInstance()
                (23,76), # apply_class Function() -> backward_association
                (76,4), #  backward_association -> apply_class TestCase()
                (20,77), # apply_class FunctionCall() -> backward_association
                (77,6), #  backward_association -> apply_class InitializeConfiguration()
                (24,78), # apply_class Function() -> backward_association
                (78,1), #  backward_association -> apply_class Function()
                (27,79), # apply_class Function() -> backward_association
                (79,1), #  backward_association -> apply_class Function()
                (31,80), # apply_class FunctionCall() -> backward_association
                (80,9), #  backward_association -> apply_class TestCaseRef()
                (32,81), # apply_class FunctionPrototype() -> backward_association
                (81,4), #  backward_association -> apply_class TestCase()
                (13,45), # apply_class ImplementationModule() -> association contents
                (45,11), # association contents  -> apply_class Function()
                (13,46), # apply_class ImplementationModule() -> association contents
                (46,12), # association contents  -> apply_class FunctionPrototype()
                (13,47), # apply_class ImplementationModule() -> association contents
                (47,14), # association contents  -> apply_class FunctionPrototype()
                (16,48), # apply_class StatementList() -> association statements
                (48,18), # association statements  -> apply_class ExpressionStatement()
                (13,49), # apply_class ImplementationModule() -> association contents
                (49,15), # association contents  -> apply_class FunctionPrototype()
                (11,50), # apply_class Function() -> association body
                (50,16), # association body  -> apply_class StatementList()
                (13,51), # apply_class ImplementationModule() -> association contents
                (51,17), # association contents  -> apply_class Function()
                (18,52), # apply_class ExpressionStatement() -> association expr
                (52,19), # association expr  -> apply_class FunctionCall()
                (19,53), # apply_class FunctionCall() -> association function
                (53,15), # association function  -> apply_class FunctionPrototype()
                (13,54), # apply_class ImplementationModule() -> association contents
                (54,23), # association contents  -> apply_class Function()
                (23,55), # apply_class Function() -> association body
                (55,22), # association body  -> apply_class StatementList()
                (22,56), # apply_class StatementList() -> association statements
                (56,21), # association statements  -> apply_class ExpressionStatement()
                (21,57), # apply_class ExpressionStatement() -> association expr
                (57,20), # association expr  -> apply_class FunctionCall()
                (20,58), # apply_class FunctionCall() -> association function
                (58,12), # association function  -> apply_class FunctionPrototype()
                (13,59), # apply_class ImplementationModule() -> association contents
                (59,24), # association contents  -> apply_class Function()
                (13,60), # apply_class ImplementationModule() -> association contents
                (60,27), # association contents  -> apply_class Function()
                (28,61), # apply_class FunctionCall() -> association function
                (61,14), # association function  -> apply_class FunctionPrototype()
                (24,62), # apply_class Function() -> association body
                (62,29), # association body  -> apply_class StatementList()
                (27,63), # apply_class Function() -> association body
                (63,26), # association body  -> apply_class StatementList()
                (26,64), # apply_class StatementList() -> association statements
                (64,25), # association statements  -> apply_class ExpressionStatement()
                (25,65), # apply_class ExpressionStatement() -> association expr
                (65,28), # association expr  -> apply_class FunctionCall()
                (29,66), # apply_class StatementList() -> association statements
                (66,30), # association statements  -> apply_class ExpressionStatement()
                (30,67), # apply_class ExpressionStatement() -> association expr
                (67,31), # association expr  -> apply_class FunctionCall()
                (13,68), # apply_class ImplementationModule() -> association contents
                (68,32), # association contents  -> apply_class FunctionPrototype()
                (31,69), # apply_class FunctionCall() -> association function
                (69,32), # association function  -> apply_class FunctionPrototype()
                (3,33), # match_class InstanceConfiguration() -> association contents
                (33,2), # association contents  -> match_class ComponentInstance()
                (0,34), # match_class ImplementationModule() -> association contents
                (34,1), # association contents  -> match_class Function()
                (0,35), # match_class ImplementationModule() -> association contents
                (35,3), # association contents  -> match_class InstanceConfiguration()
                (0,36), # match_class ImplementationModule() -> association contents
                (36,4), # association contents  -> match_class TestCase()
                (4,37), # match_class TestCase() -> association body
                (37,5), # association body  -> match_class StatementList()
                (5,38), # match_class StatementList() -> association statements
                (38,6), # association statements  -> match_class InitializeConfiguration()
                (6,39), # match_class InitializeConfiguration() -> association config
                (39,3), # association config  -> match_class InstanceConfiguration()
                (1,40), # match_class Function() -> association body
                (40,7), # association body  -> match_class StatementList()
                (7,41), # match_class StatementList() -> association statements
                (41,10), # association statements  -> match_class ReturnStatement()
                (10,42), # match_class ReturnStatement() -> association expression
                (42,8), # association expression  -> match_class ExecuteTestExpression()
                (8,43), # match_class ExecuteTestExpression() -> association tests
                (43,9), # association tests  -> match_class TestCaseRef()
                (9,44), # match_class TestCaseRef() -> association testcase
                (44,4) # association testcase  -> match_class TestCase()
                ])
        
                # Add the attribute equations
                self["equations"] = []
        
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

                return attr_value == "contents"


        def eval_attr136(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr137(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr138(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr139(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr140(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "config"


        def eval_attr141(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr142(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr143(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expression"


        def eval_attr144(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "tests"


        def eval_attr145(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "testcase"


        
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
        
        def eval_attr127(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr128(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr129(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr130(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr131(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr132(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr133(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return True
        
        def eval_attr146(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr147(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr148(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr149(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr150(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr151(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr152(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr153(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expr"


        def eval_attr154(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "function"


        def eval_attr155(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr156(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr157(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr158(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expr"


        def eval_attr159(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "function"


        def eval_attr160(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr161(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr162(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "function"


        def eval_attr163(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr164(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "body"


        def eval_attr165(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr166(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expr"


        def eval_attr167(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "statements"


        def eval_attr168(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expr"


        def eval_attr169(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "contents"


        def eval_attr170(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "function"


        
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

