

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HS2S_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S_run3, self).__init__(name='HS2S_run3', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 4), (6, 1), (2, 6), (2, 3), (3, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """S2S_run3"""
        self["GUID__"] = UUID('cf2348b4-918e-46ef-9923-23453b0b3cd1')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('959d6560-b897-4ccc-b40b-ed6904ffee13')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('e633f258-44dd-4ff0-b74a-28923f998d77')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('6271f21e-f70a-41a0-9cfc-2073166ded6d')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('d3f78043-37d9-413f-ae3b-137f9ef6e267')
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["classtype"] = """station3"""
        self.vs[4]["name"] = """s"""
        self.vs[4]["GUID__"] = UUID('fead48a4-eb00-43d7-8bfa-6078293c052e')
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["classtype"] = """station3"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """s"""
        self.vs[5]["GUID__"] = UUID('ed20a1b1-15dd-4d8d-a7a7-90e955afa1cf')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('f5b13259-4bc9-499f-9cd1-89a9e15b110e')

