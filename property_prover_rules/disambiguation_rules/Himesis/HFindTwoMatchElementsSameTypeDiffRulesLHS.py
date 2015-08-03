

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HFindTwoMatchElementsSameTypeDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFindTwoMatchElementsSameTypeDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFindTwoMatchElementsSameTypeDiffRulesLHS, self).__init__(name='HFindTwoMatchElementsSameTypeDiffRulesLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 2], [5, 1], [1, 3]])
        # Set the graph attributes
        self["name"] = """"""
        self["mm__"] = ['MT_pre__mbeddr_MM', 'MoTifRule']
        self["MT_constraint__"] = """
guid1 = PreNode('1').index
guid2 = PreNode('2').index

matchModel1ID = PreNode('3').index
matchModel2ID = PreNode('4').index

if PreNode('1')['classtype'] == PreNode('2')['classtype'] and int(guid1) < int(guid2) and int(matchModel1ID) < int(matchModel2ID):
    return True
return False
"""
        self["superclasses_dict"] = {'FunctionRefType': ['MetaModelElement_T'], 'NumericLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'ExpressionStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'TestCaseRef': ['MetaModelElement_S'], 'PrimitiveType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapterRefExpr': ['MetaModelElement_S'], 'ReturnStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'Statement': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssemblyConnector': ['MetaModelElement_S'], 'CFunctionPointerStructMember': ['MetaModelElement_T'], 'PortAdapter': ['MetaModelElement_S'], 'ModuleContentSUDeclaration': ['MetaModelElement_T'], 'FunctionSignature': ['MetaModelElement_T', 'MetaModelElement_S'], 'StatementList': ['MetaModelElement_T', 'MetaModelElement_S'], 'BinaryComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationTrigger': ['MetaModelElement_S'], 'SUType': ['MetaModelElement_T'], 'Int32Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'InterfaceOperationCallExpr': ['MetaModelElement_S'], 'SUContent': ['MetaModelElement_T'], 'PointerType': ['MetaModelElement_T'], 'Operation': ['MetaModelElement_S'], 'GlobalVariableDeclaration': ['MetaModelElement_T'], 'PortRef': ['MetaModelElement_S'], 'StructDeclaration': ['MetaModelElement_T'], 'PortRefExpr': ['MetaModelElement_S'], 'Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'StringType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PointerExpr': ['MetaModelElement_T'], 'PlusExpression': ['MetaModelElement_S'], 'AbstractInstanceConfiguration': ['MetaModelElement_S'], 'Interface': ['MetaModelElement_S'], 'IType': ['MetaModelElement_T'], 'GreaterEqualsExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'ArgumentRef': ['MetaModelElement_S'], 'ITypeContainingType': ['MetaModelElement_T', 'MetaModelElement_S'], 'ITyped': ['MetaModelElement_T', 'MetaModelElement_S'], 'Argument': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionCall': ['MetaModelElement_T'], 'SUDeclaration': ['MetaModelElement_T'], 'DerefExpr': ['MetaModelElement_T'], 'ExecuteTestExpression': ['MetaModelElement_S'], 'Member': ['MetaModelElement_T'], 'Literal': ['MetaModelElement_T', 'MetaModelElement_S'], 'IArgumentLike': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionRefExpr': ['MetaModelElement_T'], 'AdapterInstancePortRef': ['MetaModelElement_S'], 'InstancePortRef': ['MetaModelElement_S'], 'ICanBeExecutedAsTest': ['MetaModelElement_S'], 'RequiredPort': ['MetaModelElement_S'], 'LocalVarRef': ['MetaModelElement_S'], 'CModule': ['MetaModelElement_T'], 'IModuleContent': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssignmentExpr': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeWithDeclaration': ['MetaModelElement_T'], 'StructType': ['MetaModelElement_T'], 'AtomicComponent': ['MetaModelElement_S'], 'InstanceConfiguration': ['MetaModelElement_S'], 'NumberLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationParameter': ['MetaModelElement_S'], 'InstanceConfigContents': ['MetaModelElement_S'], 'GlobalVarRef': ['MetaModelElement_T'], 'BinaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'Expression': ['MetaModelElement_T', 'MetaModelElement_S'], 'LocalVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'UnaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'VoidType': ['MetaModelElement_T', 'MetaModelElement_S'], 'WhileStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'StringLiteral': ['MetaModelElement_S'], 'ProvidedPort': ['MetaModelElement_S'], 'Prefix': ['MetaModelElement_T'], 'MbeddrModule': ['MetaModelElement_S'], 'ImplementationModule': ['MetaModelElement_T', 'MetaModelElement_S'], 'Executable': ['MetaModelElement_S'], 'CastExpression': ['MetaModelElement_T'], 'GenericDotExpression': ['MetaModelElement_T'], 'IGenericDotTarget': ['MetaModelElement_T'], 'ArrayType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PrimitiveC99IntegralType': ['MetaModelElement_T', 'MetaModelElement_S'], 'IIdentifierNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapterOpCallExpr': ['MetaModelElement_S'], 'IVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'Function': ['MetaModelElement_T', 'MetaModelElement_S'], 'IControlledNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionPrototype': ['MetaModelElement_T'], 'Component': ['MetaModelElement_S'], 'TestCase': ['MetaModelElement_S'], 'RunnableTrigger': ['MetaModelElement_S'], 'BinaryArithmeticExpression': ['MetaModelElement_S'], 'ComponentInstance': ['MetaModelElement_S'], 'GenericMemberRef': ['MetaModelElement_T'], 'ICSInterfaceContents': ['MetaModelElement_S'], 'ReferenceExpr': ['MetaModelElement_T'], 'RequiredPortOpCallExpr': ['MetaModelElement_S'], 'BinaryOrderedComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeDefType': ['MetaModelElement_T'], 'IComponentContent': ['MetaModelElement_S'], 'INamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeDef': ['MetaModelElement_T'], 'IOperationTriggerLike': ['MetaModelElement_S'], 'InitializeConfiguration': ['MetaModelElement_S'], 'ClientServerInterface': ['MetaModelElement_S'], 'IModuleContentContainer': ['MetaModelElement_T', 'MetaModelElement_S'], 'IHasPrefixes': ['MetaModelElement_T'], 'Port': ['MetaModelElement_S'], 'IFunctionLike': ['MetaModelElement_T', 'MetaModelElement_S']}
        self["equations"] = []
        self["GUID__"] = 4448450274503426919
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["mm__"] = """MT_pre__match_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 7181928297639646230
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["mm__"] = """MT_pre__match_contains"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 7943422122721247554
        self.vs[2]["MT_pivotOut__"] = """element1"""
        self.vs[2]["MT_pre__classtype"] = """
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
        self.vs[2]["MT_pre__cardinality"] = """

return True
"""
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__name"] = """

return True
"""
        self.vs[2]["GUID__"] = 2210858195324649237
        self.vs[3]["MT_pivotOut__"] = """element2"""
        self.vs[3]["MT_pre__classtype"] = """

return True
"""
        self.vs[3]["MT_pre__cardinality"] = """

return True
"""
        self.vs[3]["MT_label__"] = """2"""
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__name"] = """

return True
"""
        self.vs[3]["GUID__"] = 2056133774871146816
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["mm__"] = """MT_pre__MatchModel"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = 4699185555220633200
        self.vs[5]["MT_label__"] = """4"""
        self.vs[5]["mm__"] = """MT_pre__MatchModel"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = 1687034107671583005

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


    def eval_cardinality1(self, attr_value, this):
        
        
        return True


    def eval_name1(self, attr_value, this):
        
        
        return True


    def eval_classtype2(self, attr_value, this):
        
        
        return True


    def eval_cardinality2(self, attr_value, this):
        
        
        return True


    def eval_name2(self, attr_value, this):
        
        
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        
        guid1 = PreNode('1').index
        guid2 = PreNode('2').index
        
        matchModel1ID = PreNode('3').index
        matchModel2ID = PreNode('4').index
        
        if PreNode('1')['classtype'] == PreNode('2')['classtype'] and int(guid1) < int(guid2) and int(matchModel1ID) < int(matchModel2ID):
            return True
        return False

