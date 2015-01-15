

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HM2M_matchRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M_matchRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M_matchRHS, self).__init__(name='HM2M_matchRHS', num_nodes=10, edges=[])
        
        # Add the edges
        self.add_edges([(6, 8), (4, 8), (7, 9), (1, 9), (0, 3), (0, 7), (2, 1), (2, 4), (3, 5), (5, 6)])
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
        self["GUID__"] = UUID('3a873c8b-faf0-40cb-8965-5a8295c4051b')
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """4"""
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
        self.vs[0]["mm__"] = """MT_post__Male_T"""
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
        self.vs[0]["GUID__"] = UUID('e3b9b460-32b7-4d5b-8af4-670ce8c3f5f3')
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_post__rightExpr"""
        self.vs[1]["GUID__"] = UUID('a1c65942-57c5-4243-8211-78e556bff77f')
        self.vs[2]["MT_label__"] = """10"""
        self.vs[2]["mm__"] = """MT_post__Equation"""
        self.vs[2]["GUID__"] = UUID('ee4165ea-7bcc-4954-852f-06edbf8440ff')
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["mm__"] = """MT_post__trace_link"""
        self.vs[3]["GUID__"] = UUID('a9cad236-c0f7-4fc5-a5d9-4312a47675e5')
        self.vs[4]["MT_label__"] = """8"""
        self.vs[4]["mm__"] = """MT_post__leftExpr"""
        self.vs[4]["GUID__"] = UUID('3ac4ffab-e0c1-4ea4-b09d-a564bb12857a')
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
        self.vs[5]["mm__"] = """MT_post__Male_S"""
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
        self.vs[5]["GUID__"] = UUID('a4e0d50c-4782-40b1-9e59-6819465fc26e')
        self.vs[6]["MT_label__"] = """6"""
        self.vs[6]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[6]["GUID__"] = UUID('d89fd3a5-4389-4b31-b101-ca39ec049ba6')
        self.vs[7]["MT_label__"] = """7"""
        self.vs[7]["mm__"] = """MT_post__hasAttr_T"""
        self.vs[7]["GUID__"] = UUID('b3ee0900-32f4-449d-b4c8-af5516169bd2')
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
        self.vs[8]["GUID__"] = UUID('a132e619-2123-48d6-8281-27f82c453a0d')
        self.vs[9]["MT_label__"] = """5"""
        self.vs[9]["MT_post__name"] = """
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
        self.vs[9]["mm__"] = """MT_post__Attribute"""
        self.vs[9]["GUID__"] = UUID('ef7c1107-0492-49ea-a42d-424ca6da5f47')

        from HM2M_matchLHS import HM2M_matchLHS
        self.pre = HM2M_matchLHS()
    
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
        # Male_T4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Male_T'
        # rightExpr9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation10
        new_node = graph.add_node()
        labels['10'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # trace_link3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        # leftExpr8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # hasAttr_T7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttr_T'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Equation10 -> rightExpr9
        graph.add_edges((labels['10'], labels['9']))
        # Equation10 -> leftExpr8
        graph.add_edges((labels['10'], labels['8']))
        # Male_T4 -> trace_link3
        graph.add_edges((labels['4'], labels['3']))
        # trace_link3 -> Male_S1
        graph.add_edges((labels['3'], labels['1']))
        # Male_T4 -> hasAttr_T7
        graph.add_edges((labels['4'], labels['7']))
        # hasAttr_T7 -> Attribute5
        graph.add_edges((labels['7'], labels['5']))
        # rightExpr9 -> Attribute5
        graph.add_edges((labels['9'], labels['5']))
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
    
