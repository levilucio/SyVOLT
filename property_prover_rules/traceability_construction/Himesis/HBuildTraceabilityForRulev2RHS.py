

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HBuildTraceabilityForRulev2RHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBuildTraceabilityForRulev2RHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBuildTraceabilityForRulev2RHS, self).__init__(name='HBuildTraceabilityForRulev2RHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 1), (2, 1), (3, 2), (6, 3), (5, 6)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__GM2AUTOSAR_MM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = pickle.loads("""Vif set([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'trace_link'])) == set():\u000a    return True\u000a\u000areturn False\u000a
p1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('8783d80d-d447-4cb4-a14f-a628ffd8908f')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MT_post__match_contains"""
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["GUID__"] = UUID('9af9f313-6d30-45d9-9af1-c65dcb5d6988')
        self.vs[1]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["MT_post__attr2"] = """
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
        self.vs[1]["GUID__"] = UUID('2b0899ef-66c8-4cc5-ba18-28d4dd765887')
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["MT_label__"] = """7"""
        self.vs[2]["GUID__"] = UUID('25de610b-6c3b-4e7c-bd71-13fcd3bd23b4')
        self.vs[3]["mm__"] = """MT_post__MetaModelElement_T"""
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["MT_post__attr2"] = """
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
        self.vs[3]["GUID__"] = UUID('d8b6dcf9-49e0-49ea-86e9-be9a220e77ad')
        self.vs[4]["mm__"] = """MT_post__MatchModel"""
        self.vs[4]["MT_label__"] = """1"""
        self.vs[4]["GUID__"] = UUID('d122e03d-2708-4855-826d-15b29cb835b6')
        self.vs[5]["mm__"] = """MT_post__ApplyModel"""
        self.vs[5]["MT_label__"] = """2"""
        self.vs[5]["GUID__"] = UUID('2a25df3d-d291-4218-8e1f-374a9c300424')
        self.vs[6]["mm__"] = """MT_post__apply_contains"""
        self.vs[6]["MT_label__"] = """6"""
        self.vs[6]["GUID__"] = UUID('dd8a143e-d989-43f8-a753-fc4560b50955')

        from HBuildTraceabilityForRulev2LHS import HBuildTraceabilityForRulev2LHS
        self.pre = HBuildTraceabilityForRulev2LHS()
    
    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        if set([i for i in graph.neighbors(PreNode('1').index) if graph.vs[i]['mm__'] == 'trace_link']).intersection(set([i for i in graph.neighbors(PreNode('2').index) if graph.vs[i]['mm__'] == 'trace_link'])) == set():
            return True
        
        return False

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
        # trace_link7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # trace_link7 -> MetaModelElement_S3
        graph.add_edges((labels['7'], labels['3']))
        # MetaModelElement_T4 -> trace_link7
        graph.add_edges((labels['4'], labels['7']))
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        
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
    
