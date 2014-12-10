

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HF2F_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F_run2, self).__init__(name='HF2F_run2', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 3), (6, 1), (2, 6), (2, 4), (4, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """F2F_run2"""
        self["GUID__"] = UUID('25d0326c-21ed-4e55-845a-b36f5fe52860')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('ad56796d-0827-4900-b359-50fcf9d33d80')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('fb58d965-2cc1-4be1-a300-4a8de872eb42')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('1591be6e-020f-4f28-8cea-ef216fe978f1')
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["classtype"] = """female2"""
        self.vs[3]["name"] = """f"""
        self.vs[3]["GUID__"] = UUID('83e7b0fb-2b61-46b3-8fba-0856724e15eb')
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = UUID('4d3ee91b-0ca6-4705-b192-5cf34981cd85')
        self.vs[5]["mm__"] = """Female_S"""
        self.vs[5]["classtype"] = """female2"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """f"""
        self.vs[5]["GUID__"] = UUID('5af7667f-f3ba-44c7-b454-f9f4f52d59e6')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('ff8df73c-cf21-48d3-8b17-065efd72d67d')

