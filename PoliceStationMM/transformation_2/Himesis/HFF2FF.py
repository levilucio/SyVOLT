

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HFF2FF(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF, self).__init__(name='HFF2FF', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(2, 5), (5, 9), (2, 6), (6, 10), (9, 0), (0, 10), (4, 1), (1, 2), (9, 7), (7, 11), (10, 8), (8, 12), (11, 3), (3, 12), (13, 11), (14, 12), (4, 13), (4, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """FF2FF"""
        self["GUID__"] = UUID('4024dbb7-41b3-42f9-85be-35c362e6023e')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('8f6b20a9-0f46-462e-a3d4-591498ea4d1d')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('88ad3769-3bb1-4ba4-bbc8-eb1971240c7c')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('fc80f7cc-ff93-437a-b2b6-6338f3d97511')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('67df0634-1a3d-4b21-a454-975f63534598')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('3a475b0a-2a40-456f-a934-dd8a8a959437')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('492f1392-7441-4dce-bf62-1bb114e55063')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('388b9eb8-cadd-47ca-ae12-12b97cceef9a')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('b1d8eefa-a408-454c-ac93-b8b5c16de267')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('081d4b39-4234-48c0-9244-d1f90de03cd5')
        self.vs[9]["name"] = """s_"""
        self.vs[9]["classtype"] = """t_"""
        self.vs[9]["mm__"] = """Female_T"""
        self.vs[9]["GUID__"] = UUID('6726a9bd-70c1-4ff8-9400-08519e9541f6')
        self.vs[10]["name"] = """s_"""
        self.vs[10]["classtype"] = """t_"""
        self.vs[10]["mm__"] = """Female_T"""
        self.vs[10]["GUID__"] = UUID('a5e387d6-64cb-46b5-b48b-9f90e347a7f7')
        self.vs[11]["name"] = """s_"""
        self.vs[11]["classtype"] = """1"""
        self.vs[11]["mm__"] = """Female_S"""
        self.vs[11]["cardinality"] = """s_"""
        self.vs[11]["GUID__"] = UUID('614c1b74-8f4d-4958-baa3-3db017935d23')
        self.vs[12]["name"] = """s_"""
        self.vs[12]["classtype"] = """1"""
        self.vs[12]["mm__"] = """Female_S"""
        self.vs[12]["cardinality"] = """s_"""
        self.vs[12]["GUID__"] = UUID('f9f3752b-de4b-4399-8d81-99591477481c')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('d4aab556-ad6a-4d52-9266-be701a3fb222')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('5489f660-6c09-4077-a3a4-8313fc640cf9')

