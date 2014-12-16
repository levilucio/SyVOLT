

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
        self["GUID__"] = UUID('39c41ae7-bd5d-4c24-9768-f3b346375ca5')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('74430ebb-dc00-488b-9c97-3262d6389fe6')
        self.vs[1]["mm__"] = """leftExpr"""
        self.vs[1]["GUID__"] = UUID('797a2981-0b31-44f9-a9b5-abd5cec91571')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('5c95d6b2-b95c-45c7-8055-f3a9b0793ec1')
        self.vs[3]["mm__"] = """hasAttr_S"""
        self.vs[3]["GUID__"] = UUID('82f87907-783b-49aa-ad45-b39fdf27500a')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('ac6bf04f-cb42-42cb-9dc7-cd974cecfd6f')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Female_T"""
        self.vs[5]["GUID__"] = UUID('0595c091-0c19-4582-84c4-249a3d72e0c4')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """1"""
        self.vs[6]["mm__"] = """Female_S"""
        self.vs[6]["cardinality"] = """s_"""
        self.vs[6]["GUID__"] = UUID('3a61238f-c5b0-4fd9-bc58-7ac7a352e858')
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = UUID('f52cd4b6-a241-4f99-b979-a6dda883a3f6')
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = UUID('77c4ede5-dc7c-4009-b4b9-26594c5d9810')
        self.vs[9]["value"] = """otherfemale"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["GUID__"] = UUID('ae5e07e5-2e7e-40e4-97b4-78b7a9df7a29')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('bf36daae-0693-4cc2-82cd-2fcc22f268e9')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('16331242-bcdf-48b2-97fe-463c80164da3')
        self.vs[12]["name"] = """name"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = UUID('b91b5d52-76f3-4350-a6d3-716369dd1e7d')

