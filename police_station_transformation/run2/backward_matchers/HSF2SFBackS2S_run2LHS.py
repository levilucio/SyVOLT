

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HSF2SFBackS2S_run2LHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SFBackS2S_run2LHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SFBackS2S_run2LHS, self).__init__(name='HSF2SFBackS2S_run2LHS', num_nodes=3, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (2, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__PoliceStationMM'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
        self["name"] = """"""
        self["GUID__"] = UUID('1fe65102-013e-4336-b7c3-e718abd924a6')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station2':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
        self.vs[0]["MT_pre__cardinality"] = pickle.loads("""Vreturn True\u000a
p1
.""")
        self.vs[0]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn True\u000a
p1
.""")
        self.vs[0]["GUID__"] = UUID('52ce6997-78eb-412d-a7a0-9385c55ebf94')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """9"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["mm__"] = """MT_pre__trace_link"""
        self.vs[1]["GUID__"] = UUID('74b64767-fdf5-43de-9ac6-abad4f85a786')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = pickle.loads("""Vif attr_value == 'station2':\u000a    return True\u000aelse:\u000a    return False\u000a
p1
.""")
        self.vs[2]["MT_label__"] = """2"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["mm__"] = """MT_pre__Station_T"""
        self.vs[2]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[2]["GUID__"] = UUID('86604c46-1d82-4b27-80ab-5ad2e82ea022')

    def eval_classtype1(self, attr_value, this):
        if attr_value == 'station2':
            return True
        else:
            return False


    def eval_cardinality1(self, attr_value, this):
        return True


    def eval_name1(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_classtype2(self, attr_value, this):
        if attr_value == 'station2':
            return True
        else:
            return False


    def eval_name2(self, attr_value, this):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================
        
        return True

