

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HDeleteUncollapsedElementLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDeleteUncollapsedElementLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeleteUncollapsedElementLHS, self).__init__(name='HDeleteUncollapsedElementLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 3], [5, 1], [1, 2]])
        # Set the graph attributes
        self["name"] = """"""
        self["mm__"] = ['MT_pre__mbeddr_MM', 'MoTifRule']
        self["MT_constraint__"] = """return True"""
        self["superclasses_dict"] = {'FunctionRefType': ['MetaModelElement_T'], 'NumericLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'ExpressionStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'TestCaseRef': ['MetaModelElement_S'], 'PrimitiveType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapterRefExpr': ['MetaModelElement_S'], 'ReturnStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'Statement': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssemblyConnector': ['MetaModelElement_S'], 'CFunctionPointerStructMember': ['MetaModelElement_T'], 'PortAdapter': ['MetaModelElement_S'], 'ModuleContentSUDeclaration': ['MetaModelElement_T'], 'FunctionSignature': ['MetaModelElement_T', 'MetaModelElement_S'], 'StatementList': ['MetaModelElement_T', 'MetaModelElement_S'], 'BinaryComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationTrigger': ['MetaModelElement_S'], 'SUType': ['MetaModelElement_T'], 'Int32Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'InterfaceOperationCallExpr': ['MetaModelElement_S'], 'SUContent': ['MetaModelElement_T'], 'PointerType': ['MetaModelElement_T'], 'Operation': ['MetaModelElement_S'], 'GlobalVariableDeclaration': ['MetaModelElement_T'], 'PortRef': ['MetaModelElement_S'], 'StructDeclaration': ['MetaModelElement_T'], 'PortRefExpr': ['MetaModelElement_S'], 'Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'StringType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PointerExpr': ['MetaModelElement_T'], 'PlusExpression': ['MetaModelElement_S'], 'AbstractInstanceConfiguration': ['MetaModelElement_S'], 'Interface': ['MetaModelElement_S'], 'IType': ['MetaModelElement_T'], 'GreaterEqualsExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'ArgumentRef': ['MetaModelElement_S'], 'ITypeContainingType': ['MetaModelElement_T', 'MetaModelElement_S'], 'ITyped': ['MetaModelElement_T', 'MetaModelElement_S'], 'Argument': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionCall': ['MetaModelElement_T'], 'SUDeclaration': ['MetaModelElement_T'], 'DerefExpr': ['MetaModelElement_T'], 'ExecuteTestExpression': ['MetaModelElement_S'], 'Member': ['MetaModelElement_T'], 'Literal': ['MetaModelElement_T', 'MetaModelElement_S'], 'IArgumentLike': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionRefExpr': ['MetaModelElement_T'], 'AdapterInstancePortRef': ['MetaModelElement_S'], 'InstancePortRef': ['MetaModelElement_S'], 'ICanBeExecutedAsTest': ['MetaModelElement_S'], 'RequiredPort': ['MetaModelElement_S'], 'LocalVarRef': ['MetaModelElement_S'], 'CModule': ['MetaModelElement_T'], 'IModuleContent': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssignmentExpr': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeWithDeclaration': ['MetaModelElement_T'], 'StructType': ['MetaModelElement_T'], 'AtomicComponent': ['MetaModelElement_S'], 'InstanceConfiguration': ['MetaModelElement_S'], 'NumberLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationParameter': ['MetaModelElement_S'], 'InstanceConfigContents': ['MetaModelElement_S'], 'GlobalVarRef': ['MetaModelElement_T'], 'BinaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'Expression': ['MetaModelElement_T', 'MetaModelElement_S'], 'LocalVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'UnaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'VoidType': ['MetaModelElement_T', 'MetaModelElement_S'], 'WhileStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'StringLiteral': ['MetaModelElement_S'], 'ProvidedPort': ['MetaModelElement_S'], 'Prefix': ['MetaModelElement_T'], 'MbeddrModule': ['MetaModelElement_S'], 'ImplementationModule': ['MetaModelElement_T', 'MetaModelElement_S'], 'Executable': ['MetaModelElement_S'], 'CastExpression': ['MetaModelElement_T'], 'GenericDotExpression': ['MetaModelElement_T'], 'IGenericDotTarget': ['MetaModelElement_T'], 'ArrayType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PrimitiveC99IntegralType': ['MetaModelElement_T', 'MetaModelElement_S'], 'IIdentifierNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapterOpCallExpr': ['MetaModelElement_S'], 'IVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'Function': ['MetaModelElement_T', 'MetaModelElement_S'], 'IControlledNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionPrototype': ['MetaModelElement_T'], 'Component': ['MetaModelElement_S'], 'TestCase': ['MetaModelElement_S'], 'RunnableTrigger': ['MetaModelElement_S'], 'BinaryArithmeticExpression': ['MetaModelElement_S'], 'ComponentInstance': ['MetaModelElement_S'], 'GenericMemberRef': ['MetaModelElement_T'], 'ICSInterfaceContents': ['MetaModelElement_S'], 'ReferenceExpr': ['MetaModelElement_T'], 'RequiredPortOpCallExpr': ['MetaModelElement_S'], 'BinaryOrderedComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeDefType': ['MetaModelElement_T'], 'IComponentContent': ['MetaModelElement_S'], 'INamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeDef': ['MetaModelElement_T'], 'IOperationTriggerLike': ['MetaModelElement_S'], 'InitializeConfiguration': ['MetaModelElement_S'], 'ClientServerInterface': ['MetaModelElement_S'], 'IModuleContentContainer': ['MetaModelElement_T', 'MetaModelElement_S'], 'IHasPrefixes': ['MetaModelElement_T'], 'Port': ['MetaModelElement_S'], 'IFunctionLike': ['MetaModelElement_T', 'MetaModelElement_S']}
        self["equations"] = []
        self["GUID__"] = 8606295276883309858
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["mm__"] = """MT_pre__match_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 2492652436716073316
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["mm__"] = """MT_pre__match_contains"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 1356976907983983460
        self.vs[2]["MT_pivotOut__"] = """element2"""
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
        self.vs[2]["MT_pivotIn__"] = """element2"""
        self.vs[2]["MT_label__"] = """2"""
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = 5061772226935437731
        self.vs[3]["MT_pivotOut__"] = """element1"""
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
        self.vs[3]["MT_pivotIn__"] = """element1"""
        self.vs[3]["MT_label__"] = """1"""
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = 6670895658872261885
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["mm__"] = """MT_pre__MatchModel"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = 2929545596509939901
        self.vs[5]["MT_label__"] = """4"""
        self.vs[5]["mm__"] = """MT_pre__MatchModel"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = 589586432928941143

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



    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

