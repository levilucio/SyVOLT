

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMM2MM(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM, self).__init__(name='HMM2MM', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(2, 5), (5, 11), (2, 6), (6, 12), (11, 0), (0, 12), (4, 1), (1, 2), (11, 7), (7, 13), (12, 8), (8, 14), (13, 3), (3, 14), (4, 9), (9, 13), (4, 10), (10, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """MM2MM"""
        self["GUID__"] = UUID('1a23cb2d-d829-46ef-948a-ba47383ac675')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('8a787718-e182-4886-856a-dac424d3e1f5')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('94322776-f7db-4af6-893a-bfcaca92ed6a')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('c06aad11-06c4-4fcb-ab57-3517527736c9')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('480c626e-a429-421f-aed8-85079644e950')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('91182c47-3017-411d-8156-4ab62c057452')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('15d19bc2-ad86-4f36-864c-7ad2f2452d58')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('912dec40-70e9-463e-91bb-e0d839e35381')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('71db8ad7-61ca-43e3-a149-6772a3a3fd06')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('d5d6e7e7-0ec8-4912-89fb-7d946ad1c5d4')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('691ace40-beb1-4535-958f-d4aed3877ed0')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('75d33660-4d2d-4938-a22a-798fd544e236')
        self.vs[11]["name"] = """s_"""
        self.vs[11]["classtype"] = """t_"""
        self.vs[11]["mm__"] = """Male_T"""
        self.vs[11]["GUID__"] = UUID('784366d7-0f99-4562-9223-568fa6a9ae48')
        self.vs[12]["name"] = """s_"""
        self.vs[12]["classtype"] = """t_"""
        self.vs[12]["mm__"] = """Male_T"""
        self.vs[12]["GUID__"] = UUID('62a6a86b-d0e5-4176-8f50-43be4b086dfd')
        self.vs[13]["name"] = """s_"""
        self.vs[13]["classtype"] = """1"""
        self.vs[13]["mm__"] = """Male_S"""
        self.vs[13]["cardinality"] = """s_"""
        self.vs[13]["GUID__"] = UUID('9c25d4bf-9069-4b14-aa59-4fe55f9025f2')
        self.vs[14]["name"] = """s_"""
        self.vs[14]["classtype"] = """1"""
        self.vs[14]["mm__"] = """Male_S"""
        self.vs[14]["cardinality"] = """s_"""
        self.vs[14]["GUID__"] = UUID('056f13b6-2ed7-4aa3-8890-49a9e063190d')

