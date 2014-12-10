

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HM2M_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M_run4, self).__init__(name='HM2M_run4', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 5), (6, 1), (2, 6), (2, 3), (3, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """M2M_run4"""
        self["GUID__"] = UUID('e5a31f8b-8323-454e-9133-dc5de2d7804a')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('a1aaf21c-74ca-4387-8e3a-de58958cf0ab')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('1bfd6b1c-c07c-4d85-bfde-dd32c1b6df6e')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('f0505037-e177-4c42-bde9-c8676311cf99')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('d2f283dc-37c8-4c1d-a885-01cdfdc15582')
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["classtype"] = """male4"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["name"] = """m"""
        self.vs[4]["GUID__"] = UUID('a42e252b-f324-4f95-b68e-c8ee384db90d')
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["classtype"] = """male4"""
        self.vs[5]["name"] = """m"""
        self.vs[5]["GUID__"] = UUID('5a8c21d2-5f73-4e9c-82b5-ab9441026221')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('d8f02ac7-0261-4638-9185-585da16f9678')

