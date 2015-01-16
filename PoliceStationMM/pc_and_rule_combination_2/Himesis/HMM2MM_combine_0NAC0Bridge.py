

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HMM2MM_combine_0NAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_combine_0NAC0Bridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_combine_0NAC0Bridge, self).__init__(name='HMM2MM_combine_0NAC0Bridge', num_nodes=2, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["GUID__"] = UUID('a0664376-bdf2-4721-a4e9-1487f7a0be11')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
lhs = HMM2MM_combine_0LHS()
return HMM2MM_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HMM2MM_combine_0LHS().eval_classtype1(attr_value, this)"""
        self.vs[0]["MT_pre__name"] = """from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
lhs = HMM2MM_combine_0LHS()
return HMM2MM_combine_0NAC0(lhs).eval_name1(attr_value, this) and HMM2MM_combine_0LHS().eval_name1(attr_value, this)"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Male_S"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__cardinality"] = """from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
lhs = HMM2MM_combine_0LHS()
return HMM2MM_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HMM2MM_combine_0LHS().eval_cardinality1(attr_value, this)"""
        self.vs[0]["GUID__"] = UUID('47feabea-ca7d-44a2-9179-cc7583a4d1c3')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
lhs = HMM2MM_combine_0LHS()
return HMM2MM_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HMM2MM_combine_0LHS().eval_classtype2(attr_value, this)"""
        self.vs[1]["MT_pre__name"] = """from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
lhs = HMM2MM_combine_0LHS()
return HMM2MM_combine_0NAC0(lhs).eval_name2(attr_value, this) and HMM2MM_combine_0LHS().eval_name2(attr_value, this)"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["mm__"] = """MT_pre__Male_S"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__cardinality"] = """from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
lhs = HMM2MM_combine_0LHS()
return HMM2MM_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HMM2MM_combine_0LHS().eval_cardinality2(attr_value, this)"""
        self.vs[1]["GUID__"] = UUID('52bba13c-5700-41f2-934d-686a6091c455')

    def eval_classtype1(self, attr_value, this):
        from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
        from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
        lhs = HMM2MM_combine_0LHS()
        return HMM2MM_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HMM2MM_combine_0LHS().eval_classtype1(attr_value, this)


    def eval_name1(self, attr_value, this):
        from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
        from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
        lhs = HMM2MM_combine_0LHS()
        return HMM2MM_combine_0NAC0(lhs).eval_name1(attr_value, this) and HMM2MM_combine_0LHS().eval_name1(attr_value, this)


    def eval_cardinality1(self, attr_value, this):
        from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
        from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
        lhs = HMM2MM_combine_0LHS()
        return HMM2MM_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HMM2MM_combine_0LHS().eval_cardinality1(attr_value, this)


    def eval_classtype2(self, attr_value, this):
        from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
        from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
        lhs = HMM2MM_combine_0LHS()
        return HMM2MM_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HMM2MM_combine_0LHS().eval_classtype2(attr_value, this)


    def eval_name2(self, attr_value, this):
        from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
        from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
        lhs = HMM2MM_combine_0LHS()
        return HMM2MM_combine_0NAC0(lhs).eval_name2(attr_value, this) and HMM2MM_combine_0LHS().eval_name2(attr_value, this)


    def eval_cardinality2(self, attr_value, this):
        from HMM2MM_combine_0NAC0 import HMM2MM_combine_0NAC0
        from HMM2MM_combine_0LHS import HMM2MM_combine_0LHS
        lhs = HMM2MM_combine_0LHS()
        return HMM2MM_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HMM2MM_combine_0LHS().eval_cardinality2(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

