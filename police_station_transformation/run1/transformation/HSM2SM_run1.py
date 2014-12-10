

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_run1, self).__init__(name='HSM2SM_run1', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 7), (5, 11), (11, 6), (7, 12), (12, 4), (5, 0), (0, 7), (8, 1), (2, 8), (2, 13), (2, 14), (6, 3), (3, 4), (13, 6), (14, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_run1"""
        self["GUID__"] = UUID('41de9224-7702-4c94-8fcf-aa9866fde8fd')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """s2m"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('093d51c8-9bd2-4438-84b1-c7b04e61c511')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('6eca1311-b6bb-467a-8fda-fa488429cb78')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('216245fd-9872-4215-a4e2-5ff92c8ac0cc')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('e9823e8e-581e-4ff5-a237-decacabfdfbd')
        self.vs[4]["name"] = """4.m"""
        self.vs[4]["classtype"] = """male1"""
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('66f60d0a-10c6-48ee-904f-8892b7593a57')
        self.vs[5]["name"] = """4.s"""
        self.vs[5]["classtype"] = """station1"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('25f8f13e-688d-49c2-a236-b32a94a8a0a8')
        self.vs[6]["name"] = """4.s"""
        self.vs[6]["classtype"] = """station1"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('9e2c90f0-b024-46bd-b8ce-97500b5b0f8e')
        self.vs[7]["name"] = """4.m"""
        self.vs[7]["classtype"] = """male1"""
        self.vs[7]["mm__"] = """Male_T"""
        self.vs[7]["GUID__"] = UUID('633dce68-d89d-4137-ba3e-6620ca9df1ba')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('3c76abac-7727-46a9-917b-245d4556edf9')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('62aca1b1-2c26-41ba-94ed-817c8e0d21e1')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('bc5da071-f40d-4aed-b86b-2bb1a65e17d9')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('8b297282-4c6e-460a-882c-7e49a1e4992c')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('081d2126-9d8a-446f-ba9c-86f4049943b5')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('92c1360a-025e-4631-ba54-390adbfc25c2')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('3fd93264-27a5-42ec-b43a-f3b5eea9551e')

