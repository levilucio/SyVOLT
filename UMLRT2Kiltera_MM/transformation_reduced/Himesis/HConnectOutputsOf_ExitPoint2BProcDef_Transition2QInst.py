

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
        self["GUID__"] = UUID('bd68c01f-1da7-4411-9f23-ffa4217067da')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """outgoingTransitions"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('d3b22400-92e3-46ba-bddb-84e97498cd44')
        self.vs[1]["associationType"] = """p"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('5b74e80c-456f-44e2-b62f-a0f89f33597e')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('316bf598-c41f-48e3-bcf4-fcdb1b30023e')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('187a14b3-62d2-4559-9731-a5e33683861f')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('56c7a360-e38c-44ba-a99d-a3b17ebd25a4')
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('3f86931b-e659-49e0-a26c-708bb40cca45')
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('1d1da977-2f97-4bd3-a744-956fbb48fbea')
        self.vs[7]["name"] = """par1"""
        self.vs[7]["classtype"] = """Par"""
        self.vs[7]["mm__"] = """Par"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('841b58b3-6426-4d2d-8759-6951de78dd99')
        self.vs[8]["name"] = """exitpoint1"""
        self.vs[8]["classtype"] = """ExitPoint"""
        self.vs[8]["mm__"] = """ExitPoint"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('acd54885-48d0-4ac4-ae89-08d134da5f75')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('c928c2ce-fe84-40d7-8bea-36dfd18fff7a')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('2705d77b-b40a-4acc-a0d4-b50a313d69a3')
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = UUID('848e85e8-a923-4e45-8a9c-38a949fdd3f7')
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = UUID('1578c001-cb97-43f1-a7ed-019daf68dda4')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('603b3652-1954-4dd0-82ae-3e05ee394b23')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('e667e11a-2a4e-472a-b4e4-3f9eb9f42147')
        self.vs[15]["name"] = """eq1"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = UUID('75e7ac96-b683-4f55-b42b-7c5cd5abcb70')
        self.vs[16]["name"] = """eq2"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = UUID('52dd67d9-6615-4a7e-8c6e-5939f6f33246')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('577f83af-c3f9-43bf-9d19-1c6554d07b6b')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('5a3f7cfb-54bc-4ed0-9601-9610c3240810')
        self.vs[19]["name"] = """pivot"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = UUID('86f90288-3da7-4580-8d19-d6700e099bd5')
        self.vs[20]["name"] = """pivot"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = UUID('ae476456-2f8b-48da-acca-5c69d0e43f85')
        self.vs[21]["type"] = """ruleDef"""
        self.vs[21]["mm__"] = """backward_link"""
        self.vs[21]["GUID__"] = UUID('1bb73f30-bb40-454c-8061-0672f37cd426')
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["GUID__"] = UUID('4e3aa65c-fe51-4523-a0c6-aa0e9bb50b5c')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('a871980d-48a3-4f1e-93e8-ef582b6f6872')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('52ab12ca-f21f-4fd1-80cf-cb5d7955ede1')
        self.vs[25]["name"] = """parexitpoint"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('7135c405-4b44-4a03-a568-56358bed2612')
        self.vs[26]["name"] = """instfortrans"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('49314554-0cca-467a-90bf-85a668b7160b')

