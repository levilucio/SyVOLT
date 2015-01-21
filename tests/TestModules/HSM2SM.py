

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM, self).__init__(name='HSM2SM', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 5), (2, 10), (10, 6), (5, 0), (0, 6), (7, 1), (1, 2), (4, 3), (3, 8), (11, 4), (13, 4), (5, 13), (7, 11), (7, 12), (12, 8), (6, 14), (14, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM"""
        self["GUID__"] = UUID('48342a5f-199c-425b-a5f3-2b5aed60edc8')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('e1ccb60d-73f7-4af7-8dd1-c7fc476dd39e')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('e5bf6586-4835-4082-bf6f-68ab79106240')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('bee83c1d-adaa-4058-aca2-68d5a4c5b073')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('3ff1f3bc-ad1f-460d-97ca-c61e42a16f94')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """1"""
        self.vs[4]["mm__"] = """Station_S"""
        self.vs[4]["cardinality"] = """s_"""
        self.vs[4]["GUID__"] = UUID('b6332978-430f-4146-b4ae-3b242a919734')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('b207b38f-3f01-4c06-99dc-82ec892d0d68')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Male_T"""
        self.vs[6]["GUID__"] = UUID('94aadab4-df6a-4fad-9a74-cc8c834589e3')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('d997be42-8341-4064-88ac-9d4a9c7d6694')
        self.vs[8]["name"] = """s_"""
        self.vs[8]["classtype"] = """1"""
        self.vs[8]["mm__"] = """Male_S"""
        self.vs[8]["cardinality"] = """s_"""
        self.vs[8]["GUID__"] = UUID('9648d762-49a1-4b78-8d2c-6c2ee2647968')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('28d6975c-ea8f-45d8-92de-edc4ab449ccb')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('988dc6cb-b510-4396-9c5a-4f8016d0a409')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('c90b468c-59fe-44bf-adc7-fb68ba1f8108')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('7d5d8353-6350-46fa-9a7a-99d7555fe27a')
        self.vs[13]["mm__"] = """trace_link"""
        self.vs[13]["GUID__"] = UUID('533ce21d-4c86-4c49-b7b8-8a9e541dea59')
        self.vs[14]["mm__"] = """trace_link"""
        self.vs[14]["GUID__"] = UUID('2bca0e3b-c664-45af-a54e-763070912769')

