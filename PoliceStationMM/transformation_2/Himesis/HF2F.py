

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
        self.add_edges([(7, 0), (0, 12), (6, 1), (1, 9), (4, 2), (2, 10), (8, 3), (3, 6), (8, 4), (10, 5), (7, 11), (11, 9)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'mbeddr2C_MM'
p2
aS'PoliceStationMM'
p3
a.""")
        self["name"] = """F2F"""
        self["GUID__"] = UUID('5effb004-32ce-4d12-8166-cbd3b4b92b45')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """rightExpr"""
        self.vs[0]["GUID__"] = UUID('45174b99-b6de-42a1-8755-1f1a5b076661')
        self.vs[1]["mm__"] = """hasAttr_S"""
        self.vs[1]["GUID__"] = UUID('2fb07509-9caa-434c-8c35-df2a0eadd61f')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('2b923210-dcf2-43df-a6df-36707ce79ff2')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('00d2afcb-1844-4d9c-aaac-382ad042feb5')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('2942613e-ce95-4b82-b768-8947aca8a35e')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Female_T"""
        self.vs[5]["GUID__"] = UUID('a2908be3-778c-41d2-aa90-a1d4c3eda28b')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """1"""
        self.vs[6]["mm__"] = """Female_S"""
        self.vs[6]["cardinality"] = """s_"""
        self.vs[6]["GUID__"] = UUID('3059e37e-c2c6-4280-9632-2e720c0ae3cb')
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = UUID('9b6c2500-91a9-47bb-bf76-5384e783ce37')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('92594e15-ae09-4000-b5ce-e2ac0cdcea01')
        self.vs[9]["name"] = """name"""
        self.vs[9]["mm__"] = """Attribute"""
        self.vs[9]["GUID__"] = UUID('23389ef2-aa4a-4582-8cb7-b793f46646fb')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('00033596-ec78-4545-bef4-119238c4e64e')
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = UUID('5de94549-ef23-4d10-9b43-2c2f21b21975')
        self.vs[12]["value"] = """somefemale"""
        self.vs[12]["mm__"] = """Constant"""
        self.vs[12]["GUID__"] = UUID('a7bd8818-04f5-4cbc-a52a-daebc1b35b65')

