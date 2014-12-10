

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HS2S_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S_run2, self).__init__(name='HS2S_run2', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 4), (6, 1), (2, 6), (2, 3), (3, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """S2S_run2"""
        self["GUID__"] = UUID('f0e829ca-f3c6-4382-aafa-587a8815acf0')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('e62b1dd8-2a94-4453-b37d-8b818ec6a1d8')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('e94a0f05-ec3a-4174-b343-8cd4e4dedd9f')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('3beebbff-c91c-4811-bd1a-a90c9ca03f95')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('8cdb60e5-5b3a-4937-bec3-09b50e75c5b2')
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["classtype"] = """station2"""
        self.vs[4]["name"] = """s"""
        self.vs[4]["GUID__"] = UUID('afdbcf5e-5315-461f-976e-1d573cfdd461')
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["classtype"] = """station2"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """s"""
        self.vs[5]["GUID__"] = UUID('ec1aae26-bc12-4a20-8c51-252fdfbe0714')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('f4277af0-9f67-4449-8a23-ba1a148a839b')

