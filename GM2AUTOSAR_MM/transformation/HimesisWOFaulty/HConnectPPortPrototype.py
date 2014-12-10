

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnectPPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectPPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectPPortPrototype, self).__init__(name='HConnectPPortPrototype', num_nodes=23, edges=[])
        
        # Add the edges
        self.add_edges([(7, 14), (14, 8), (8, 15), (15, 0), (0, 16), (16, 9), (9, 17), (17, 10), (5, 12), (12, 6), (5, 13), (13, 2), (20, 0), (11, 1), (1, 5), (4, 2), (6, 3), (3, 7), (6, 4), (18, 7), (19, 8), (21, 9), (22, 10), (11, 18), (11, 19), (11, 20), (11, 21), (11, 22)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """ConnectPPortPrototype"""
        self["GUID__"] = UUID('7be912d7-8f4c-45c8-a60b-40379e662c73')
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('dde7c5e5-9bfb-483d-af50-9ec3ad3ea954')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('fdadb6ac-433c-4ef5-8449-7a2ea18efcd1')
        self.vs[2]["name"] = """pport1"""
        self.vs[2]["classtype"] = """PPortPrototype"""
        self.vs[2]["mm__"] = """PPortPrototype"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('e42d9358-5729-45a8-a839-baeefb42da1e')
        self.vs[3]["mm__"] = """backward_link"""
        self.vs[3]["type"] = """ruleDef"""
        self.vs[3]["GUID__"] = UUID('29df13e6-889a-4091-94ae-c6d5998a6da6')
        self.vs[4]["associationType"] = """port"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = UUID('8ecba722-7e05-47ef-af3f-9012236d66a7')
        self.vs[5]["mm__"] = """ApplyModel"""
        self.vs[5]["GUID__"] = UUID('51a121d0-c136-4906-927c-58aa11a36c4c')
        self.vs[6]["name"] = """composty1"""
        self.vs[6]["classtype"] = """CompositionType"""
        self.vs[6]["mm__"] = """CompositionType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('ccd8450d-dfb3-46c3-a4f3-f9d62b948842')
        self.vs[7]["name"] = """ecu1"""
        self.vs[7]["classtype"] = """ECU"""
        self.vs[7]["mm__"] = """ECU"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('004d014f-5f9e-45b8-adf7-c56e58c1de30')
        self.vs[8]["name"] = """vd1"""
        self.vs[8]["classtype"] = """VirtualDevice"""
        self.vs[8]["mm__"] = """VirtualDevice"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('203b794d-83e1-4f91-874f-d5e8c61b2ea7')
        self.vs[9]["name"] = """ef1"""
        self.vs[9]["classtype"] = """ExecFrame"""
        self.vs[9]["mm__"] = """ExecFrame"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = UUID('6b3f4dc5-df6a-4ebb-9eb9-a3d0ae43aa99')
        self.vs[10]["name"] = """s1"""
        self.vs[10]["classtype"] = """Signal"""
        self.vs[10]["mm__"] = """Signal"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('5c4353ca-02a7-45b4-b18d-5ce19708e6b4')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('38eaa9bb-e095-4006-beb6-bbdae26a2097')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('1a292446-c398-46fb-b6f0-a315236c3bb8')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('d5d5c08a-32d2-4e98-89c0-0261e699522f')
        self.vs[14]["associationType"] = """virtualDevice"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('72894285-f8b9-48f4-9920-b08046e695e3')
        self.vs[15]["associationType"] = """distributable"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('2a41be14-69be-458f-8ad5-81c9ae0edf7a')
        self.vs[16]["associationType"] = """execFrame"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('816956ee-1648-4785-83dd-65bf536d04f9')
        self.vs[17]["associationType"] = """provided"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('4248937e-1e48-45d2-8d25-f9dc7b7bcfb3')
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = UUID('ce6d1f96-357e-42b9-abaa-12f019e2445f')
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = UUID('d618a91c-de03-47ba-8127-6f5e9e9829b3')
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = UUID('129c7f03-9c03-4b35-9fa6-a4a0a1850f4f')
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = UUID('3a311184-3cc5-4a07-81d5-8673de0548ab')
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = UUID('04e467f1-cd01-4a97-aca8-95120696a5d6')

