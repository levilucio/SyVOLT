

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
        self["GUID__"] = UUID('f766bb59-4b92-4253-87ab-c85b9610abcc')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('8e3567e7-7873-4788-9f00-fdcee50e7e9e')
        self.vs[1]["mm__"] = """leftExpr"""
        self.vs[1]["GUID__"] = UUID('791cf657-1d82-4b9b-8c92-202c31c302c4')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('8e1d4569-c74e-4550-a795-e2d298a060f7')
        self.vs[3]["mm__"] = """hasAttr_S"""
        self.vs[3]["GUID__"] = UUID('262811d6-d77e-44b1-80bb-b8840d5fa4d9')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('fd05f545-3304-4d57-ab94-3382a232aba5')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Female_T"""
        self.vs[5]["GUID__"] = UUID('56d12824-a9e5-445c-ab3f-583fe0fa2edf')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """1"""
        self.vs[6]["mm__"] = """Female_S"""
        self.vs[6]["cardinality"] = """s_"""
        self.vs[6]["GUID__"] = UUID('dffc0c52-1243-44a7-8be0-8fa4e61fedf5')
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = UUID('82e0457b-a9c1-4f89-8bb2-07b74b274adc')
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = UUID('46b17f2c-fb1c-446c-8b07-772075ddce96')
        self.vs[9]["value"] = """somestation"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["GUID__"] = UUID('98da730c-0f77-4465-99e6-3d912b6f5a53')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('103e0dcf-9318-4af5-bea9-9c95a35d6110')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('9a1b3fc0-3545-49ab-81da-07b1512311e4')
        self.vs[12]["name"] = """name"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = UUID('521f89e2-9f6d-4938-b818-3fe3aebc9834')

