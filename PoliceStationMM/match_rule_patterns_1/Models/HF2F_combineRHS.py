

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HF2F_combineRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F_combineRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F_combineRHS, self).__init__(name='HF2F_combineRHS', num_nodes=10, edges=[])
        
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
        self["GUID__"] = UUID('2c2e8f95-c8a0-4807-a5ae-2257e60070d6')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """11"""
        self.vs[0]["mm__"] = """MT_post__rightExpr"""
        self.vs[0]["GUID__"] = UUID('92e71c25-c498-41e7-8eae-0b0b6fbe4304')
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_post__Equation"""
        self.vs[1]["GUID__"] = UUID('bf15d85f-5472-4d38-97de-0ca0ed5e1a74')
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["mm__"] = """MT_post__trace_link"""
        self.vs[2]["GUID__"] = UUID('39e2f5c4-4da0-49b8-bce5-fdd9fa00884d')
        self.vs[3]["MT_label__"] = """10"""
        self.vs[3]["mm__"] = """MT_post__leftExpr"""
        self.vs[3]["GUID__"] = UUID('87c1f923-8f33-42cf-b83b-4da284abb2b5')
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
        self.vs[4]["GUID__"] = UUID('c5e4d9d2-aecc-4365-837c-2e9bc6e35c44')
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
        self.vs[5]["GUID__"] = UUID('78cb57a9-aebf-48e7-a297-a9c4c8cfdd20')
        self.vs[6]["MT_label__"] = """7"""
        self.vs[6]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[6]["GUID__"] = UUID('d4fce1b6-be7e-4b54-bf4e-d862015ae8a3')
        self.vs[7]["MT_label__"] = """8"""
        self.vs[7]["mm__"] = """MT_post__hasAttr_T"""
        self.vs[7]["GUID__"] = UUID('f59058e3-7205-4b3b-9c10-21e895d6c02c')
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
        self.vs[8]["GUID__"] = UUID('0529efe8-5a25-42e7-bffa-fdb8aa3f228f')
        self.vs[9]["MT_label__"] = """5"""
        self.vs[9]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value\u000a# of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn "name"\u000a
p1
.""")
        self.vs[9]["mm__"] = """MT_post__Attribute"""
        self.vs[9]["GUID__"] = UUID('829b4014-336f-4ef0-97ae-dc84ae08cfbd')

        from HF2F_combineLHS import HF2F_combineLHS
        self.pre = HF2F_combineLHS()
    
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
    
