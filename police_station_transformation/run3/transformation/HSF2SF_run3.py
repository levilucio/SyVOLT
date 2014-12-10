

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSF2SF_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_run3, self).__init__(name='HSF2SF_run3', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 3), (5, 11), (11, 6), (3, 12), (12, 7), (5, 0), (0, 3), (8, 1), (2, 8), (2, 13), (2, 14), (6, 4), (4, 7), (13, 6), (14, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SF2SF_run3"""
        self["GUID__"] = UUID('9b9e86ec-9d4f-4fb4-b6ea-a6e289c0fe36')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('d76f3c39-4b02-4aa1-a2e2-1761cccc321f')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('936f6e5f-f2b8-46da-bc51-b54c74916351')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('0d68e7c1-3bdb-4730-bdd3-a46e57fa8156')
        self.vs[3]["name"] = """f"""
        self.vs[3]["classtype"] = """female3"""
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["GUID__"] = UUID('5f11f0f6-6d79-40c2-b569-098b76357437')
        self.vs[4]["mm__"] = """indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('b3df694f-78a1-4aa8-bf52-fe82d2653328')
        self.vs[5]["name"] = """s"""
        self.vs[5]["classtype"] = """station3"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('40d8d85c-8719-4d1f-bc9d-c06b050cd9c9')
        self.vs[6]["name"] = """s"""
        self.vs[6]["classtype"] = """station3"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('f8d6ea3b-4afc-4557-9c95-f0e3b614abc6')
        self.vs[7]["name"] = """f"""
        self.vs[7]["classtype"] = """female3"""
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('22f045dc-7ff9-409b-9fe9-53023faffdd5')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('bef3c897-24b6-4a2d-8cf2-96b0f4fc4732')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('144c017d-0d7d-4bd4-ab65-bc28cc939c12')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('b9eb6de1-4868-4a53-84b1-b0b788b081c3')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('ea6c6067-0b1c-4d78-abc0-e42f49bb9e1c')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('262b9d57-4fb6-42c7-9042-4ba206e344e9')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('a1118dbe-b83b-47e7-b6df-b4e5996bb0d5')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('e480247a-b1d0-4549-b3d9-162ed7346f15')

