

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst, self).__init__(name='HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([(8, 0), (0, 6), (7, 1), (1, 5), (15, 9), (9, 25), (16, 10), (10, 26), (7, 11), (11, 19), (5, 12), (12, 20), (3, 2), (2, 17), (2, 18), (4, 13), (13, 8), (4, 14), (14, 6), (4, 3), (15, 23), (16, 24), (17, 7), (18, 5), (5, 22), (22, 6), (23, 19), (24, 20), (7, 21), (21, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst"""
        self["GUID__"] = UUID('ac2fe0aa-a87e-451b-8238-208eaa9c91ad')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """outgoingTransitions"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('614a3da7-45b4-4c1d-a49a-1d22e4122b8f')
        self.vs[1]["associationType"] = """p"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('45d983ee-d59c-43f1-aae8-a7cd6ce87a08')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('72feae3b-0bc0-4a49-b887-c8043d339b85')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('3d1e748f-e8a9-42ed-9a38-7d50a68453d3')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('847761fd-86ef-44b6-9f3d-dfc351c67c14')
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('ba9c04f3-9417-4027-b93f-c8083cac4ec0')
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('b7ca7333-4d0d-4257-a396-cbdac03aaa74')
        self.vs[7]["name"] = """par1"""
        self.vs[7]["classtype"] = """Par"""
        self.vs[7]["mm__"] = """Par"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('a1851d89-f1cf-4e2b-ae9f-d85a18345f68')
        self.vs[8]["name"] = """exitpoint1"""
        self.vs[8]["classtype"] = """ExitPoint"""
        self.vs[8]["mm__"] = """ExitPoint"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('c3200ca9-b83f-4c9b-b0a2-5bd97a7f49ee')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('37fe2e9a-73f0-48c2-b52c-385a2a4c809f')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('8741aefb-6f5f-4336-9e66-2c7641169e17')
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = UUID('566e0edd-27b1-47c7-8aad-d8e9f8f6012a')
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = UUID('d7c8fada-028d-4fa1-902f-013f8e20fff2')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('c4d56473-db27-4b34-9533-a767bed8b067')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('2cb08ec1-dd86-4b7e-81bd-0e1d49502b5a')
        self.vs[15]["name"] = """eq1"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = UUID('ed0f87d0-cbf8-4184-8100-fb656dd55072')
        self.vs[16]["name"] = """eq2"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = UUID('01b0a6ec-b525-4a04-8339-a9df73c35fe3')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('b163d938-3ff2-4596-8d68-316273eecc18')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('7225642b-9c8a-4ec8-b5fe-ecba6ae0870c')
        self.vs[19]["name"] = """pivotin"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = UUID('fdea7540-548a-43d1-9a0e-8200b3e50a20')
        self.vs[20]["name"] = """pivotin"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = UUID('493fd822-0570-45bf-9786-4e53bd45a3e0')
        self.vs[21]["type"] = """ruleDef"""
        self.vs[21]["mm__"] = """backward_link"""
        self.vs[21]["GUID__"] = UUID('b96da084-4c40-4fc2-a493-40f77f53adcf')
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["GUID__"] = UUID('6fb62711-e5d4-4e02-9537-3a3470b7e005')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('9189c13e-7c00-4cb0-8d39-d59ae1ccdf84')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('00247f6a-6680-4596-9c24-479bdfe55861')
        self.vs[25]["name"] = """parexitpoint"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('b0ee7e60-5004-4704-9969-be273975f2a8')
        self.vs[26]["name"] = """instfortrans"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('d8e3d3ed-ff9a-4573-91c5-b9a1dc8fab9d')

