

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HBasicStateNoOutgoing2ProcDef_match_pattern_rewriter(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicStateNoOutgoing2ProcDef_match_pattern_rewriter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicStateNoOutgoing2ProcDef_match_pattern_rewriter, self).__init__(name='HBasicStateNoOutgoing2ProcDef_match_pattern_rewriter', num_nodes=30, edges=[])
        
        # Add the edges
        self.add_edges([[8, 0], [0, 7], [19, 15], [15, 28], [18, 16], [16, 27], [20, 17], [17, 29], [8, 1], [1, 23], [5, 2], [2, 12], [2, 13], [6, 3], [3, 4], [4, 10], [10, 21], [4, 11], [11, 22], [9, 4], [6, 5], [18, 24], [19, 25], [20, 26], [13, 7], [12, 8], [8, 9], [24, 21], [25, 22], [26, 23], [7, 14], [14, 4]])
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
        self["name"] = """BasicStateNoOutgoing2ProcDef"""
        self["GUID__"] = UUID('08346ac3-1a47-4fed-a83e-4b403ea6994d')
        
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
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["mm__"] = """MT_post__directLink_T"""
        self.vs[0]["GUID__"] = UUID('58ab6e87-4551-443e-bfff-63fbaec4aece')
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["mm__"] = """MT_post__hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('9fb62753-1769-4343-a251-1e39317acbe9')
        self.vs[2]["MT_label__"] = """2"""
        self.vs[2]["mm__"] = """MT_post__ApplyModel"""
        self.vs[2]["GUID__"] = UUID('d972c3f8-f639-4f7c-84ff-8363453a522d')
        self.vs[3]["MT_label__"] = """3"""
        self.vs[3]["mm__"] = """MT_post__match_contains"""
        self.vs[3]["GUID__"] = UUID('5f94aced-772a-4fb2-bfc5-9814cf857f1d')
        self.vs[4]["MT_post__cardinality"] = """
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
        self.vs[4]["mm__"] = """MT_post__State"""
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
        self.vs[4]["GUID__"] = UUID('c6922e5f-99ee-4364-a792-6c57221d528a')
        self.vs[5]["MT_label__"] = """5"""
        self.vs[5]["mm__"] = """MT_post__paired_with"""
        self.vs[5]["GUID__"] = UUID('8ce1a5f1-3270-49b7-9a0f-7d0d26f809f7')
        self.vs[6]["MT_label__"] = """6"""
        self.vs[6]["mm__"] = """MT_post__MatchModel"""
        self.vs[6]["GUID__"] = UUID('4420071f-e83a-4268-8800-632cf7217570')
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
        self.vs[7]["MT_label__"] = """7"""
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
        self.vs[7]["mm__"] = """MT_post__Null"""
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
        self.vs[7]["GUID__"] = UUID('126a0f48-d3d4-418e-99cc-119845c0824b')
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
        self.vs[8]["MT_label__"] = """8"""
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
        self.vs[8]["mm__"] = """MT_post__ProcDef"""
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
        self.vs[8]["GUID__"] = UUID('9233ea41-f0ba-46a2-9cf5-1afcc0e29357')
        self.vs[9]["MT_post__type"] = """
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
        self.vs[9]["MT_label__"] = """9"""
        self.vs[9]["mm__"] = """MT_post__trace_link"""
        self.vs[9]["GUID__"] = UUID('ec016c81-d5de-4142-be2b-a2c199b4bd4d')
        self.vs[10]["MT_label__"] = """10"""
        self.vs[10]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('08746aa3-1cce-4d1b-836a-a4a32027579c')
        self.vs[11]["MT_label__"] = """11"""
        self.vs[11]["mm__"] = """MT_post__hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('c044e48e-3dbf-4672-a699-664c44b592ea')
        self.vs[12]["MT_label__"] = """12"""
        self.vs[12]["mm__"] = """MT_post__apply_contains"""
        self.vs[12]["GUID__"] = UUID('c3bea447-16d5-4b5f-b46c-04410400b949')
        self.vs[13]["MT_label__"] = """13"""
        self.vs[13]["mm__"] = """MT_post__apply_contains"""
        self.vs[13]["GUID__"] = UUID('32976621-348e-41b9-9d9e-0e5cc18f7983')
        self.vs[14]["MT_label__"] = """29"""
        self.vs[14]["mm__"] = """MT_post__trace_link"""
        self.vs[14]["GUID__"] = UUID('e7130ecb-4b72-4f7f-9b79-e9ae14694eba')
        self.vs[15]["MT_label__"] = """14"""
        self.vs[15]["mm__"] = """MT_post__rightExpr"""
        self.vs[15]["GUID__"] = UUID('2084dd88-dcc6-4cc4-bf73-4e6ba642889d')
        self.vs[16]["MT_label__"] = """15"""
        self.vs[16]["mm__"] = """MT_post__rightExpr"""
        self.vs[16]["GUID__"] = UUID('5f6be339-0999-4fd7-9e9d-eb543ad11b08')
        self.vs[17]["MT_label__"] = """16"""
        self.vs[17]["mm__"] = """MT_post__rightExpr"""
        self.vs[17]["GUID__"] = UUID('0db1fbd6-cb67-4813-963f-9e0c55025b24')
        self.vs[18]["MT_label__"] = """17"""
        self.vs[18]["MT_post__name"] = """
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
        self.vs[18]["mm__"] = """MT_post__Equation"""
        self.vs[18]["GUID__"] = UUID('8b49bbf3-1bf9-428d-84ed-d98e720da5d5')
        self.vs[19]["MT_label__"] = """18"""
        self.vs[19]["MT_post__name"] = """
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
        self.vs[19]["mm__"] = """MT_post__Equation"""
        self.vs[19]["GUID__"] = UUID('97df9a79-4269-4dfe-8196-a03ec0a36eca')
        self.vs[20]["MT_label__"] = """19"""
        self.vs[20]["MT_post__name"] = """
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
        self.vs[20]["mm__"] = """MT_post__Equation"""
        self.vs[20]["GUID__"] = UUID('7d22d7b5-ae26-4fae-8ca0-6ac250ed9d1b')
        self.vs[21]["MT_label__"] = """20"""
        self.vs[21]["MT_post__Type"] = """
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
        self.vs[21]["MT_post__name"] = """
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
        self.vs[21]["mm__"] = """MT_post__Attribute"""
        self.vs[21]["GUID__"] = UUID('a9c9e9b8-d009-40a7-a9ea-df0fc913200d')
        self.vs[22]["MT_label__"] = """21"""
        self.vs[22]["MT_post__Type"] = """
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
        self.vs[22]["MT_post__name"] = """
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
        self.vs[22]["mm__"] = """MT_post__Attribute"""
        self.vs[22]["GUID__"] = UUID('afd9794f-4f68-4d05-94ab-d63985935fce')
        self.vs[23]["MT_label__"] = """22"""
        self.vs[23]["MT_post__Type"] = """
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
        self.vs[23]["MT_post__name"] = """
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
        self.vs[23]["mm__"] = """MT_post__Attribute"""
        self.vs[23]["GUID__"] = UUID('ab7d9cc5-6f6b-496b-a28b-9f5d80992d12')
        self.vs[24]["MT_label__"] = """23"""
        self.vs[24]["mm__"] = """MT_post__leftExpr"""
        self.vs[24]["GUID__"] = UUID('f76659f6-1300-451e-91d1-41677c07802c')
        self.vs[25]["MT_label__"] = """24"""
        self.vs[25]["mm__"] = """MT_post__leftExpr"""
        self.vs[25]["GUID__"] = UUID('d6d9217b-413d-485e-92b7-714d2727a400')
        self.vs[26]["MT_label__"] = """25"""
        self.vs[26]["mm__"] = """MT_post__leftExpr"""
        self.vs[26]["GUID__"] = UUID('6c08f50c-fa5f-417e-ae40-7d2964489148')
        self.vs[27]["MT_label__"] = """26"""
        self.vs[27]["MT_post__Type"] = """
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
        self.vs[27]["MT_post__name"] = """return 'false'"""
        self.vs[27]["mm__"] = """MT_post__Constant"""
        self.vs[27]["GUID__"] = UUID('780ccb04-ca3a-4391-a999-828acfbc3691')
        self.vs[28]["MT_label__"] = """27"""
        self.vs[28]["MT_post__Type"] = """
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
        self.vs[28]["MT_post__name"] = """return 'false'"""
        self.vs[28]["mm__"] = """MT_post__Constant"""
        self.vs[28]["GUID__"] = UUID('4ebd2dfc-60e3-47f5-ac8a-395158a30a95')
        self.vs[29]["MT_label__"] = """28"""
        self.vs[29]["MT_post__Type"] = """
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
        self.vs[29]["MT_post__name"] = """return 'procdef'"""
        self.vs[29]["mm__"] = """MT_post__Constant"""
        self.vs[29]["GUID__"] = UUID('e1138885-34ab-4053-98d8-8006df3406f3')

        from HBasicStateNoOutgoing2ProcDef_match_pattern_matcher import HBasicStateNoOutgoing2ProcDef_match_pattern_matcher
        self.pre = HBasicStateNoOutgoing2ProcDef_match_pattern_matcher()
    
    def set_name26(self, attr_value, PreNode, graph):
        return 'false'


    def set_name27(self, attr_value, PreNode, graph):
        return 'false'


    def set_name28(self, attr_value, PreNode, graph):
        return 'procdef'


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
        # directLink_T0
        new_node = graph.add_node()
        labels['0'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'directLink_T'
        # hasAttribute_T1
        new_node = graph.add_node()
        labels['1'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'hasAttribute_T'
        # ApplyModel2
        new_node = graph.add_node()
        labels['2'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'ApplyModel'
        # match_contains3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'match_contains'
        # paired_with5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'paired_with'
        # MatchModel6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'MatchModel'
        # Null7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Null'
        # apply_contains12
        new_node = graph.add_node()
        labels['12'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # apply_contains13
        new_node = graph.add_node()
        labels['13'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'apply_contains'
        # rightExpr14
        new_node = graph.add_node()
        labels['14'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr15
        new_node = graph.add_node()
        labels['15'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # rightExpr16
        new_node = graph.add_node()
        labels['16'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'rightExpr'
        # Equation17
        new_node = graph.add_node()
        labels['17'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation18
        new_node = graph.add_node()
        labels['18'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Equation19
        new_node = graph.add_node()
        labels['19'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Equation'
        # Attribute22
        new_node = graph.add_node()
        labels['22'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Attribute'
        # leftExpr23
        new_node = graph.add_node()
        labels['23'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr24
        new_node = graph.add_node()
        labels['24'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # leftExpr25
        new_node = graph.add_node()
        labels['25'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'leftExpr'
        # Constant26
        new_node = graph.add_node()
        labels['26'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name26(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant27
        new_node = graph.add_node()
        labels['27'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name27(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # Constant28
        new_node = graph.add_node()
        labels['28'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['name'] = self.set_name28(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # trace_link29
        new_node = graph.add_node()
        labels['29'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'trace_link'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # ProcDef8 -> directLink_T0
        graph.add_edges([(labels['8'], labels['0'])])
        # directLink_T0 -> Null7
        graph.add_edges([(labels['0'], labels['7'])])
        # ProcDef8 -> hasAttribute_T1
        graph.add_edges([(labels['8'], labels['1'])])
        # hasAttribute_T1 -> Attribute22
        graph.add_edges([(labels['1'], labels['22'])])
        # ApplyModel2 -> apply_contains12
        graph.add_edges([(labels['2'], labels['12'])])
        # apply_contains12 -> ProcDef8
        graph.add_edges([(labels['12'], labels['8'])])
        # ApplyModel2 -> apply_contains13
        graph.add_edges([(labels['2'], labels['13'])])
        # apply_contains13 -> Null7
        graph.add_edges([(labels['13'], labels['7'])])
        # Equation18 -> rightExpr14
        graph.add_edges([(labels['18'], labels['14'])])
        # rightExpr14 -> Constant27
        graph.add_edges([(labels['14'], labels['27'])])
        # Equation17 -> rightExpr15
        graph.add_edges([(labels['17'], labels['15'])])
        # rightExpr15 -> Constant26
        graph.add_edges([(labels['15'], labels['26'])])
        # Equation19 -> rightExpr16
        graph.add_edges([(labels['19'], labels['16'])])
        # rightExpr16 -> Constant28
        graph.add_edges([(labels['16'], labels['28'])])
        # Equation17 -> leftExpr23
        graph.add_edges([(labels['17'], labels['23'])])
        # Equation18 -> leftExpr24
        graph.add_edges([(labels['18'], labels['24'])])
        # Equation19 -> leftExpr25
        graph.add_edges([(labels['19'], labels['25'])])
        # paired_with5 -> ApplyModel2
        graph.add_edges([(labels['5'], labels['2'])])
        # leftExpr25 -> Attribute22
        graph.add_edges([(labels['25'], labels['22'])])
        # leftExpr23 -> Attribute20
        graph.add_edges([(labels['23'], labels['20'])])
        # leftExpr24 -> Attribute21
        graph.add_edges([(labels['24'], labels['21'])])
        # Null7 -> trace_link29
        graph.add_edges([(labels['7'], labels['29'])])
        # trace_link29 -> State4
        graph.add_edges([(labels['29'], labels['4'])])
        # MatchModel6 -> match_contains3
        graph.add_edges([(labels['6'], labels['3'])])
        # match_contains3 -> State4
        graph.add_edges([(labels['3'], labels['4'])])
        # MatchModel6 -> paired_with5
        graph.add_edges([(labels['6'], labels['5'])])
        
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
    
