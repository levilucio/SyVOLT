

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HBuildTraceabilityForRuleLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBuildTraceabilityForRuleLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBuildTraceabilityForRuleLHS, self).__init__(name='HBuildTraceabilityForRuleLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[3, 0], [0, 4], [1, 2], [2, 5]])
        # Set the graph attributes
        self["MT_constraint__"] = """mms = graph.vs["mm__"]
if set([i for i in graph.neighbors(PreNode('1').index) if mms[i] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if mms[i] == 'trace_link'])) == set():
    return True

return False
"""
        self["equations"] = []
        self["superclasses_dict"] = {'CModule': ['MetaModelElement_T'], 'GlobalVarRef': ['MetaModelElement_T'], 'ICanBeExecutedAsTest': ['MetaModelElement_S'], 'GenericDotExpression': ['MetaModelElement_T'], 'ProvidedPort': ['MetaModelElement_S'], 'BinaryArithmeticExpression': ['MetaModelElement_S'], 'IVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapter': ['MetaModelElement_S'], 'FunctionPrototype': ['MetaModelElement_T'], 'StringType': ['MetaModelElement_T', 'MetaModelElement_S'], 'InstanceConfigContents': ['MetaModelElement_S'], 'VoidType': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationParameter': ['MetaModelElement_S'], 'PortAdapterRefExpr': ['MetaModelElement_S'], 'ReturnStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'IHasPrefixes': ['MetaModelElement_T'], 'OperationTrigger': ['MetaModelElement_S'], 'ArgumentRef': ['MetaModelElement_S'], 'IGenericDotTarget': ['MetaModelElement_T'], 'TypeWithDeclaration': ['MetaModelElement_T'], 'Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'TestCase': ['MetaModelElement_S'], 'INamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'SUType': ['MetaModelElement_T'], 'Executable': ['MetaModelElement_S'], 'Interface': ['MetaModelElement_S'], 'IModuleContentContainer': ['MetaModelElement_T', 'MetaModelElement_S'], 'IModuleContent': ['MetaModelElement_T', 'MetaModelElement_S'], 'SUDeclaration': ['MetaModelElement_T'], 'Statement': ['MetaModelElement_T', 'MetaModelElement_S'], 'AdapterInstancePortRef': ['MetaModelElement_S'], 'PortRefExpr': ['MetaModelElement_S'], 'GlobalVariableDeclaration': ['MetaModelElement_T'], 'CFunctionPointerStructMember': ['MetaModelElement_T'], 'TestCaseRef': ['MetaModelElement_S'], 'RequiredPort': ['MetaModelElement_S'], 'ComponentInstance': ['MetaModelElement_S'], 'ClientServerInterface': ['MetaModelElement_S'], 'AssemblyConnector': ['MetaModelElement_S'], 'Literal': ['MetaModelElement_T', 'MetaModelElement_S'], 'IType': ['MetaModelElement_T'], 'TypeDef': ['MetaModelElement_T'], 'InstanceConfiguration': ['MetaModelElement_S'], 'ITypeContainingType': ['MetaModelElement_T', 'MetaModelElement_S'], 'StructType': ['MetaModelElement_T'], 'PointerExpr': ['MetaModelElement_T'], 'GreaterEqualsExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'Function': ['MetaModelElement_T', 'MetaModelElement_S'], 'PointerType': ['MetaModelElement_T'], 'InterfaceOperationCallExpr': ['MetaModelElement_S'], 'ReferenceExpr': ['MetaModelElement_T'], 'Port': ['MetaModelElement_S'], 'IArgumentLike': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionRefExpr': ['MetaModelElement_T'], 'IControlledNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionCall': ['MetaModelElement_T'], 'BinaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'RequiredPortOpCallExpr': ['MetaModelElement_S'], 'PlusExpression': ['MetaModelElement_S'], 'AtomicComponent': ['MetaModelElement_S'], 'Int32Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'LocalVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'ITyped': ['MetaModelElement_T', 'MetaModelElement_S'], 'ExecuteTestExpression': ['MetaModelElement_S'], 'Argument': ['MetaModelElement_T', 'MetaModelElement_S'], 'IOperationTriggerLike': ['MetaModelElement_S'], 'ImplementationModule': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssignmentExpr': ['MetaModelElement_T', 'MetaModelElement_S'], 'Prefix': ['MetaModelElement_T'], 'ArrayType': ['MetaModelElement_T', 'MetaModelElement_S'], 'MbeddrModule': ['MetaModelElement_S'], 'StatementList': ['MetaModelElement_T', 'MetaModelElement_S'], 'AbstractInstanceConfiguration': ['MetaModelElement_S'], 'FunctionSignature': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortRef': ['MetaModelElement_S'], 'NumericLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'GenericMemberRef': ['MetaModelElement_T'], 'Expression': ['MetaModelElement_T', 'MetaModelElement_S'], 'DerefExpr': ['MetaModelElement_T'], 'StructDeclaration': ['MetaModelElement_T'], 'SUContent': ['MetaModelElement_T'], 'InstancePortRef': ['MetaModelElement_S'], 'TypeDefType': ['MetaModelElement_T'], 'BinaryOrderedComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'PrimitiveType': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionRefType': ['MetaModelElement_T'], 'IFunctionLike': ['MetaModelElement_T', 'MetaModelElement_S'], 'BinaryComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'ModuleContentSUDeclaration': ['MetaModelElement_T'], 'InitializeConfiguration': ['MetaModelElement_S'], 'CastExpression': ['MetaModelElement_T'], 'PortAdapterOpCallExpr': ['MetaModelElement_S'], 'Member': ['MetaModelElement_T'], 'StringLiteral': ['MetaModelElement_S'], 'Operation': ['MetaModelElement_S'], 'ExpressionStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'NumberLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'WhileStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'IComponentContent': ['MetaModelElement_S'], 'Component': ['MetaModelElement_S'], 'IIdentifierNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'RunnableTrigger': ['MetaModelElement_S'], 'LocalVarRef': ['MetaModelElement_S'], 'PrimitiveC99IntegralType': ['MetaModelElement_T', 'MetaModelElement_S'], 'ICSInterfaceContents': ['MetaModelElement_S'], 'UnaryExpression': ['MetaModelElement_T', 'MetaModelElement_S']}
        self["name"] = """"""
        self["mm__"] = ['MT_pre__mbeddr_MM', 'MoTifRule']
        self["GUID__"] = 1339043830988334966
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["GUID__"] = 6601769124712063922
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["mm__"] = """MT_pre__apply_contains"""
        self.vs[0]["MT_subtypes__"] = []
        self.vs[0]["MT_label__"] = """6"""
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["GUID__"] = 3211031155982416150
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["mm__"] = """MT_pre__MatchModel"""
        self.vs[1]["MT_subtypes__"] = []
        self.vs[1]["MT_label__"] = """3"""
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["GUID__"] = 3676593120352744638
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["mm__"] = """MT_pre__match_contains"""
        self.vs[2]["MT_subtypes__"] = []
        self.vs[2]["MT_label__"] = """5"""
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["GUID__"] = 3729121856167067283
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["mm__"] = """MT_pre__ApplyModel"""
        self.vs[3]["MT_subtypes__"] = []
        self.vs[3]["MT_label__"] = """4"""
        self.vs[4]["MT_subtypeMatching__"] = True
        self.vs[4]["MT_pre__name"] = """
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
        self.vs[4]["MT_pre__cardinality"] = """
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
        self.vs[4]["GUID__"] = 925503974014884163
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["MT_pre__classtype"] = """
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
        self.vs[4]["mm__"] = """MT_pre__MetaModelElement_T"""
        self.vs[4]["MT_subtypes__"] = ['MT_pre__CommunityRoot', 'MT_pre__Person', 'MT_pre__Man', 'MT_pre__Woman']
        self.vs[4]["MT_label__"] = """2"""
        self.vs[5]["MT_subtypeMatching__"] = True
        self.vs[5]["MT_pre__name"] = """
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
        self.vs[5]["MT_pre__cardinality"] = """
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
        self.vs[5]["GUID__"] = 9053659576832917539
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["MT_pre__classtype"] = """
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
        self.vs[5]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[5]["MT_subtypes__"] = ['MT_pre__HouseholdRoot', 'MT_pre__Family', 'MT_pre__Member']
        self.vs[5]["MT_label__"] = """1"""

    def eval_name2(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality2(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype2(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_cardinality1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        mms = graph.vs["mm__"]
        if set([i for i in graph.neighbors(PreNode('1').index) if mms[i] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if mms[i] == 'trace_link'])) == set():
            return True
        
        return False

