

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst, self).__init__(name='HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([(8, 0), (0, 6), (7, 1), (1, 5), (15, 9), (9, 25), (16, 10), (10, 26), (7, 11), (11, 19), (5, 12), (12, 20), (3, 2), (2, 17), (2, 18), (4, 13), (13, 8), (4, 14), (14, 6), (4, 3), (15, 23), (16, 24), (17, 7), (18, 5), (5, 22), (22, 6), (23, 19), (24, 20), (7, 21), (21, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst"""
        self["GUID__"] = UUID('3d748ef2-0367-41d7-b7cc-f140fee0a687')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """outgoingTransitions"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('964f3547-f8b7-4284-8965-80772964f697')
        self.vs[1]["associationType"] = """p"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('fdcb654e-27bc-4ca8-9edf-9221a0dfe73d')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('3ca84416-672f-4d36-9f1e-799486f2f264')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('34080af9-4890-446a-8526-e307ee4b6911')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('16d6ae0e-e9ef-489a-a364-560a98010677')
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('93094366-b094-4f6f-ace0-3d29fbff5b1e')
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('ac7a9846-dcdc-4a6f-b086-46649854fd4c')
        self.vs[7]["name"] = """par1"""
        self.vs[7]["classtype"] = """Par"""
        self.vs[7]["mm__"] = """Par"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('0b0a9a45-c975-4660-ad6e-19ddc626e6e8')
        self.vs[8]["name"] = """exitpoint1"""
        self.vs[8]["classtype"] = """ExitPoint"""
        self.vs[8]["mm__"] = """ExitPoint"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('59596cc2-93d9-496d-9482-edd5f834efd4')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('95f1e009-3242-4ca3-8c20-07e9d6827b81')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('f2141ddd-2908-42f1-ab6d-473d075aa5f5')
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = UUID('2e3b4f47-2764-45d4-b90b-b635b16ba4a5')
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = UUID('9db52e5d-e2b2-4c84-8be2-d5ba6ffd62f2')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('3ce0f4f2-4c34-4abb-a59e-2e766e24e4c1')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('13ed2bef-492c-4ee9-a1a6-f8cd076c2f09')
        self.vs[15]["name"] = """eq1"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = UUID('ed24efa7-512c-4725-91eb-6cbc168da166')
        self.vs[16]["name"] = """eq2"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = UUID('3d1e31a4-d103-41ed-a22d-ad47564532b2')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('d18f75f6-69f8-4117-8d38-cc2b1baa6a06')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('e42b0a0c-3dfc-4208-a831-382aa5a09307')
        self.vs[19]["name"] = """pivot"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = UUID('18dbc4c0-9bdb-4a4b-b098-5ca2ae6117ea')
        self.vs[20]["name"] = """pivot"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = UUID('a464f834-51f6-499e-81f7-4f891cc3fd8d')
        self.vs[21]["type"] = """ruleDef"""
        self.vs[21]["mm__"] = """backward_link"""
        self.vs[21]["GUID__"] = UUID('3f33bdea-ae91-4b0a-bc1f-d3188a05ed80')
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["GUID__"] = UUID('45bb2b10-9abf-40e3-8fb7-3c71b3c41dc9')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('086da598-0133-4ab9-a397-c2c8e5699682')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('210c3eba-9ae5-4682-a0c4-92ba3ca51995')
        self.vs[25]["name"] = """parexitpoint"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('0ffba890-a1b0-4af9-9585-148d64566d37')
        self.vs[26]["name"] = """instfortrans"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('2693e48d-1fc8-4ca5-aa7a-d3ca28d82d33')

