

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_run3, self).__init__(name='HSM2SM_run3', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 7), (5, 11), (11, 6), (7, 12), (12, 4), (5, 0), (0, 7), (8, 1), (2, 8), (2, 13), (2, 14), (6, 3), (3, 4), (13, 6), (14, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_run3"""
        self["GUID__"] = UUID('62bc211d-f3de-4261-9dee-2eee9a9d2eb6')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('69308b57-d03a-477b-8d7c-3010672dd178')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('74450e7c-0776-4612-b1a6-e8b5ab8190e2')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('b3c4ac84-3d19-4c33-ae74-5466b41a7212')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('28163d09-7aeb-4208-9dc7-14a3cd1cd98a')
        self.vs[4]["name"] = """m"""
        self.vs[4]["classtype"] = """male3"""
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('3a4abd6d-fbfe-4109-9a3b-41b7ed02d8d2')
        self.vs[5]["name"] = """s"""
        self.vs[5]["classtype"] = """station3"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('84f38ea8-3b7e-40fc-87c8-1e484d80b94f')
        self.vs[6]["name"] = """s"""
        self.vs[6]["classtype"] = """station3"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('b8440a6e-540e-41da-9d2d-6c9e6c29981b')
        self.vs[7]["name"] = """m"""
        self.vs[7]["classtype"] = """male3"""
        self.vs[7]["mm__"] = """Male_T"""
        self.vs[7]["GUID__"] = UUID('b8707d2b-2960-487e-8e46-347e231738b5')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('2a27d070-a2c7-48d5-b121-457732526673')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('77c3e075-fbad-4db4-bb4d-5c9296527e89')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('7968ba71-aff6-4c0f-89b1-be17afdb0073')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('a1278222-280c-4b52-bfbd-4a6c3ae13b9a')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('e27743ed-f098-41c8-92aa-8d1c7628ecbd')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('963b345d-393d-408a-9bab-c2552f9d628f')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('f871e0bb-0405-4d47-bc17-c5067e90c085')

