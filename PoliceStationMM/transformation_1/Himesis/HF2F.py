

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
        
        super(HF2F, self).__init__(name='HF2F', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 6), (6, 1), (1, 13), (8, 2), (2, 12), (11, 3), (3, 5), (7, 4), (4, 12), (9, 7), (8, 10), (11, 9), (10, 13)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """F2F"""
        self["GUID__"] = UUID('f29f67c2-7181-4bae-9ec2-2e0c2e162141')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('8adfc35e-1a81-4fab-ae34-238717c092ee')
        self.vs[1]["mm__"] = """hasAttr_T"""
        self.vs[1]["GUID__"] = UUID('aef99c75-33c2-4c29-bd64-775b5f06ae3c')
        self.vs[2]["mm__"] = """leftExpr"""
        self.vs[2]["GUID__"] = UUID('f1e605b8-de6c-40a4-aa38-5ffd700176a2')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('218f056f-3b42-47e0-b23a-24157aa072a1')
        self.vs[4]["mm__"] = """hasAttr_S"""
        self.vs[4]["GUID__"] = UUID('0a6341f4-645b-404f-9c4a-2a31af6af8c7')
        self.vs[5]["mm__"] = """ApplyModel"""
        self.vs[5]["GUID__"] = UUID('4060bb50-c666-4a99-aff7-85b3020f1513')
        self.vs[6]["mm__"] = """Female_T"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["name"] = """s_"""
        self.vs[6]["GUID__"] = UUID('30dbdbba-e992-4d8e-8214-f44aa53956c7')
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["name"] = """s_"""
        self.vs[7]["GUID__"] = UUID('353a981b-f21a-4497-baeb-dd78586d60d6')
        self.vs[8]["mm__"] = """Equation"""
        self.vs[8]["GUID__"] = UUID('90c951b0-7a81-40f6-b364-4a32ff93e711')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('3ccf7db2-9099-485f-b4a3-b0c06a68d242')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('dbf1e211-448c-4d55-b012-d043ab74c5d4')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('52278209-fc0b-4fe7-9080-ad81c1008df4')
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["name"] = """name"""
        self.vs[12]["GUID__"] = UUID('499491f3-dfa0-4000-a1a9-47bf3acba82a')
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["name"] = """name"""
        self.vs[13]["GUID__"] = UUID('b966fe5d-3db3-4a29-8533-9248ee256139')

