

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HF2F(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F, self).__init__(name='HF2F', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 5), (7, 1), (1, 12), (11, 2), (2, 4), (6, 3), (3, 12), (8, 6), (7, 10), (11, 8), (10, 9)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """F2F"""
        self["GUID__"] = UUID('72717195-5d7d-4f80-800e-cf9fe025284c')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('65309cc5-d98d-43d5-b6db-7c13557aa4c9')
        self.vs[1]["mm__"] = """leftExpr"""
        self.vs[1]["GUID__"] = UUID('cd748650-7047-4847-97bc-b9415947ea72')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('57bd7ce1-43f6-4506-9da0-1ac139f934d0')
        self.vs[3]["mm__"] = """hasAttr_S"""
        self.vs[3]["GUID__"] = UUID('910f9064-c910-4e1b-b3cb-088ee5fc3c0b')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('b4cf2e9e-6329-42a1-a89f-4f85ccac31d6')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Female_T"""
        self.vs[5]["GUID__"] = UUID('e2f4b6a6-f37d-4e18-b27d-7c5fce4cc6c7')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """1"""
        self.vs[6]["mm__"] = """Female_S"""
        self.vs[6]["cardinality"] = """s_"""
        self.vs[6]["GUID__"] = UUID('e0fad517-da69-49a4-a354-fcc29a5ef92d')
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = UUID('b7dbfc8a-079f-4a26-ac4b-76ae8730ad05')
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = UUID('99c408c9-b257-4a89-ab76-875c7397b198')
        self.vs[9]["value"] = """somefemale"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["GUID__"] = UUID('33a22295-542c-4093-a9dc-3ee345422406')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('84833519-3e66-4dc8-9f67-29a9472a3385')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('768a631c-0131-4ab5-9080-3e1bc44de21c')
        self.vs[12]["name"] = """name"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = UUID('52f821d5-b503-4001-92cd-ba085049b08b')

