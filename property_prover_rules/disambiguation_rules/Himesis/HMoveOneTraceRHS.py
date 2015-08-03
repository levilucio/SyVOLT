

from core.himesis import Himesis, HimesisPostConditionPattern

class HMoveOneTraceRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneTraceRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneTraceRHS, self).__init__(name='HMoveOneTraceRHS', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([[0, 2], [1, 0]])
        # Set the graph attributes
        self["name"] = """"""
        self["MT_action__"] = """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""
        self["mm__"] = ['MT_post__UMLRT2Kiltera_MM', 'MoTifRule']
        self["superclasses_dict"] = {'OPTIONAL1,': ['MetaModelElement_S'], 'Par': ['MetaModelElement_T'], 'NamedElement': ['MetaModelElement_S'], 'Pattern': ['MetaModelElement_T'], 'InitialPoint': ['MetaModelElement_S'], 'PortRef': ['MetaModelElement_S'], 'IN0': ['MetaModelElement_S'], 'OUT2': ['MetaModelElement_S'], 'MatchCase': ['MetaModelElement_T'], 'Site': ['MetaModelElement_T'], 'Delay': ['MetaModelElement_T'], 'Print': ['MetaModelElement_T'], 'State': ['MetaModelElement_S', 'StateMachine'], 'SignalType': ['MetaModelElement_S'], 'FuncDef': ['MetaModelElement_T'], 'New': ['MetaModelElement_T'], 'ExitPoint': ['MetaModelElement_S'], 'Proc': ['MetaModelElement_T'], 'Match': ['MetaModelElement_T'], 'Listen': ['MetaModelElement_T'], 'StateMachineElement': ['MetaModelElement_S'], 'Thread': ['MetaModelElement_S'], 'StateMachine': ['MetaModelElement_S'], 'TransitionType': ['MetaModelElement_S'], 'Vertex': ['MetaModelElement_S'], 'ListenBranch': ['MetaModelElement_T'], 'Capsule': ['MetaModelElement_S'], 'Trigger_S': ['MetaModelElement_S'], 'Inst': ['MetaModelElement_T'], 'LocalDef': ['MetaModelElement_T'], 'Trigger_T': ['MetaModelElement_T'], 'FIXED0': ['MetaModelElement_S'], 'LogicalThread': ['MetaModelElement_S'], 'Condition': ['MetaModelElement_T'], 'RoleType': ['MetaModelElement_S'], 'CONJUGATE1': ['MetaModelElement_S'], 'Transition': ['MetaModelElement_S'], 'Name': ['MetaModelElement_T'], 'PhysicalThread': ['MetaModelElement_S'], 'Package': ['MetaModelElement_S'], 'Expr': ['MetaModelElement_T'], 'Signal': ['MetaModelElement_S'], 'RootElement': ['MetaModelElement_T', 'MetaModelElement_S'], 'PortConnectorRef': ['MetaModelElement_S'], 'Element': ['MetaModelElement_S'], 'IN1': ['MetaModelElement_S'], 'Model_S': ['MetaModelElement_S'], 'Model_T': ['MetaModelElement_T'], 'PLUGIN2': ['MetaModelElement_S'], 'Action': ['MetaModelElement_S'], 'PortType': ['MetaModelElement_S'], 'SIBLING0': ['MetaModelElement_S'], 'PackageContainer': ['MetaModelElement_S'], 'Def': ['MetaModelElement_T'], 'CapsuleRole': ['MetaModelElement_S'], 'ProcDef': ['MetaModelElement_T'], 'Protocol': ['MetaModelElement_S'], 'Seq': ['MetaModelElement_T'], 'OUT1': ['MetaModelElement_S'], 'PythonRef': ['MetaModelElement_T'], 'ConditionSet': ['MetaModelElement_T'], 'Module': ['MetaModelElement_T'], 'BASE0': ['MetaModelElement_S'], 'EntryPoint': ['MetaModelElement_S'], 'ConditionBranch': ['MetaModelElement_T'], 'ParIndexed': ['MetaModelElement_T'], 'Null': ['MetaModelElement_T'], 'Port': ['MetaModelElement_S'], 'PortConnector': ['MetaModelElement_S']}
        self["equations"] = []
        self["GUID__"] = 9043970257047724692
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """20"""
        self.vs[0]["mm__"] = """MT_post__trace_link"""
        self.vs[0]["GUID__"] = 7601443841073304996
        self.vs[1]["MT_post__cardinality"] = """
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
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["MT_post__name"] = """
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
        self.vs[1]["mm__"] = """MT_post__MetaModelElement_T"""
        self.vs[1]["MT_post__classtype"] = """
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
        self.vs[1]["GUID__"] = 7803727040313128711
        self.vs[2]["MT_pivotOut__"] = """element1"""
        self.vs[2]["MT_post__cardinality"] = """
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
        self.vs[2]["MT_label__"] = """7"""
        self.vs[2]["MT_post__name"] = """
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
        self.vs[2]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[2]["MT_post__classtype"] = """
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
        self.vs[2]["GUID__"] = 2143674367009436808
        self.vs[3]["MT_pivotOut__"] = """element2"""
        self.vs[3]["MT_post__cardinality"] = """
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
        self.vs[3]["MT_label__"] = """8"""
        self.vs[3]["MT_post__name"] = """
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
        self.vs[3]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[3]["MT_post__classtype"] = """
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
        self.vs[3]["GUID__"] = 1164749033936639214

        try:
            from .HMoveOneTraceLHS import HMoveOneTraceLHS
        except Exception:
            from HMoveOneTraceLHS import HMoveOneTraceLHS
        self.pre = HMoveOneTraceLHS()
    
    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        #===============================================================================
        # This code is executed after the rule has been applied.
        # You can access a node labelled n matched by this rule by: PostNode('n').
        # To access attribute x of node n, use: PostNode('n')['x'].
        #===============================================================================
        
        pass

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
        
        # trace_link20
        labels['20'] = node_num
        vs[node_num]["mm__"] = 'trace_link'
        vs[node_num]['GUID__'] = nprnd.randint(9223372036854775806)
        
        node_num += 1
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        graph.add_edges([
        # trace_link20 -> MetaModelElement_S7
        (labels['20'], labels['7']),
        # MetaModelElement_T9 -> trace_link20
        (labels['9'], labels['20']),
        ])
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        # MetaModelElement_S7
        packet.global_pivots['element1'] = graph.vs[labels['7']][Himesis.Constants.GUID]
        # MetaModelElement_S8
        packet.global_pivots['element2'] = graph.vs[labels['8']][Himesis.Constants.GUID]
        
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
        # MT_pre__trace_link10
        graph.delete_nodes(labels["10"])
    
