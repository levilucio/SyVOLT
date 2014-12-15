

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
        self["GUID__"] = UUID('a5165a35-d067-4e8e-a323-7fa4722e37a0')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('c0bf4911-386b-473c-bcbc-d8844e5a7041')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('5a39e18c-d41d-4cb4-beb3-aa328c5cac26')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('db5edc76-fc4d-419d-8935-17d8f0f19a90')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('eb1fbda0-d590-4461-ac83-611091846697')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('77b22669-524d-4893-aee6-9904be45bf30')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('d9eaf6ed-c5be-4e12-a8cb-02886b4b1c54')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('e39ba9b2-c41b-4635-b6a5-08e698b4aff4')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('5316299e-40dc-4425-b635-3f80f7d6cb6c')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('c203a6ae-3708-4622-924a-27b7ad0efa18')
        self.vs[9]["name"] = """s_"""
        self.vs[9]["classtype"] = """t_"""
        self.vs[9]["mm__"] = """Female_T"""
        self.vs[9]["GUID__"] = UUID('b551e105-bfa3-415e-b3f0-814e5a3200af')
        self.vs[10]["name"] = """s_"""
        self.vs[10]["classtype"] = """t_"""
        self.vs[10]["mm__"] = """Female_T"""
        self.vs[10]["GUID__"] = UUID('96c2fe7c-56ed-4001-a164-67d78b41caef')
        self.vs[11]["name"] = """s_"""
        self.vs[11]["classtype"] = """1"""
        self.vs[11]["mm__"] = """Female_S"""
        self.vs[11]["cardinality"] = """s_"""
        self.vs[11]["GUID__"] = UUID('06925961-9c12-4c77-aff3-8d837da79749')
        self.vs[12]["name"] = """s_"""
        self.vs[12]["classtype"] = """1"""
        self.vs[12]["mm__"] = """Female_S"""
        self.vs[12]["cardinality"] = """s_"""
        self.vs[12]["GUID__"] = UUID('dc45b2e9-7e78-4c4f-987a-b4b491b553ad')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('dd85854b-022d-4b2a-b8ca-b5cbf9e2da2e')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('683e3a4e-8776-49bb-84cf-74b6c92d77d3')

