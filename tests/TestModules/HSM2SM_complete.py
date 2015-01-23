

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_complete(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_complete.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_complete, self).__init__(name='HSM2SM_complete', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 5), (2, 10), (10, 6), (5, 0), (0, 6), (7, 1), (1, 2), (5, 11), (11, 4), (6, 12), (12, 8), (4, 13), (13, 17), (8, 14), (14, 18), (4, 3), (3, 8), (15, 4), (7, 15), (7, 16), (16, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_complete"""
        self["GUID__"] = UUID('9b5f75bf-04f9-4571-a40f-da83b42e54ba')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('6e55a67c-b151-451c-9380-6d9a328e1e6d')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('78464650-1eea-47b8-a4b9-e6792632d335')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('40024bb8-89b3-4765-a4f7-365915f5b1b6')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('65c0b3b0-4b86-4c04-8e2f-cded8b820da0')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """1"""
        self.vs[4]["mm__"] = """Station_S"""
        self.vs[4]["cardinality"] = """s_"""
        self.vs[4]["GUID__"] = UUID('d132814e-45b5-4d43-a832-64f9c11000a6')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('caa876b8-2953-4aaf-9cc8-e559ec4d68b7')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Male_T"""
        self.vs[6]["GUID__"] = UUID('db1dbac5-4f4f-4745-afb4-3c020c601e83')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('6c0183f5-b0f5-4081-a624-97a374ecfe38')
        self.vs[8]["name"] = """s_"""
        self.vs[8]["classtype"] = """1"""
        self.vs[8]["mm__"] = """Male_S"""
        self.vs[8]["cardinality"] = """s_"""
        self.vs[8]["GUID__"] = UUID('ad30b759-6f1a-4245-8848-7a1c2d6ce7fd')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('8f72dca2-793a-44c1-87ba-88d196ecd342')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('abb496c0-1d67-48a1-8b38-e0f883c79ad4')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('d7d1ab08-0d1f-4452-98a8-9d0f19d65b36')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('bb5a7ddb-1556-482c-a046-a7f9590dec5d')
        self.vs[13]["mm__"] = """hasAttr_S"""
        self.vs[13]["GUID__"] = UUID('cba61f96-79d7-40ba-8f58-b6e509299a4a')
        self.vs[14]["mm__"] = """hasAttr_S"""
        self.vs[14]["GUID__"] = UUID('5257ab18-2e32-4946-a57c-6110baaeea35')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('e66ff4bb-6e24-4d74-ba00-8fdf7e143ecc')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('5c99e827-fa22-4344-a8b3-d3373fd3694b')
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["GUID__"] = UUID('0b3e07d6-49fc-42d0-91f1-c6014364b6a5')
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["GUID__"] = UUID('b8c92931-c9d5-486d-a604-5208bda50847')

