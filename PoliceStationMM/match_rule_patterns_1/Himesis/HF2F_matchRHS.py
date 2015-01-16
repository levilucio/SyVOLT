

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HF2F_matchRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F_matchRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F_matchRHS, self).__init__(name='HF2F_matchRHS', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(10, 13), (5, 13), (11, 14), (2, 14), (4, 0), (0, 8), (6, 1), (1, 8), (3, 2), (3, 5), (4, 9), (12, 6), (6, 11), (9, 7), (7, 12), (8, 10)])
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
        self["GUID__"] = UUID('c76282fd-4668-474c-bb6d-7ace413728ac')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """14"""
        self.vs[0]["mm__"] = """MT_post__match_contains"""
        self.vs[0]["GUID__"] = UUID('2982577c-f8da-4c9e-8842-e3ce9a1858b2')
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["mm__"] = """MT_post__trace_link"""
        self.vs[1]["GUID__"] = UUID('3f630b12-3334-4219-9896-7b3ae46609ef')
        self.vs[2]["MT_label__"] = """11"""
        self.vs[2]["mm__"] = """MT_post__rightExpr"""
        self.vs[2]["GUID__"] = UUID('37f4dc2b-458c-4324-9870-d6fbddf26d62')
        self.vs[3]["MT_label__"] = """9"""
        self.vs[3]["mm__"] = """MT_post__Equation"""
        self.vs[3]["GUID__"] = UUID('15a1c108-d652-4b12-a85e-43dff6a438f1')
        self.vs[4]["MT_label__"] = """12"""
        self.vs[4]["mm__"] = """MT_post__MatchModel"""
        self.vs[4]["GUID__"] = UUID('61af8648-0435-4288-b7fe-38acd75306f3')
        self.vs[5]["MT_label__"] = """10"""
        self.vs[5]["mm__"] = """MT_post__leftExpr"""
        self.vs[5]["GUID__"] = UUID('3076fe2e-1ac1-4718-8a7b-940a659d1802')
        self.vs[6]["MT_label__"] = """4"""
        self.vs[6]["MT_post__name"] = """
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
        self.vs[6]["mm__"] = """MT_post__Female_T"""
        self.vs[6]["MT_post__classtype"] = """
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
        self.vs[6]["GUID__"] = UUID('28f79675-43bf-40df-9232-f3c2bc13a9ac')
        self.vs[7]["MT_label__"] = """13"""
        self.vs[7]["mm__"] = """MT_post__ApplyModel"""
        self.vs[7]["GUID__"] = UUID('7a2386ec-237d-4675-b70e-6b0236d89e6d')
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
        self.vs[8]["mm__"] = """MT_post__Female_S"""
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
        self.vs[8]["GUID__"] = UUID('8fbae60e-2aba-4cc1-a22b-9c434dd11772')
        self.vs[9]["MT_label__"] = """16"""
        self.vs[9]["mm__"] = """MT_post__paired_with"""
        self.vs[9]["GUID__"] = UUID('51f5381e-39af-42c2-acd5-9dff194e5aed')
        self.vs[10]["MT_label__"] = """7"""
        self.vs[10]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[10]["GUID__"] = UUID('a9e269e4-c256-4d55-9f45-9881ac2a5f59')
        self.vs[11]["MT_label__"] = """8"""
        self.vs[11]["mm__"] = """MT_post__hasAttr_T"""
        self.vs[11]["GUID__"] = UUID('5cc554b8-6a39-4192-a84b-37603c2b51df')
        self.vs[12]["MT_label__"] = """15"""
        self.vs[12]["mm__"] = """MT_post__apply_contains"""
        self.vs[12]["GUID__"] = UUID('da05d5dd-b2d6-47b7-a666-0ae898119c54')
        self.vs[13]["MT_label__"] = """2"""
        self.vs[13]["MT_post__name"] = """
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
        self.vs[13]["mm__"] = """MT_post__Attribute"""
        self.vs[13]["GUID__"] = UUID('587f7a9d-84a7-4158-a92d-e828cc7c8654')
        self.vs[14]["MT_label__"] = """5"""
        self.vs[14]["MT_post__name"] = """
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

return "name"
"""
        self.vs[14]["mm__"] = """MT_post__Attribute"""
        self.vs[14]["GUID__"] = UUID('90e1c983-3612-4358-b91a-7dc567a6aa30')

        from HF2F_matchLHS import HF2F_matchLHS
        self.pre = HF2F_matchLHS()
    
    def set_name5(self, attr_value, PreNode, graph):
        
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
        
        return "name"


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
        # Attribute5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        try:
            graph.vs[new_node]['name'] = self.set_name5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # match_contains14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # trace_link3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # rightExpr11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # MatchModel12
        new_node = graph.add_node()
        labels['12'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # leftExpr10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Female_T4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Female_T'
        # ApplyModel13
        new_node = graph.add_node()
        labels['13'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # paired_with16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # hasAttr_T8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_T'
        # apply_contains15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # leftExpr10 -> Attribute2
        graph.add_edges((labels['10'], labels['2']))
        # Equation9 -> leftExpr10
        graph.add_edges((labels['9'], labels['10']))
        # rightExpr11 -> Attribute5
        graph.add_edges((labels['11'], labels['5']))
        # Equation9 -> rightExpr11
        graph.add_edges((labels['9'], labels['11']))
        # MatchModel12 -> match_contains14
        graph.add_edges((labels['12'], labels['14']))
        # MatchModel12 -> paired_with16
        graph.add_edges((labels['12'], labels['16']))
        # paired_with16 -> ApplyModel13
        graph.add_edges((labels['16'], labels['13']))
        # ApplyModel13 -> apply_contains15
        graph.add_edges((labels['13'], labels['15']))
        # match_contains14 -> Female_S1
        graph.add_edges((labels['14'], labels['1']))
        # apply_contains15 -> Female_T4
        graph.add_edges((labels['15'], labels['4']))
        # Female_T4 -> trace_link3
        graph.add_edges((labels['4'], labels['3']))
        # trace_link3 -> Female_S1
        graph.add_edges((labels['3'], labels['1']))
        # Female_T4 -> hasAttr_T8
        graph.add_edges((labels['4'], labels['8']))
        # hasAttr_T8 -> Attribute5
        graph.add_edges((labels['8'], labels['5']))
        
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
    
