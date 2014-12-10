

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnECU2VirtualDevice(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnECU2VirtualDevice.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnECU2VirtualDevice, self).__init__(name='HConnECU2VirtualDevice', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 6), (3, 13), (13, 1), (3, 14), (14, 5), (3, 15), (15, 8), (1, 9), (1, 17), (7, 2), (2, 3), (8, 16), (16, 4), (17, 4), (5, 18), (18, 6), (9, 5), (5, 10), (10, 8), (11, 4), (12, 6), (7, 11), (7, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """ConnECU2VirtualDevice"""
        self["GUID__"] = UUID('3be4f213-0e4b-49d2-84c6-44949b82b049')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """virtualDevice"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('19b02799-57a0-4b59-8099-07cd24e24491')
        self.vs[1]["name"] = """sysmap1"""
        self.vs[1]["classtype"] = """SystemMapping"""
        self.vs[1]["mm__"] = """SystemMapping"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('4956a301-40b7-4a0a-853b-ae42dfe25aeb')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('0fde8c3b-5cbf-4919-9793-7ae6567a75e7')
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = UUID('c3754f9f-5f5e-44c3-8e5e-ff8cf774614f')
        self.vs[4]["name"] = """ecu1"""
        self.vs[4]["classtype"] = """ECU"""
        self.vs[4]["mm__"] = """ECU"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('9ff16b07-6d24-4d64-9f56-5428941cf908')
        self.vs[5]["name"] = """stem1"""
        self.vs[5]["classtype"] = """SwcToEcuMapping"""
        self.vs[5]["mm__"] = """SwcToEcuMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('e54c2b2c-a084-4c64-85ec-c3e8b8ca9aab')
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('6b171f86-3dd0-4a6f-aeee-0f4378071774')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('bc044fbb-1054-4a44-9323-ca393ea0ff7a')
        self.vs[8]["name"] = """ecuinst1"""
        self.vs[8]["classtype"] = """EcuInstance"""
        self.vs[8]["mm__"] = """EcuInstance"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('075c83f0-7606-441a-b574-feabaa58aa14')
        self.vs[9]["associationType"] = """swMapping"""
        self.vs[9]["mm__"] = """directLink_T"""
        self.vs[9]["GUID__"] = UUID('d33af912-fceb-4418-b4f8-c96aa809b544')
        self.vs[10]["associationType"] = """ecuInstance"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('2d912b60-4f4a-4ff1-badf-0702fb419277')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('39f7be72-1dd4-4792-97a3-10c9694466a6')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('ab0231e1-5de5-4028-ac39-c4af6eade78e')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('3d41e711-a62b-42d6-9d98-fa8f3ef7d64b')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('9081bab9-a9e8-4173-a60e-68daacd3424d')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('ebe0cd73-a521-45ef-8f7a-35a8489c34f5')
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["GUID__"] = UUID('43ac5101-6503-4dc9-aca5-793042468d8b')
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["GUID__"] = UUID('5630626d-750d-4235-87b8-7d45ffc84c74')
        self.vs[18]["mm__"] = """backward_link"""
        self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["GUID__"] = UUID('ec764348-d1fb-4941-8797-50ecfc4c1b05')

