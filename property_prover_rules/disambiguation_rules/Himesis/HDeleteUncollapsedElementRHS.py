

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

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
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__UMLRT2Kiltera_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""
        self["name"] = """"""
        self["GUID__"] = 7812174363778671626
        
        # Set the node attributes
        self.vs[0]["MT_pivotOut__"] = """element1"""
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
        self.vs[0]["MT_label__"] = """1"""
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
        self.vs[0]["mm__"] = """MT_post__MetaModelElement_S"""
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
        self.vs[0]["GUID__"] = 6268035427006317116
        self.vs[1]["MT_label__"] = """5"""
        self.vs[1]["mm__"] = """MT_post__match_contains"""
        self.vs[1]["GUID__"] = 249157694221731772
        self.vs[2]["MT_label__"] = """6"""
        self.vs[2]["mm__"] = """MT_post__match_contains"""
        self.vs[2]["GUID__"] = 4053263962751487492
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["mm__"] = """MT_post__MatchModel"""
        self.vs[3]["GUID__"] = 3509172987562613612
        self.vs[4]["MT_label__"] = """4"""
        self.vs[4]["mm__"] = """MT_post__MatchModel"""
        self.vs[4]["GUID__"] = 8167246094907919532

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
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        
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
        except Exception, e:
            raise Exception('An error has occurred while applying the post-action', e)
        #===============================================================================
        # Finally, delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        # MT_pre__MetaModelElement_S2
        graph.delete_nodes([labels["2"]])
    
