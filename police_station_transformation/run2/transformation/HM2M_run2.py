

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HM2M_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M_run2, self).__init__(name='HM2M_run2', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 5), (6, 1), (2, 6), (2, 3), (3, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """M2M_run2"""
        self["GUID__"] = UUID('6d470f20-0333-41bb-b4b6-6ac0f2a1e141')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('0da4e04a-82d3-438b-9964-488a352d3441')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('a74925e0-2d6b-460a-a12f-28c1bf184c84')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('100b8103-9ffa-4600-a841-e03ec682153b')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('e0027e0e-cd30-42eb-9686-64bb9b2c06d9')
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["classtype"] = """male2"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["name"] = """m"""
        self.vs[4]["GUID__"] = UUID('f49fce18-2f5a-481d-9254-8fee696cdf10')
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["classtype"] = """male2"""
        self.vs[5]["name"] = """m"""
        self.vs[5]["GUID__"] = UUID('67e423ee-482a-44af-aeb4-cd881c200848')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('698deaa5-912b-4db4-b6b3-ab35e6c6050f')

