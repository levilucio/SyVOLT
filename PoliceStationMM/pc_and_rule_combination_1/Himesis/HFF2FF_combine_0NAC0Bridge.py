

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HFF2FF_combine_0NAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_combine_0NAC0Bridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_combine_0NAC0Bridge, self).__init__(name='HFF2FF_combine_0NAC0Bridge', num_nodes=2, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["GUID__"] = UUID('3b980f30-c33c-4f9a-a9d1-ffc0e27ba60f')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
lhs = HFF2FF_combine_0LHS()
return HFF2FF_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HFF2FF_combine_0LHS().eval_classtype1(attr_value, this)"""
        self.vs[0]["MT_pre__name"] = """from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
lhs = HFF2FF_combine_0LHS()
return HFF2FF_combine_0NAC0(lhs).eval_name1(attr_value, this) and HFF2FF_combine_0LHS().eval_name1(attr_value, this)"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Female_S"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__cardinality"] = """from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
lhs = HFF2FF_combine_0LHS()
return HFF2FF_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HFF2FF_combine_0LHS().eval_cardinality1(attr_value, this)"""
        self.vs[0]["GUID__"] = UUID('c50c1bee-a242-4bdb-bfe1-8a66d3f10eec')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
lhs = HFF2FF_combine_0LHS()
return HFF2FF_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HFF2FF_combine_0LHS().eval_classtype2(attr_value, this)"""
        self.vs[1]["MT_pre__name"] = """from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
lhs = HFF2FF_combine_0LHS()
return HFF2FF_combine_0NAC0(lhs).eval_name2(attr_value, this) and HFF2FF_combine_0LHS().eval_name2(attr_value, this)"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["mm__"] = """MT_pre__Female_S"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__cardinality"] = """from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
lhs = HFF2FF_combine_0LHS()
return HFF2FF_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HFF2FF_combine_0LHS().eval_cardinality2(attr_value, this)"""
        self.vs[1]["GUID__"] = UUID('63bb90ec-3554-4ee8-a27e-f672576d8bb7')

    def eval_classtype1(self, attr_value, this):
        from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        lhs = HFF2FF_combine_0LHS()
        return HFF2FF_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HFF2FF_combine_0LHS().eval_classtype1(attr_value, this)


    def eval_name1(self, attr_value, this):
        from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        lhs = HFF2FF_combine_0LHS()
        return HFF2FF_combine_0NAC0(lhs).eval_name1(attr_value, this) and HFF2FF_combine_0LHS().eval_name1(attr_value, this)


    def eval_cardinality1(self, attr_value, this):
        from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        lhs = HFF2FF_combine_0LHS()
        return HFF2FF_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HFF2FF_combine_0LHS().eval_cardinality1(attr_value, this)


    def eval_classtype2(self, attr_value, this):
        from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        lhs = HFF2FF_combine_0LHS()
        return HFF2FF_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HFF2FF_combine_0LHS().eval_classtype2(attr_value, this)


    def eval_name2(self, attr_value, this):
        from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        lhs = HFF2FF_combine_0LHS()
        return HFF2FF_combine_0NAC0(lhs).eval_name2(attr_value, this) and HFF2FF_combine_0LHS().eval_name2(attr_value, this)


    def eval_cardinality2(self, attr_value, this):
        from HFF2FF_combine_0NAC0 import HFF2FF_combine_0NAC0
        from HFF2FF_combine_0LHS import HFF2FF_combine_0LHS
        lhs = HFF2FF_combine_0LHS()
        return HFF2FF_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HFF2FF_combine_0LHS().eval_cardinality2(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

