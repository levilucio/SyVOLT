

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
        self["GUID__"] = UUID('f21d40aa-28d8-4c34-b01d-0c36cd03b7e4')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('b1b2b988-dff0-4f04-b925-26c5eed7274f')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('39a53c1c-398e-4bd0-b8f6-81258ab1e9bd')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('e9f684b0-af47-4851-bb50-4a05be5da622')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('93287002-bf23-44b2-8e72-00ed92221cbd')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('d0b7a91f-7463-4773-aee7-33fca1f30d13')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('5ea46137-db9c-4324-b890-63fcefe94c05')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('73940a5d-9dd3-40a9-af6b-3acaaf3876fd')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('d28b672d-f3f1-4c70-b8f5-d93f58504f85')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('e23bfcac-3889-47e0-91d6-7066e2cbf489')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('90118640-ec6d-4f22-acc8-35f19be01a2a')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('7e26d555-1fb4-4605-8120-7b97b6ecfb87')
        self.vs[11]["name"] = """s_"""
        self.vs[11]["classtype"] = """t_"""
        self.vs[11]["mm__"] = """Male_T"""
        self.vs[11]["GUID__"] = UUID('fd66dac7-f7dc-4d4a-931e-179bfc0c3258')
        self.vs[12]["name"] = """s_"""
        self.vs[12]["classtype"] = """t_"""
        self.vs[12]["mm__"] = """Male_T"""
        self.vs[12]["GUID__"] = UUID('6b96e742-bf38-4372-93d7-5ac3f66d5e36')
        self.vs[13]["name"] = """s_"""
        self.vs[13]["classtype"] = """1"""
        self.vs[13]["mm__"] = """Male_S"""
        self.vs[13]["cardinality"] = """s_"""
        self.vs[13]["GUID__"] = UUID('2727158b-89fb-427c-b1ca-a7c59f80a619')
        self.vs[14]["name"] = """s_"""
        self.vs[14]["classtype"] = """1"""
        self.vs[14]["mm__"] = """Male_S"""
        self.vs[14]["cardinality"] = """s_"""
        self.vs[14]["GUID__"] = UUID('fbc2425d-334b-4336-bd4a-03007f4d5848')

