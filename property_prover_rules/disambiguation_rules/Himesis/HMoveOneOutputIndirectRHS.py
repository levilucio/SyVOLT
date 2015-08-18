

from core.himesis import Himesis, HimesisPostConditionPattern

class HMoveOneOutputIndirectRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneOutputIndirectRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneOutputIndirectRHS, self).__init__(name='HMoveOneOutputIndirectRHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[1, 0], [0, 3]])
        # Set the graph attributes
        self["mm__"] = ['MT_post__mbeddr', 'MoTifRule']
        self["MT_action__"] = """PostNode('19')['associationType'] = PostNode('9')['associationType']
"""
        self["superclasses_dict"] = {'FunctionRefType': ['MetaModelElement_T'], 'NumericLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'ExpressionStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'TestCaseRef': ['MetaModelElement_S'], 'PrimitiveType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapterRefExpr': ['MetaModelElement_S'], 'ReturnStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'Statement': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssemblyConnector': ['MetaModelElement_S'], 'CFunctionPointerStructMember': ['MetaModelElement_T'], 'PortAdapter': ['MetaModelElement_S'], 'ModuleContentSUDeclaration': ['MetaModelElement_T'], 'FunctionSignature': ['MetaModelElement_T', 'MetaModelElement_S'], 'StatementList': ['MetaModelElement_T', 'MetaModelElement_S'], 'BinaryComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationTrigger': ['MetaModelElement_S'], 'SUType': ['MetaModelElement_T'], 'Int32Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'InterfaceOperationCallExpr': ['MetaModelElement_S'], 'SUContent': ['MetaModelElement_T'], 'PointerType': ['MetaModelElement_T'], 'Operation': ['MetaModelElement_S'], 'GlobalVariableDeclaration': ['MetaModelElement_T'], 'PortRef': ['MetaModelElement_S'], 'StructDeclaration': ['MetaModelElement_T'], 'PortRefExpr': ['MetaModelElement_S'], 'Type': ['MetaModelElement_T', 'MetaModelElement_S'], 'StringType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PointerExpr': ['MetaModelElement_T'], 'PlusExpression': ['MetaModelElement_S'], 'AbstractInstanceConfiguration': ['MetaModelElement_S'], 'Interface': ['MetaModelElement_S'], 'IType': ['MetaModelElement_T'], 'GreaterEqualsExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'ArgumentRef': ['MetaModelElement_S'], 'ITypeContainingType': ['MetaModelElement_T', 'MetaModelElement_S'], 'ITyped': ['MetaModelElement_T', 'MetaModelElement_S'], 'Argument': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionCall': ['MetaModelElement_T'], 'SUDeclaration': ['MetaModelElement_T'], 'DerefExpr': ['MetaModelElement_T'], 'ExecuteTestExpression': ['MetaModelElement_S'], 'Member': ['MetaModelElement_T'], 'Literal': ['MetaModelElement_T', 'MetaModelElement_S'], 'IArgumentLike': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionRefExpr': ['MetaModelElement_T'], 'AdapterInstancePortRef': ['MetaModelElement_S'], 'InstancePortRef': ['MetaModelElement_S'], 'ICanBeExecutedAsTest': ['MetaModelElement_S'], 'RequiredPort': ['MetaModelElement_S'], 'LocalVarRef': ['MetaModelElement_S'], 'CModule': ['MetaModelElement_T'], 'IModuleContent': ['MetaModelElement_T', 'MetaModelElement_S'], 'AssignmentExpr': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeWithDeclaration': ['MetaModelElement_T'], 'StructType': ['MetaModelElement_T'], 'AtomicComponent': ['MetaModelElement_S'], 'InstanceConfiguration': ['MetaModelElement_S'], 'NumberLiteral': ['MetaModelElement_T', 'MetaModelElement_S'], 'OperationParameter': ['MetaModelElement_S'], 'InstanceConfigContents': ['MetaModelElement_S'], 'GlobalVarRef': ['MetaModelElement_T'], 'BinaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'Expression': ['MetaModelElement_T', 'MetaModelElement_S'], 'LocalVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'UnaryExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'VoidType': ['MetaModelElement_T', 'MetaModelElement_S'], 'WhileStatement': ['MetaModelElement_T', 'MetaModelElement_S'], 'StringLiteral': ['MetaModelElement_S'], 'ProvidedPort': ['MetaModelElement_S'], 'Prefix': ['MetaModelElement_T'], 'MbeddrModule': ['MetaModelElement_S'], 'ImplementationModule': ['MetaModelElement_T', 'MetaModelElement_S'], 'Executable': ['MetaModelElement_S'], 'CastExpression': ['MetaModelElement_T'], 'GenericDotExpression': ['MetaModelElement_T'], 'IGenericDotTarget': ['MetaModelElement_T'], 'ArrayType': ['MetaModelElement_T', 'MetaModelElement_S'], 'PrimitiveC99IntegralType': ['MetaModelElement_T', 'MetaModelElement_S'], 'IIdentifierNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortAdapterOpCallExpr': ['MetaModelElement_S'], 'IVariableDeclaration': ['MetaModelElement_T', 'MetaModelElement_S'], 'Function': ['MetaModelElement_T', 'MetaModelElement_S'], 'IControlledNamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'FunctionPrototype': ['MetaModelElement_T'], 'Component': ['MetaModelElement_S'], 'TestCase': ['MetaModelElement_S'], 'RunnableTrigger': ['MetaModelElement_S'], 'BinaryArithmeticExpression': ['MetaModelElement_S'], 'ComponentInstance': ['MetaModelElement_S'], 'GenericMemberRef': ['MetaModelElement_T'], 'ICSInterfaceContents': ['MetaModelElement_S'], 'ReferenceExpr': ['MetaModelElement_T'], 'RequiredPortOpCallExpr': ['MetaModelElement_S'], 'BinaryOrderedComparisonExpression': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeDefType': ['MetaModelElement_T'], 'IComponentContent': ['MetaModelElement_S'], 'INamedConcept': ['MetaModelElement_T', 'MetaModelElement_S'], 'TypeDef': ['MetaModelElement_T'], 'IOperationTriggerLike': ['MetaModelElement_S'], 'InitializeConfiguration': ['MetaModelElement_S'], 'ClientServerInterface': ['MetaModelElement_S'], 'IModuleContentContainer': ['MetaModelElement_T', 'MetaModelElement_S'], 'IHasPrefixes': ['MetaModelElement_T'], 'Port': ['MetaModelElement_S'], 'IFunctionLike': ['MetaModelElement_T', 'MetaModelElement_S']}
        self["name"] = """"""
        self["GUID__"] = 7221155243241900300
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """7"""
        self.vs[0]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[0]["GUID__"] = 8983501963842356629
        self.vs[1]["MT_pivotOut__"] = """element1"""
        self.vs[1]["MT_post__attr1"] = """
#===============================================================================
# You can access the value of the current node's attribute value by: attr_value.
# If the current node shall be created you MUST initialize it here!
# You can access a node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# Note that the attribute values are those before the match is rewritten.
# The order in which this code is executed depends on the label value
# of the encapsulating node.
# The given action must return the new value of the attribute.
#===============================================================================

return attr_value
"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[1]["GUID__"] = 1212754244606261678
        self.vs[2]["MT_pivotOut__"] = """element2"""
        self.vs[2]["MT_post__attr1"] = """
#===============================================================================
# You can access the value of the current node's attribute value by: attr_value.
# If the current node shall be created you MUST initialize it here!
# You can access a node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# Note that the attribute values are those before the match is rewritten.
# The order in which this code is executed depends on the label value
# of the encapsulating node.
# The given action must return the new value of the attribute.
#===============================================================================

return attr_value
"""
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[2]["GUID__"] = 424706264847277057
        self.vs[3]["MT_post__attr1"] = """
#===============================================================================
# You can access the value of the current node's attribute value by: attr_value.
# If the current node shall be created you MUST initialize it here!
# You can access a node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# Note that the attribute values are those before the match is rewritten.
# The order in which this code is executed depends on the label value
# of the encapsulating node.
# The given action must return the new value of the attribute.
#===============================================================================

return attr_value
"""
        self.vs[3]["MT_label__"] = """5"""
        self.vs[3]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[3]["GUID__"] = 1746090873004102793

        try:
            from .HMoveOneOutputIndirectLHS import HMoveOneOutputIndirectLHS
        except Exception:
            from HMoveOneOutputIndirectLHS import HMoveOneOutputIndirectLHS
        self.pre = HMoveOneOutputIndirectLHS()
    
    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        PostNode('19')['associationType'] = PostNode('9')['associationType']

    def execute(self, packet, match):
        """
            Transforms the current match of the packet according to the rule %s.
            Pivots are also assigned, if any.
            @param packet: The input packet.
            @param match: The match to rewrite.
        """
        graph = packet.graph
        
        vs = graph.vs
        
        import numpy.random as nprnd
        
        # Build a dictionary {label: node index} mapping each label of the pattern to a node in the graph to rewrite.
        # Because of the uniqueness property of labels in a rule, we can store all LHS labels
        # and subsequently add the labels corresponding to the nodes to be created.
        labels = match.copy()
        
        #===============================================================================
        # Update attribute values
        #===============================================================================
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        
        node_num = graph.vcount()
        
        graph.add_vertices(1)
        
        # indirectLink_S7
        labels['7'] = node_num
        vs[node_num]["mm__"] = 'indirectLink_S'
        vs[node_num]['GUID__'] = nprnd.randint(9223372036854775806)
        
        node_num += 1
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        graph.add_edges([
        # MetaModelElement_S3 -> indirectLink_S7
        (labels['3'], labels['7']),
        # indirectLink_S7 -> MetaModelElement_S5
        (labels['7'], labels['5']),
        ])
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        # MetaModelElement_S3
        packet.global_pivots['element1'] = graph.vs[labels['3']][Himesis.Constants.GUID]
        # MetaModelElement_S4
        packet.global_pivots['element2'] = graph.vs[labels['4']][Himesis.Constants.GUID]
        
        #===============================================================================
        # Perform the post-action
        #===============================================================================
        try:
            self.action(lambda i: graph.vs[labels[i]], graph)
        except Exception as e:
            raise Exception('An error has occurred while applying the post-action', e)
        #===============================================================================
        # Finally, delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        # MT_pre__indirectLink_S6
        graph.delete_nodes(labels["6"])
    
