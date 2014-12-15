

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HSF2SF_combine_0NAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_combine_0NAC0Bridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_combine_0NAC0Bridge, self).__init__(name='HSF2SF_combine_0NAC0Bridge', num_nodes=2, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["GUID__"] = UUID('2928652e-1d98-4f9a-b4ab-430714a9ff54')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
lhs = HSF2SF_combine_0LHS()
return HSF2SF_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HSF2SF_combine_0LHS().eval_classtype1(attr_value, this)"""
        self.vs[0]["MT_pre__name"] = """from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
lhs = HSF2SF_combine_0LHS()
return HSF2SF_combine_0NAC0(lhs).eval_name1(attr_value, this) and HSF2SF_combine_0LHS().eval_name1(attr_value, this)"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__cardinality"] = """from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
lhs = HSF2SF_combine_0LHS()
return HSF2SF_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HSF2SF_combine_0LHS().eval_cardinality1(attr_value, this)"""
        self.vs[0]["GUID__"] = UUID('a9764ae2-16dd-4abb-b1b7-506299b9dc64')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
lhs = HSF2SF_combine_0LHS()
return HSF2SF_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HSF2SF_combine_0LHS().eval_classtype2(attr_value, this)"""
        self.vs[1]["MT_pre__name"] = """from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
lhs = HSF2SF_combine_0LHS()
return HSF2SF_combine_0NAC0(lhs).eval_name2(attr_value, this) and HSF2SF_combine_0LHS().eval_name2(attr_value, this)"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["mm__"] = """MT_pre__Female_S"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__cardinality"] = """from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
lhs = HSF2SF_combine_0LHS()
return HSF2SF_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HSF2SF_combine_0LHS().eval_cardinality2(attr_value, this)"""
        self.vs[1]["GUID__"] = UUID('5dc29e67-a709-4cb8-9689-4df0c2fe879a')

    def eval_classtype1(self, attr_value, this):
        from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
        from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
        lhs = HSF2SF_combine_0LHS()
        return HSF2SF_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HSF2SF_combine_0LHS().eval_classtype1(attr_value, this)


    def eval_name1(self, attr_value, this):
        from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
        from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
        lhs = HSF2SF_combine_0LHS()
        return HSF2SF_combine_0NAC0(lhs).eval_name1(attr_value, this) and HSF2SF_combine_0LHS().eval_name1(attr_value, this)


    def eval_cardinality1(self, attr_value, this):
        from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
        from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
        lhs = HSF2SF_combine_0LHS()
        return HSF2SF_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HSF2SF_combine_0LHS().eval_cardinality1(attr_value, this)


    def eval_classtype2(self, attr_value, this):
        from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
        from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
        lhs = HSF2SF_combine_0LHS()
        return HSF2SF_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HSF2SF_combine_0LHS().eval_classtype2(attr_value, this)


    def eval_name2(self, attr_value, this):
        from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
        from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
        lhs = HSF2SF_combine_0LHS()
        return HSF2SF_combine_0NAC0(lhs).eval_name2(attr_value, this) and HSF2SF_combine_0LHS().eval_name2(attr_value, this)


    def eval_cardinality2(self, attr_value, this):
        from HSF2SF_combine_0NAC0 import HSF2SF_combine_0NAC0
        from HSF2SF_combine_0LHS import HSF2SF_combine_0LHS
        lhs = HSF2SF_combine_0LHS()
        return HSF2SF_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HSF2SF_combine_0LHS().eval_cardinality2(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

