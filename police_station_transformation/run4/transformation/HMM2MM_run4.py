

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMM2MM_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_run4, self).__init__(name='HMM2MM_run4', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 13), (1, 6), (6, 14), (13, 7), (7, 11), (14, 8), (8, 12), (13, 0), (0, 14), (4, 1), (2, 4), (2, 9), (2, 10), (11, 3), (3, 12), (9, 11), (10, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """MM2MM_run4"""
        self["GUID__"] = UUID('6acb3545-ba46-40f9-b66c-4c77a17bc75c')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('e43a5561-8d6c-492e-b1fe-f5a58db46ed2')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('1d78eb90-962f-43bc-abaa-81d508e4026e')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('556c2279-654d-402f-ab5f-42f54375b6a4')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('070c29ee-eeb5-49bd-903b-6d4a0f1de520')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('c8fe2336-40c5-464c-8eaa-d6f235865965')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('cd9e191e-f343-4307-94f2-83a51b988436')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('884b87a8-e128-4414-8139-2d8b5f5cbacd')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('80e55655-057e-433e-8ee5-833db719ea64')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('f3109b3a-6c6e-4f25-bb51-54071fbb36ef')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('91220133-6a55-4331-82d3-2b9aa9a7c042')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('f90e7a59-5737-41a6-bbbb-f4b68c3e2666')
        self.vs[11]["name"] = """m1"""
        self.vs[11]["classtype"] = """male4"""
        self.vs[11]["mm__"] = """Male_S"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = UUID('c758247e-621f-478c-a0da-5428489492f6')
        self.vs[12]["name"] = """m2"""
        self.vs[12]["classtype"] = """male4"""
        self.vs[12]["mm__"] = """Male_S"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('dfd5bc1b-5c8a-4b98-8e6a-67ef475a1f0c')
        self.vs[13]["name"] = """m"""
        self.vs[13]["classtype"] = """male4"""
        self.vs[13]["mm__"] = """Male_T"""
        self.vs[13]["GUID__"] = UUID('b091481a-ef8c-4040-ba3b-913bc4de57dd')
        self.vs[14]["name"] = """m2"""
        self.vs[14]["classtype"] = """male4"""
        self.vs[14]["mm__"] = """Male_T"""
        self.vs[14]["GUID__"] = UUID('8ca73912-533f-41df-9477-80f1ca1d30dc')

