

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HSF2SF_matchRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_matchRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_matchRHS, self).__init__(name='HSF2SF_matchRHS', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 8), (2, 10), (10, 1), (5, 0), (0, 4), (5, 11), (11, 8), (4, 12), (12, 1), (3, 1), (2, 7), (8, 3), (14, 4), (13, 5), (7, 6), (6, 13), (6, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__PoliceStationMM'
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
        self["GUID__"] = UUID('f0bec048-4827-402b-aa35-d750d2d48f44')
        
        # Set the node attributes
        self.vs[0]["MT_post__associationType"] = """
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
        self.vs[0]["MT_label__"] = """11"""
        self.vs[0]["mm__"] = """MT_post__directLink_T"""
        self.vs[0]["GUID__"] = UUID('8eeaea5e-975c-4b5a-989a-e796e6a05e71')
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
        self.vs[1]["MT_label__"] = """2"""
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
        self.vs[1]["mm__"] = """MT_post__Female_S"""
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
        self.vs[1]["GUID__"] = UUID('3413a175-a002-4cf2-8adb-5542b532f012')
        self.vs[2]["MT_label__"] = """12"""
        self.vs[2]["mm__"] = """MT_post__MatchModel"""
        self.vs[2]["GUID__"] = UUID('b0a242aa-84b9-489c-af24-ee32149194d6')
        self.vs[3]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_post__indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('af4877ec-ad67-43da-be4b-e10e42b45721')
        self.vs[4]["MT_label__"] = """4"""
        self.vs[4]["MT_post__name"] = """
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
        self.vs[4]["mm__"] = """MT_post__Female_T"""
        self.vs[4]["MT_post__classtype"] = """
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
        self.vs[4]["GUID__"] = UUID('5fcee4ae-dcfb-4cf0-8bf6-facfe7f28f7b')
        self.vs[5]["MT_label__"] = """3"""
        self.vs[5]["MT_post__name"] = """
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
        self.vs[5]["mm__"] = """MT_post__Station_T"""
        self.vs[5]["MT_post__classtype"] = """
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
        self.vs[5]["GUID__"] = UUID('72e4cc51-2ec0-497e-87e8-1fca2cdf938f')
        self.vs[6]["MT_label__"] = """13"""
        self.vs[6]["mm__"] = """MT_post__ApplyModel"""
        self.vs[6]["GUID__"] = UUID('4fd380b0-a799-4b41-8708-5333fdbe306f')
        self.vs[7]["MT_label__"] = """18"""
        self.vs[7]["mm__"] = """MT_post__paired_with"""
        self.vs[7]["GUID__"] = UUID('268a2a28-5c4a-49ce-b33e-2ba38c5fc3a8')
        self.vs[8]["MT_post__cardinality"] = """
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
        self.vs[8]["MT_label__"] = """1"""
        self.vs[8]["MT_post__name"] = """
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
        self.vs[8]["mm__"] = """MT_post__Station_S"""
        self.vs[8]["MT_post__classtype"] = """
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
        self.vs[8]["GUID__"] = UUID('3e9b0688-eb10-4ced-9dd7-ccf8342e1d9c')
        self.vs[9]["MT_label__"] = """14"""
        self.vs[9]["mm__"] = """MT_post__match_contains"""
        self.vs[9]["GUID__"] = UUID('fe9efd72-eeee-40e8-9674-a965bcfc781c')
        self.vs[10]["MT_label__"] = """15"""
        self.vs[10]["mm__"] = """MT_post__match_contains"""
        self.vs[10]["GUID__"] = UUID('1b8c1ffe-4775-49f8-8616-2aaf38553087')
        self.vs[11]["MT_label__"] = """5"""
        self.vs[11]["mm__"] = """MT_post__trace_link"""
        self.vs[11]["GUID__"] = UUID('31b1a395-bcba-4794-9816-d0eb06ec0e38')
        self.vs[12]["MT_label__"] = """6"""
        self.vs[12]["mm__"] = """MT_post__trace_link"""
        self.vs[12]["GUID__"] = UUID('187a69b9-d370-4b5d-9e32-ddff1f5fd3d9')
        self.vs[13]["MT_label__"] = """16"""
        self.vs[13]["mm__"] = """MT_post__apply_contains"""
        self.vs[13]["GUID__"] = UUID('28a15359-d992-4410-b7ff-bb33e6ba89c2')
        self.vs[14]["MT_label__"] = """17"""
        self.vs[14]["mm__"] = """MT_post__apply_contains"""
        self.vs[14]["GUID__"] = UUID('3296fce3-a988-4bbd-914a-4091aa68e25c')

        from HSF2SF_matchLHS import HSF2SF_matchLHS
        self.pre = HSF2SF_matchLHS()
    
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
        # match_contains14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # match_contains15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # directLink_T11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # MatchModel12
        new_node = graph.add_node()
        labels['12'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # ApplyModel13
        new_node = graph.add_node()
        labels['13'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # paired_with18
        new_node = graph.add_node()
        labels['18'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # apply_contains16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains17
        new_node = graph.add_node()
        labels['17'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Station_T3 -> directLink_T11
        graph.add_edges((labels['3'], labels['11']))
        # directLink_T11 -> Female_T4
        graph.add_edges((labels['11'], labels['4']))
        # MatchModel12 -> match_contains14
        graph.add_edges((labels['12'], labels['14']))
        # MatchModel12 -> match_contains15
        graph.add_edges((labels['12'], labels['15']))
        # MatchModel12 -> paired_with18
        graph.add_edges((labels['12'], labels['18']))
        # paired_with18 -> ApplyModel13
        graph.add_edges((labels['18'], labels['13']))
        # ApplyModel13 -> apply_contains16
        graph.add_edges((labels['13'], labels['16']))
        # ApplyModel13 -> apply_contains17
        graph.add_edges((labels['13'], labels['17']))
        # match_contains14 -> Station_S1
        graph.add_edges((labels['14'], labels['1']))
        # match_contains15 -> Female_S2
        graph.add_edges((labels['15'], labels['2']))
        # apply_contains16 -> Station_T3
        graph.add_edges((labels['16'], labels['3']))
        # apply_contains17 -> Female_T4
        graph.add_edges((labels['17'], labels['4']))
        
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
    
