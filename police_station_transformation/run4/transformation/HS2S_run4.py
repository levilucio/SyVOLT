

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HS2S_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S_run4, self).__init__(name='HS2S_run4', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 4), (6, 1), (2, 6), (2, 3), (3, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """S2S_run4"""
        self["GUID__"] = UUID('2ef9058d-cfa6-48f5-9cea-23569cd80cf9')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('923162a6-186c-4af2-8d92-6663440b9f12')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('d5a47cbd-ea2d-487d-9e80-008d15633000')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('26cefbb8-3864-4b22-97eb-285ed0135341')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('492dfc56-4d23-4dca-b15d-6c5aa464df8f')
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["classtype"] = """station4"""
        self.vs[4]["name"] = """s"""
        self.vs[4]["GUID__"] = UUID('8f3177e6-834f-4e94-b1d5-8703cc20711d')
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["classtype"] = """station4"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """s"""
        self.vs[5]["GUID__"] = UUID('9335345b-59b8-47dc-84b5-3c21ea484c41')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('608bd548-a2f3-4487-93b4-bf00f8f24d63')

