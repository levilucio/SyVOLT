

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnVirtualDeviceToDistributable(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnVirtualDeviceToDistributable.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnVirtualDeviceToDistributable, self).__init__(name='HConnVirtualDeviceToDistributable', num_nodes=26, edges=[])
        
        # Add the edges
        self.add_edges([(5, 10), (10, 7), (7, 11), (11, 0), (3, 18), (18, 4), (3, 19), (19, 6), (3, 20), (20, 2), (3, 21), (21, 9), (17, 0), (24, 0), (25, 0), (8, 1), (1, 3), (4, 22), (22, 5), (6, 23), (23, 7), (9, 24), (2, 25), (12, 2), (2, 13), (4, 12), (13, 4), (6, 14), (14, 9), (15, 5), (16, 7), (8, 15), (8, 16), (8, 17)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """ConnVirtualDeviceToDistributable"""
        self["GUID__"] = UUID('d799922f-af2b-4ada-a379-addbff890be0')
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('87b17c59-273e-41a1-88f3-a19cb4ac5cdd')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('cb2786c0-7d2c-4a62-a2a2-b14814822495')
        self.vs[2]["name"] = """comp1"""
        self.vs[2]["classtype"] = """ComponentPrototype"""
        self.vs[2]["mm__"] = """ComponentPrototype"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('3ff2ba74-068b-4dba-b2ab-7469407e65aa')
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = UUID('111cff03-67a6-470c-90c6-9f02149ba523')
        self.vs[4]["name"] = """composty1"""
        self.vs[4]["classtype"] = """CompositionType"""
        self.vs[4]["mm__"] = """CompositionType"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('9aa826fd-72b9-4900-a101-6d101ec6a929')
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = UUID('8bf95358-1439-405a-8ac9-e16615a52562')
        self.vs[6]["name"] = """stem1"""
        self.vs[6]["classtype"] = """SwcToEcuMapping"""
        self.vs[6]["mm__"] = """SwcToEcuMapping"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('2afa5aa2-dfd9-4a79-9fd1-a1d32f3d3ef6')
        self.vs[7]["name"] = """vd1"""
        self.vs[7]["classtype"] = """VirtualDevice"""
        self.vs[7]["mm__"] = """VirtualDevice"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('f0f0bcf1-b43d-456a-b664-540d499cc206')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('f0a942df-2da9-45ba-936e-7090d9b38e3b')
        self.vs[9]["name"] = """sctemc1"""
        self.vs[9]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[9]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('737e5222-d413-442c-b3d7-03f4fb4778bf')
        self.vs[10]["associationType"] = """virtualDevice"""
        self.vs[10]["mm__"] = """directLink_S"""
        self.vs[10]["GUID__"] = UUID('3314e56b-8d14-424d-ac04-00ced8275558')
        self.vs[11]["associationType"] = """distributable"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = UUID('b8be36d6-8af8-4a98-81e8-2a56f2748610')
        self.vs[12]["associationType"] = """component"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('922b6bae-5042-4646-8c80-5e5a586bc294')
        self.vs[13]["associationType"] = """type"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = UUID('77dcbd5e-0151-4e30-8250-41cdcfc8f968')
        self.vs[14]["associationType"] = """component"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = UUID('bf0012e1-0166-46eb-8d90-338cf8e41fa2')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('62c2597c-7050-40a9-aee0-92e138760588')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('a71502c1-4a0a-480c-a6a6-848b1c183943')
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = UUID('209a01fe-bf07-4f08-b4cf-e22772a7f842')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('1097a4e2-499f-45d8-9f52-2b9757fe0a14')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('c9b15701-7dc2-40c4-aa9a-91caced2a0d8')
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = UUID('6a6af713-9eec-4f63-a1a8-aeea275cfd23')
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = UUID('f9652c10-838b-4e0b-a4dc-32edeef6fcbc')
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["GUID__"] = UUID('bce8ac63-5740-4f3c-b1e3-831ee54fdf8f')
        self.vs[23]["mm__"] = """backward_link"""
        self.vs[23]["type"] = """ruleDef"""
        self.vs[23]["GUID__"] = UUID('ca1072b0-c9c6-42c6-88fa-c4682a5df4f0')
        self.vs[24]["mm__"] = """backward_link"""
        self.vs[24]["type"] = """ruleDef"""
        self.vs[24]["GUID__"] = UUID('4a5ebc99-fe60-47ca-babb-04b787f7a4b8')
        self.vs[25]["mm__"] = """backward_link"""
        self.vs[25]["type"] = """ruleDef"""
        self.vs[25]["GUID__"] = UUID('36cb4950-71ff-4a81-8142-3835aec06188')

