

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
        
        super(HF2F_matchRHS, self).__init__(name='HF2F_matchRHS', num_nodes=9, edges=[])
        
        # Add the edges
        self.add_edges([(7, 0), (4, 0), (2, 1), (1, 8), (2, 4), (5, 3), (3, 6), (6, 7)])
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
        self["GUID__"] = UUID('d3f2e64e-5697-4c51-baa0-30257384bba5')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """2"""
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
        self.vs[0]["mm__"] = """MT_post__Attribute"""
        self.vs[0]["GUID__"] = UUID('201431c9-2ffb-4c68-a598-69fda55b149a')
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_post__rightExpr"""
        self.vs[1]["GUID__"] = UUID('b4a9d424-be51-4ce3-9ced-09c3df7b65a3')
        self.vs[2]["MT_label__"] = """6"""
        self.vs[2]["mm__"] = """MT_post__Equation"""
        self.vs[2]["GUID__"] = UUID('f7ee4663-4c65-44ad-87a1-b968d7f1ef7b')
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["mm__"] = """MT_post__trace_link"""
        self.vs[3]["GUID__"] = UUID('2aeb77d8-a00b-426c-b5dc-4708481939e1')
        self.vs[4]["MT_label__"] = """8"""
        self.vs[4]["mm__"] = """MT_post__leftExpr"""
        self.vs[4]["GUID__"] = UUID('f267e508-5714-443b-b1de-8f4be4401e70')
        self.vs[5]["MT_label__"] = """5"""
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
        self.vs[5]["mm__"] = """MT_post__Female_T"""
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
        self.vs[5]["GUID__"] = UUID('592a67e1-7acc-4fdf-9d86-d3de813b61eb')
        self.vs[6]["MT_post__cardinality"] = """
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
        self.vs[6]["MT_label__"] = """1"""
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
        self.vs[6]["mm__"] = """MT_post__Female_S"""
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
        self.vs[6]["GUID__"] = UUID('1c037de9-7a39-438e-a511-1b189e43db6c')
        self.vs[7]["MT_label__"] = """3"""
        self.vs[7]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[7]["GUID__"] = UUID('d030df8a-d851-4e01-8acf-4024ef31735f')
        self.vs[8]["MT_post__value"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value\u000a# of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn "otherfemale"\u000a
p1
.""")
        self.vs[8]["MT_label__"] = """7"""
        self.vs[8]["mm__"] = """MT_post__Constant"""
        self.vs[8]["GUID__"] = UUID('24eb43a8-68c4-45ec-9fa8-df4113a046ef')

        from HF2F_matchLHS import HF2F_matchLHS
        self.pre = HF2F_matchLHS()
    
    def set_value7(self, attr_value, PreNode, graph):
        
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
        
        return "otherfemale"


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
        # rightExpr9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # trace_link4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # leftExpr8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Female_T5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Female_T'
        # Constant7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['value'] = self.set_value7(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'value\'', e)
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Female_T5 -> trace_link4
        graph.add_edges((labels['5'], labels['4']))
        # trace_link4 -> Female_S1
        graph.add_edges((labels['4'], labels['1']))
        # Equation6 -> rightExpr9
        graph.add_edges((labels['6'], labels['9']))
        # Equation6 -> leftExpr8
        graph.add_edges((labels['6'], labels['8']))
        # rightExpr9 -> Constant7
        graph.add_edges((labels['9'], labels['7']))
        # leftExpr8 -> Attribute2
        graph.add_edges((labels['8'], labels['2']))
        
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
    
