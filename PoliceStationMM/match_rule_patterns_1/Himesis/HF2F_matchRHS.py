

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
        
        super(HF2F_matchRHS, self).__init__(name='HF2F_matchRHS', num_nodes=10, edges=[])
        
        # Add the edges
        self.add_edges([(6, 8), (3, 8), (7, 9), (0, 9), (1, 0), (1, 3), (4, 2), (2, 5), (4, 7), (5, 6)])
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
        self["GUID__"] = UUID('7173567c-2013-4ae0-8933-9a3d40f66e0e')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """11"""
        self.vs[0]["mm__"] = """MT_post__rightExpr"""
        self.vs[0]["GUID__"] = UUID('54fa361b-4482-4d5a-8d93-a83ad51c6806')
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_post__Equation"""
        self.vs[1]["GUID__"] = UUID('a507769e-0f86-411e-8321-e6eb51c62768')
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["GUID__"] = UUID('022b3fee-b660-49fd-a424-1628fd5718c2')
        self.vs[3]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_post__leftExpr"""
        self.vs[3]["GUID__"] = UUID('4a548aa2-e559-431b-a0fb-2d7506e6b663')
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
        self.vs[4]["GUID__"] = UUID('a83e520c-415b-4b3c-8040-02e10215ce87')
        self.vs[5]["MT_post__cardinality"] = """
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
        self.vs[5]["MT_label__"] = """1"""
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
        self.vs[5]["mm__"] = """MT_post__Female_S"""
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
        self.vs[5]["GUID__"] = UUID('8d885af0-4943-4954-a056-985a5331f6a5')
        self.vs[6]["MT_label__"] = """7"""
        self.vs[6]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[6]["GUID__"] = UUID('6a296e31-6eac-4322-bccc-469bf809f25d')
        self.vs[7]["MT_label__"] = """8"""
        self.vs[7]["mm__"] = """MT_post__hasAttr_T"""
        self.vs[7]["GUID__"] = UUID('f182d233-fdee-41ce-9722-db97eed08a3c')
        self.vs[8]["MT_label__"] = """2"""
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
        self.vs[8]["mm__"] = """MT_post__Attribute"""
        self.vs[8]["GUID__"] = UUID('9a7d3aea-3abd-4605-bd01-8e9cfa38487f')
        self.vs[9]["MT_label__"] = """5"""
        self.vs[9]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value\u000a# of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn "name"\u000a
p1
.""")
        self.vs[9]["mm__"] = """MT_post__Attribute"""
        self.vs[9]["GUID__"] = UUID('a3eb760d-93d5-426c-a527-734441aec25e')

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
        # rightExpr11
        new_node = graph.add_node()
        labels['11'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # trace_link3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # leftExpr10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Female_T4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Female_T'
        # hasAttr_T8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_T'
        
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
    
