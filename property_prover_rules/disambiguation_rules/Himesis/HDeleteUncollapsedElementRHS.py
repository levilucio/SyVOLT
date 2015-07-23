

from core.himesis import Himesis, HimesisPostConditionPattern

class HDeleteUncollapsedElementRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDeleteUncollapsedElementRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeleteUncollapsedElementRHS, self).__init__(name='HDeleteUncollapsedElementRHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([[3, 1], [1, 0], [4, 2], [2, 0]])
        # Set the graph attributes
        self["mm__"] = ['MT_post__FamiliesToPersons_MM', 'MoTifRule']
        self["superclasses_dict"] = {'Person': ['MetaModelElement_T'], 'Family': ['MetaModelElement_S'], 'Woman': ['MetaModelElement_T'], 'CommunityRoot': ['MetaModelElement_T'], 'Man': ['MetaModelElement_T'], 'HouseholdRoot': ['MetaModelElement_S'], 'Member': ['MetaModelElement_S']}
        self["equations"] = []
        self["name"] = """"""
        self["GUID__"] = 4361678906628492287
        self["MT_action__"] = """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_post__cardinality"] = """
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
        self.vs[0]["MT_post__classtype"] = """
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
        self.vs[0]["MT_pivotOut__"] = """element1"""
        self.vs[0]["GUID__"] = 1304423769433739448
        self.vs[0]["MT_post__name"] = """
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
        self.vs[1]["mm__"] = """MT_post__match_contains"""
        self.vs[1]["MT_label__"] = """5"""
        self.vs[1]["GUID__"] = 5925682644681422515
        self.vs[2]["mm__"] = """MT_post__match_contains"""
        self.vs[2]["MT_label__"] = """10"""
        self.vs[2]["GUID__"] = 6843251485065350586
        self.vs[3]["mm__"] = """MT_post__MatchModel"""
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["GUID__"] = 8836170241171624579
        self.vs[4]["mm__"] = """MT_post__MatchModel"""
        self.vs[4]["MT_label__"] = """4"""
        self.vs[4]["GUID__"] = 7649300617998864224

        try:
            from .HDeleteUncollapsedElementLHS import HDeleteUncollapsedElementLHS
        except Exception:
            from HDeleteUncollapsedElementLHS import HDeleteUncollapsedElementLHS
        self.pre = HDeleteUncollapsedElementLHS()
    
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
        # match_contains10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node]["mm__"] = 'match_contains'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        graph.add_edges([
        # MatchModel4 -> match_contains10
        (labels['4'], labels['10']),
        # match_contains10 -> MetaModelElement_S1
        (labels['10'], labels['1']),
        ])
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        # MetaModelElement_S1
        packet.global_pivots['element1'] = graph.vs[labels['1']][Himesis.Constants.GUID]
        
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
        # MT_pre__MetaModelElement_S2
        graph.delete_nodes(labels["2"])
        # MT_pre__match_contains6
        graph.delete_nodes(labels["6"])
    
