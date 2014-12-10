

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HNacExampleRuleNAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HNacExampleRuleNAC0Bridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HNacExampleRuleNAC0Bridge, self).__init__(name='HNacExampleRuleNAC0Bridge', num_nodes=1, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["GUID__"] = UUID('a5b37073-1248-494b-93d0-a16138df19c8')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """from HNacExampleRuleNAC0 import HNacExampleRuleNAC0
from HNacExampleRuleLHS import HNacExampleRuleLHS
lhs = HNacExampleRuleLHS()
return HNacExampleRuleNAC0(lhs).eval_classtype1(attr_value, this) and HNacExampleRuleLHS().eval_classtype1(attr_value, this)"""
        self.vs[0]["MT_pre__cardinality"] = """from HNacExampleRuleNAC0 import HNacExampleRuleNAC0
from HNacExampleRuleLHS import HNacExampleRuleLHS
lhs = HNacExampleRuleLHS()
return HNacExampleRuleNAC0(lhs).eval_cardinality1(attr_value, this) and HNacExampleRuleLHS().eval_cardinality1(attr_value, this)"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_pre__name"] = """from HNacExampleRuleNAC0 import HNacExampleRuleNAC0
from HNacExampleRuleLHS import HNacExampleRuleLHS
lhs = HNacExampleRuleLHS()
return HNacExampleRuleNAC0(lhs).eval_name1(attr_value, this) and HNacExampleRuleLHS().eval_name1(attr_value, this)"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('c71b4de1-ff15-426c-b618-9135715c0a22')

    def eval_classtype1(self, attr_value, this):
        from HNacExampleRuleNAC0 import HNacExampleRuleNAC0
        from HNacExampleRuleLHS import HNacExampleRuleLHS
        lhs = HNacExampleRuleLHS()
        return HNacExampleRuleNAC0(lhs).eval_classtype1(attr_value, this) and HNacExampleRuleLHS().eval_classtype1(attr_value, this)


    def eval_cardinality1(self, attr_value, this):
        from HNacExampleRuleNAC0 import HNacExampleRuleNAC0
        from HNacExampleRuleLHS import HNacExampleRuleLHS
        lhs = HNacExampleRuleLHS()
        return HNacExampleRuleNAC0(lhs).eval_cardinality1(attr_value, this) and HNacExampleRuleLHS().eval_cardinality1(attr_value, this)


    def eval_name1(self, attr_value, this):
        from HNacExampleRuleNAC0 import HNacExampleRuleNAC0
        from HNacExampleRuleLHS import HNacExampleRuleLHS
        lhs = HNacExampleRuleLHS()
        return HNacExampleRuleNAC0(lhs).eval_name1(attr_value, this) and HNacExampleRuleLHS().eval_name1(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

