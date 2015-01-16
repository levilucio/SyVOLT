

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HSM2SM_combine_0NAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_combine_0NAC0Bridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_combine_0NAC0Bridge, self).__init__(name='HSM2SM_combine_0NAC0Bridge', num_nodes=2, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["GUID__"] = UUID('15a23085-3315-4330-8618-9e08be3c7be5')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
lhs = HSM2SM_combine_0LHS()
return HSM2SM_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HSM2SM_combine_0LHS().eval_classtype1(attr_value, this)"""
        self.vs[0]["MT_pre__name"] = """from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
lhs = HSM2SM_combine_0LHS()
return HSM2SM_combine_0NAC0(lhs).eval_name1(attr_value, this) and HSM2SM_combine_0LHS().eval_name1(attr_value, this)"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Station_S"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__cardinality"] = """from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
lhs = HSM2SM_combine_0LHS()
return HSM2SM_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HSM2SM_combine_0LHS().eval_cardinality1(attr_value, this)"""
        self.vs[0]["GUID__"] = UUID('13a1933c-d57c-4413-ba85-55a362d88538')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
lhs = HSM2SM_combine_0LHS()
return HSM2SM_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HSM2SM_combine_0LHS().eval_classtype2(attr_value, this)"""
        self.vs[1]["MT_pre__name"] = """from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
lhs = HSM2SM_combine_0LHS()
return HSM2SM_combine_0NAC0(lhs).eval_name2(attr_value, this) and HSM2SM_combine_0LHS().eval_name2(attr_value, this)"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["mm__"] = """MT_pre__Male_S"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__cardinality"] = """from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
lhs = HSM2SM_combine_0LHS()
return HSM2SM_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HSM2SM_combine_0LHS().eval_cardinality2(attr_value, this)"""
        self.vs[1]["GUID__"] = UUID('cdb2d0c1-b8b3-4612-92c0-923ae0349a2c')

    def eval_classtype1(self, attr_value, this):
        from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        lhs = HSM2SM_combine_0LHS()
        return HSM2SM_combine_0NAC0(lhs).eval_classtype1(attr_value, this) and HSM2SM_combine_0LHS().eval_classtype1(attr_value, this)


    def eval_name1(self, attr_value, this):
        from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        lhs = HSM2SM_combine_0LHS()
        return HSM2SM_combine_0NAC0(lhs).eval_name1(attr_value, this) and HSM2SM_combine_0LHS().eval_name1(attr_value, this)


    def eval_cardinality1(self, attr_value, this):
        from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        lhs = HSM2SM_combine_0LHS()
        return HSM2SM_combine_0NAC0(lhs).eval_cardinality1(attr_value, this) and HSM2SM_combine_0LHS().eval_cardinality1(attr_value, this)


    def eval_classtype2(self, attr_value, this):
        from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        lhs = HSM2SM_combine_0LHS()
        return HSM2SM_combine_0NAC0(lhs).eval_classtype2(attr_value, this) and HSM2SM_combine_0LHS().eval_classtype2(attr_value, this)


    def eval_name2(self, attr_value, this):
        from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        lhs = HSM2SM_combine_0LHS()
        return HSM2SM_combine_0NAC0(lhs).eval_name2(attr_value, this) and HSM2SM_combine_0LHS().eval_name2(attr_value, this)


    def eval_cardinality2(self, attr_value, this):
        from HSM2SM_combine_0NAC0 import HSM2SM_combine_0NAC0
        from HSM2SM_combine_0LHS import HSM2SM_combine_0LHS
        lhs = HSM2SM_combine_0LHS()
        return HSM2SM_combine_0NAC0(lhs).eval_cardinality2(attr_value, this) and HSM2SM_combine_0LHS().eval_cardinality2(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

