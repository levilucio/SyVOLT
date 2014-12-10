

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMM2MM_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_run3, self).__init__(name='HMM2MM_run3', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 13), (1, 6), (6, 14), (13, 7), (7, 11), (14, 8), (8, 12), (13, 0), (0, 14), (4, 1), (2, 4), (2, 9), (2, 10), (11, 3), (3, 12), (9, 11), (10, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """MM2MM_run3"""
        self["GUID__"] = UUID('28d5c809-4523-4d28-9c75-0b2257e3f07e')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('3007a586-1c7a-44e5-b23d-7a761b83074a')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('9dfa4dea-1a46-4fe3-b1f8-a19005fb832f')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('72c7dfd6-802b-4723-b0ae-f7c809779d8e')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('3712882f-c6f7-4cd0-a17e-8769e1eec87f')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('f2acd2e2-fe8b-46e9-a10d-fc6e452c5108')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('f06083f8-5a41-475a-b9e7-eed24940ce8a')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('63cb6c6a-f482-4392-9f5d-238b7cdb3ee2')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('691317ae-7a06-4d83-a380-43c6ca154b8c')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('a187204f-8f78-456a-a274-b86d4f0f4447')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('adf3d92f-6828-425b-a4f8-9f65498cd1b4')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('0c0f065e-6afe-47b8-944a-c63c64d5d055')
        self.vs[11]["name"] = """m1"""
        self.vs[11]["classtype"] = """male3"""
        self.vs[11]["mm__"] = """Male_S"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = UUID('96044654-e2a9-4ff9-a0e3-9388d35c5413')
        self.vs[12]["name"] = """m2"""
        self.vs[12]["classtype"] = """male3"""
        self.vs[12]["mm__"] = """Male_S"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('7e091346-23ac-4096-a521-e10a5062d500')
        self.vs[13]["name"] = """m"""
        self.vs[13]["classtype"] = """male3"""
        self.vs[13]["mm__"] = """Male_T"""
        self.vs[13]["GUID__"] = UUID('e80ad331-4a80-4c12-b3a1-a1fc971e77b6')
        self.vs[14]["name"] = """m2"""
        self.vs[14]["classtype"] = """male3"""
        self.vs[14]["mm__"] = """Male_T"""
        self.vs[14]["GUID__"] = UUID('bbaf3a92-6945-404b-9574-ad94ace40e3f')

