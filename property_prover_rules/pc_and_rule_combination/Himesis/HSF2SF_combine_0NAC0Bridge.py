

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
        self["GUID__"] = UUID('3551a9c1-82cb-4ab6-8f6a-3ede407cd6cf')
        
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
        self.vs[0]["GUID__"] = UUID('465c543e-1244-419a-8d9d-3642244b3644')
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
        self.vs[1]["GUID__"] = UUID('14ecb234-980b-4e4d-b67f-a007f8b44b8c')

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

