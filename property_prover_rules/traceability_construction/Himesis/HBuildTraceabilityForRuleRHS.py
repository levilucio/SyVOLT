

from core.himesis import Himesis, HimesisPostConditionPattern

class HBuildTraceabilityForRuleRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBuildTraceabilityForRuleRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBuildTraceabilityForRuleRHS, self).__init__(name='HBuildTraceabilityForRuleRHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 1], [2, 1], [3, 2], [6, 3], [5, 6]])
        # Set the graph attributes
        self["mm__"] = ['MT_post__FamiliesToPersons_MM', 'MoTifRule']
        self["name"] = """"""
        self["MT_action__"] = """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""
        self["superclasses_dict"] = {'Community': ['MetaModelElement_T'], 'Parent': ['Member', 'MetaModelElement_S'], 'TownHall': ['MetaModelElement_T', 'NamedElement'], 'Facility': ['MetaModelElement_T', 'NamedElement'], 'SpecialFacility': ['MetaModelElement_T', 'NamedElement', 'Facility'], 'NamedElement': ['MetaModelElement_T', 'MetaModelElement_S'], 'Association': ['MetaModelElement_T', 'NamedElement'], 'Neighborhood': ['MetaModelElement_S'], 'District': ['MetaModelElement_T', 'NamedElement'], 'Committee': ['MetaModelElement_T', 'NamedElement'], 'Company': ['MetaModelElement_S'], 'City': ['MetaModelElement_S'], 'Service': ['MetaModelElement_S'], 'Man': ['Person', 'MetaModelElement_T'], 'Person': ['MetaModelElement_T'], 'Country': ['MetaModelElement_S'], 'Member': ['MetaModelElement_S'], 'Woman': ['Person', 'MetaModelElement_T'], 'Child': ['Member', 'MetaModelElement_S'], 'School': ['MetaModelElement_S'], 'OrdinaryFacility': ['MetaModelElement_T', 'NamedElement', 'Facility'], 'Family': ['MetaModelElement_S']}
        self["GUID__"] = 7298637889829306927
        self["equations"] = []
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MT_post__match_contains"""
        self.vs[0]["GUID__"] = 2129491675721903084
        self.vs[0]["MT_label__"] = """5"""
        self.vs[1]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[1]["GUID__"] = 5689208472773641533
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
        self.vs[1]["MT_label__"] = """1"""
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["GUID__"] = 7158037091990660655
        self.vs[2]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_post__MetaModelElement_T"""
        self.vs[3]["GUID__"] = 3210421936718083316
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
        self.vs[3]["MT_label__"] = """2"""
        self.vs[4]["mm__"] = """MT_post__MatchModel"""
        self.vs[4]["GUID__"] = 5423360042570371497
        self.vs[4]["MT_label__"] = """3"""
        self.vs[5]["mm__"] = """MT_post__ApplyModel"""
        self.vs[5]["GUID__"] = 7341201780561851443
        self.vs[5]["MT_label__"] = """4"""
        self.vs[6]["mm__"] = """MT_post__apply_contains"""
        self.vs[6]["GUID__"] = 6622716255487794805
        self.vs[6]["MT_label__"] = """6"""

        try:
            from .HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
        except Exception:
            from HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
        self.pre = HBuildTraceabilityForRuleLHS()
    
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
        
        # trace_link10
        labels['10'] = node_num
        vs[node_num]["mm__"] = 'trace_link'
        vs[node_num]['GUID__'] = nprnd.randint(9223372036854775806)
        
        node_num += 1
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        graph.add_edges([
        # trace_link10 -> MetaModelElement_S1
        (labels['10'], labels['1']),
        # MetaModelElement_T2 -> trace_link10
        (labels['2'], labels['10']),
        ])
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        
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
    
