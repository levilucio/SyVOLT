

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HMoveOneEquationsLeftExpressionRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMoveOneEquationsLeftExpressionRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMoveOneEquationsLeftExpressionRHS, self).__init__(name='HMoveOneEquationsLeftExpressionRHS', num_nodes=8, edges=[])
        
        # Add the edges
        self.add_edges([[4, 2], [5, 3], [1, 3], [0, 1], [6, 4], [7, 5]])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__FamiliesToPersons_MM'
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
        self["GUID__"] = 1606133549215567614
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """7"""
        self.vs[0]["mm__"] = """MT_post__Equation"""
        self.vs[0]["GUID__"] = 5841559181534415960
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["mm__"] = """MT_post__leftExpr"""
        self.vs[1]["GUID__"] = 386197608977951647
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["MT_post__name"] = """
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
        self.vs[2]["mm__"] = """MT_post__Attribute"""
        self.vs[2]["GUID__"] = 5112429455430898355
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["MT_post__name"] = """
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
        self.vs[3]["mm__"] = """MT_post__Attribute"""
        self.vs[3]["GUID__"] = 551492306865643050
        self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[4]["GUID__"] = 2986862843492939104
        self.vs[5]["MT_label__"] = """6"""
        self.vs[5]["mm__"] = """MT_post__hasAttr_S"""
        self.vs[5]["GUID__"] = 1551870587527699583
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
        self.vs[6]["mm__"] = """MT_post__MetaModelElement_S"""
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
        self.vs[6]["GUID__"] = 3800033019108257959
        self.vs[7]["MT_post__cardinality"] = """
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
        self.vs[7]["MT_label__"] = """2"""
        self.vs[7]["MT_post__name"] = """
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
        self.vs[7]["mm__"] = """MT_post__MetaModelElement_S"""
        self.vs[7]["MT_post__classtype"] = """
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
        self.vs[7]["GUID__"] = 5801313102950526454

        from HMoveOneEquationsLeftExpressionLHS import HMoveOneEquationsLeftExpressionLHS
        self.pre = HMoveOneEquationsLeftExpressionLHS()
    
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
        # leftExpr9
        new_node = graph.add_node()
        labels['9'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # leftExpr9 -> Attribute4
        graph.add_edges([(labels['9'], labels['4'])])
        # Equation7 -> leftExpr9
        graph.add_edges([(labels['7'], labels['9'])])
        
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
        # MT_pre__leftExpr8
        graph.delete_nodes([labels["8"]])
    
