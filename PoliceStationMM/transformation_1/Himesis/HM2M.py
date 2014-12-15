

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HM2M(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M, self).__init__(name='HM2M', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 8), (8, 1), (1, 13), (6, 2), (2, 12), (10, 3), (3, 5), (11, 4), (4, 12), (6, 9), (10, 7), (7, 11), (9, 13)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """M2M"""
        self["GUID__"] = UUID('c75accd4-00ab-4b94-8953-fb3bd2345976')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('3be8db42-90cf-4071-b2b6-dcc97abfae6d')
        self.vs[1]["mm__"] = """hasAttr_T"""
        self.vs[1]["GUID__"] = UUID('b3bf5747-0110-46aa-854e-74302afaa512')
        self.vs[2]["mm__"] = """leftExpr"""
        self.vs[2]["GUID__"] = UUID('aed86ca1-f4fa-4866-be4e-8b1616fddbbd')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('ce5a3418-09fc-4363-9cb9-9fb45222a73e')
        self.vs[4]["mm__"] = """hasAttr_S"""
        self.vs[4]["GUID__"] = UUID('965753a9-2e87-4382-ad77-b96f4e2f6066')
        self.vs[5]["mm__"] = """ApplyModel"""
        self.vs[5]["GUID__"] = UUID('b3150227-4670-4f73-97ac-28ccf12e300e')
        self.vs[6]["mm__"] = """Equation"""
        self.vs[6]["GUID__"] = UUID('f9b19499-d98b-4dc0-bbc4-acb8ce20220d')
        self.vs[7]["mm__"] = """match_contains"""
        self.vs[7]["GUID__"] = UUID('183407ab-c84a-4fd9-b403-4b3c63ed27a0')
        self.vs[8]["mm__"] = """Male_T"""
        self.vs[8]["classtype"] = """t_"""
        self.vs[8]["name"] = """s_"""
        self.vs[8]["GUID__"] = UUID('21272de3-7a67-4073-b297-62f2adcdf0ef')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('533e39f8-5280-4485-9bdd-d437ac1e1a40')
        self.vs[10]["mm__"] = """MatchModel"""
        self.vs[10]["GUID__"] = UUID('12bca39a-57be-4a6a-954e-a1fb7cf85800')
        self.vs[11]["mm__"] = """Male_S"""
        self.vs[11]["classtype"] = """1"""
        self.vs[11]["cardinality"] = """s_"""
        self.vs[11]["name"] = """s_"""
        self.vs[11]["GUID__"] = UUID('8bfc8116-0841-4aa6-b2c4-bb5af3321fdb')
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["name"] = """name"""
        self.vs[12]["GUID__"] = UUID('ddf8753f-48ce-428e-9d23-ecaabcf6b269')
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["name"] = """name"""
        self.vs[13]["GUID__"] = UUID('2393418c-e3ea-4b39-b883-1a0fc7841631')

