

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMM2MM_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_run1, self).__init__(name='HMM2MM_run1', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 13), (1, 6), (6, 14), (13, 7), (7, 11), (14, 8), (8, 12), (13, 0), (0, 14), (4, 1), (2, 4), (2, 9), (2, 10), (11, 3), (3, 12), (9, 11), (10, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """MM2MM_run1"""
        self["GUID__"] = UUID('69e361b1-7612-48c0-a91f-94d29ec02cf6')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """m2m"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('167a29fc-0d0f-427c-90d9-3798ecb86532')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('21480ce4-2bb2-4864-a928-76922c88b665')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('11e8be72-b5ca-4b3f-97d0-fc2ed0f9fbe3')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('7c848028-deb3-4b1a-b483-1e6648e563f6')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('efbfc43d-55ab-450c-ad85-5e13df4e4e21')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('5d7ee847-b226-41e1-bc78-c645591b92e7')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('14db9448-6a76-4742-bfdb-0ed05c5af630')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('f811a825-f4ec-4ebc-9c2d-12f3a6c7aa9c')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('57b3f4b6-147f-4958-a330-dee6bb9488ac')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('c0be51f4-a060-409a-ad9a-35e104efdff4')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('719b392f-92de-47ea-86fc-c9d77759705b')
        self.vs[11]["name"] = """6.m1"""
        self.vs[11]["classtype"] = """male1"""
        self.vs[11]["mm__"] = """Male_S"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = UUID('52739ca4-5828-414b-8890-ed97c92b0143')
        self.vs[12]["name"] = """6.m2"""
        self.vs[12]["classtype"] = """male1"""
        self.vs[12]["mm__"] = """Male_S"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('2ca838a7-110d-4047-b486-75659c7e25e3')
        self.vs[13]["name"] = """6.m"""
        self.vs[13]["classtype"] = """male1"""
        self.vs[13]["mm__"] = """Male_T"""
        self.vs[13]["GUID__"] = UUID('f6e4f22c-3275-4239-816a-1487442f6b74')
        self.vs[14]["name"] = """6.m2"""
        self.vs[14]["classtype"] = """male1"""
        self.vs[14]["mm__"] = """Male_T"""
        self.vs[14]["GUID__"] = UUID('16bd9985-81bc-4406-b52d-1626a976ec98')

