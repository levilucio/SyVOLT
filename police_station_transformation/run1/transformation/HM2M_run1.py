

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HM2M_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M_run1, self).__init__(name='HM2M_run1', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 5), (6, 1), (2, 6), (2, 3), (3, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """M2M_run1"""
        self["GUID__"] = UUID('7c845cc1-f28d-4e1a-b83d-2e99f726163a')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('504fc380-1643-4fae-aa97-704d356b05ce')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('fc5ed3fc-681a-498b-a91d-8449b008f782')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('69c3a833-a004-43a2-a8d7-579325ada29c')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('3ec0e85f-c396-4ca2-897b-dd4bcba1e1f4')
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["classtype"] = """male1"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["name"] = """3.m"""
        self.vs[4]["GUID__"] = UUID('8fec5286-c3a7-4121-b6b7-33cb349fcb39')
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["classtype"] = """male1"""
        self.vs[5]["name"] = """3.m"""
        self.vs[5]["GUID__"] = UUID('cc0c523c-9fa2-4ea7-84d3-4a454ddeda2c')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('057abcbe-107e-4812-ad61-e4f8c37667bc')

