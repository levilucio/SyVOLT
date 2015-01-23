

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_complete(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_complete.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_complete, self).__init__(name='HSM2SM_complete', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 5), (2, 10), (10, 6), (5, 0), (0, 6), (7, 1), (1, 2), (4, 11), (11, 15), (8, 12), (12, 16), (4, 3), (3, 8), (13, 4), (17, 4), (5, 17), (7, 13), (7, 14), (14, 8), (6, 18), (18, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_complete"""
        self["GUID__"] = UUID('2e49d513-b4bf-4f77-8e61-a3404344c09a')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('2a159334-0e59-4513-a717-986d93cce7f4')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('5b5bd5de-b019-4aa5-a3a0-659ed308f4b8')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('94909678-0fd6-405a-8284-00ae9cdbf8bb')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('cd05bb22-31e9-49ab-9ce5-c65a75a384de')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """1"""
        self.vs[4]["mm__"] = """Station_S"""
        self.vs[4]["cardinality"] = """s_"""
        self.vs[4]["GUID__"] = UUID('562b76aa-6a5b-4f8a-a784-aff3af24df7c')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('eda9e25d-d0c3-45ad-990d-be9f74ec80e4')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Male_T"""
        self.vs[6]["GUID__"] = UUID('bd7b3b05-0663-40cb-b1cd-798a405c1791')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('826fdd58-a55c-4402-a923-1b1b0b118a13')
        self.vs[8]["name"] = """s_"""
        self.vs[8]["classtype"] = """1"""
        self.vs[8]["mm__"] = """Male_S"""
        self.vs[8]["cardinality"] = """s_"""
        self.vs[8]["GUID__"] = UUID('a1084859-5f1b-4537-a219-9e38775780f5')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('88c26ea7-a39d-45ee-b218-1cb636f88ab4')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('d3cd0220-286b-4b01-b387-2f5808907824')
        self.vs[11]["mm__"] = """hasAttr_S"""
        self.vs[11]["GUID__"] = UUID('69a4a7a2-2315-49c9-ad7c-44d98b4da223')
        self.vs[12]["mm__"] = """hasAttr_S"""
        self.vs[12]["GUID__"] = UUID('5690f094-dbca-4001-a5dd-85a276b4c985')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('93ae39fd-9e1b-436d-87ed-e8ea2ad6de48')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('af32cd0f-ac67-46f6-aa23-2405bad2f532')
        self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["GUID__"] = UUID('8dbf5d82-deb7-4d3a-a95e-94f386557d62')
        self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = UUID('dd7aabe2-c7c3-45f0-b724-d219378195df')
        self.vs[17]["mm__"] = """trace_link"""
        self.vs[17]["GUID__"] = UUID('243ad50c-fbc8-42a0-813b-763c015a48b2')
        self.vs[18]["mm__"] = """trace_link"""
        self.vs[18]["GUID__"] = UUID('c88ac433-1189-48a9-bbed-ab10639d0f75')

