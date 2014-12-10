

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HF2F_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F_run1, self).__init__(name='HF2F_run1', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 3), (6, 1), (2, 6), (2, 4), (4, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """F2F_run1"""
        self["GUID__"] = UUID('4c3e8ffb-2822-4b4f-9d34-66d0982c1cf4')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('3127138e-0947-4dc6-a17f-984b6a026a3d')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('55a6c9ce-2ce5-4b60-80a5-6c8c277d81d5')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('bbad43ff-3a99-42cf-8932-a99448f7baa2')
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["classtype"] = """female1"""
        self.vs[3]["name"] = """2.f"""
        self.vs[3]["GUID__"] = UUID('0a6e37a9-2a82-4854-a4a1-b076c7cab911')
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = UUID('0bb2e76d-3174-4500-9e0e-47654f748637')
        self.vs[5]["mm__"] = """Female_S"""
        self.vs[5]["classtype"] = """female1"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """2.f"""
        self.vs[5]["GUID__"] = UUID('34d24515-123e-4721-8dd2-3e3be08f83ac')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('1cdbdc76-7ba6-4206-9d47-e4fd2e509a23')

