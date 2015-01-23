

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_partial(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_partial.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_partial, self).__init__(name='HSM2SM_partial', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([(2, 8), (8, 4), (2, 9), (9, 5), (4, 0), (0, 5), (6, 1), (1, 2), (3, 10), (10, 14), (7, 11), (11, 15), (12, 3), (16, 3), (4, 16), (6, 12), (6, 13), (13, 7), (5, 17), (17, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_partial"""
        self["GUID__"] = UUID('0c348003-dcb8-4c48-ba1a-f1a0add0662b')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('a94ebb3e-7f8e-470f-8412-7e401852f504')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('182878dd-fecc-4a6b-9bab-91b53bfe4a95')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('5bd125a2-0c58-4b3c-be63-08cc716af633')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """1"""
        self.vs[3]["mm__"] = """Station_S"""
        self.vs[3]["cardinality"] = """s_"""
        self.vs[3]["GUID__"] = UUID('251ccf29-e8fc-4954-97a4-b8f47272c578')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """t_"""
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["GUID__"] = UUID('442375fc-2f20-4121-b2a8-ccdd6c17036b')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["GUID__"] = UUID('c93f613e-c858-4c94-ae21-5dfebba644a1')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('046ef3b6-9746-483d-8919-42fc914bc023')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["mm__"] = """Male_S"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["GUID__"] = UUID('c41a737c-44e1-4221-8b84-3c375850b398')
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = UUID('be8bb699-3ff6-405f-ae29-4d948abbbff4')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('1f496c7a-8358-4193-9b6b-95c5d7385c33')
        self.vs[10]["mm__"] = """hasAttr_S"""
        self.vs[10]["GUID__"] = UUID('9e5b0d91-e174-4932-a45f-0f12b7f74b37')
        self.vs[11]["mm__"] = """hasAttr_S"""
        self.vs[11]["GUID__"] = UUID('65dae6a3-694c-4faf-9b3a-a9c387a04717')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('5b3ef3d7-716c-4bf2-aa86-ce5307767395')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('7826ac7d-86fb-404b-96e4-5f8acaebd830')
        self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["GUID__"] = UUID('9f5154f4-9e0a-4e09-a5b6-b7480d19a009')
        self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["GUID__"] = UUID('a38c63ae-5279-4f96-bde4-5dc0040d9c71')
        self.vs[16]["mm__"] = """trace_link"""
        self.vs[16]["GUID__"] = UUID('746bc92d-6a35-4e7a-983e-cbfe7da4cab3')
        self.vs[17]["mm__"] = """trace_link"""
        self.vs[17]["GUID__"] = UUID('8a4d899a-30be-473d-ab8d-8f25c70ec1d9')

