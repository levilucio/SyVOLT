

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
        self["GUID__"] = UUID('eb26fa87-20f3-45d5-92cf-44e0fcf80926')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """outgoingTransitions"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('2a9997cc-5571-4afc-adc1-e39b6dc4bfd7')
        self.vs[1]["associationType"] = """p"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('703e003d-f03c-4d7f-862e-45d6cc21b288')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('df6d904d-ebc8-4030-93d4-b2636fb58949')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('dd40d880-3324-43cf-ba51-67df188ec4d9')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('dadbe186-8697-4a84-97f6-e8e3eb43eb0b')
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('fed314ad-a9e0-4b3d-88d3-17d05de2d154')
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('91b4ecda-771d-4342-970d-e3c37f89da52')
        self.vs[7]["name"] = """par1"""
        self.vs[7]["classtype"] = """Par"""
        self.vs[7]["mm__"] = """Par"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('70827173-9822-484a-8deb-06ba00aef6b0')
        self.vs[8]["name"] = """exitpoint1"""
        self.vs[8]["classtype"] = """ExitPoint"""
        self.vs[8]["mm__"] = """ExitPoint"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('16fb4742-1a50-4fc4-a088-1a58337edc0f')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('ad41efc9-5b12-4411-ad04-f4fdebbad015')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('29cc4eb4-73ec-46c8-b6b1-d985902e2d62')
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = UUID('0b615068-d572-4b74-95d5-fa4440fbbbc0')
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = UUID('76d1f868-7e45-4fcf-b7c1-0c36d6fc2c6c')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('461cf7f5-813b-4ca0-ae0c-93411a0e1f50')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('5bbc5843-543c-455d-8bac-85a1ef3c6db7')
        self.vs[15]["name"] = """eq1"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = UUID('0236806a-890b-4511-8d53-be1c790ae20c')
        self.vs[16]["name"] = """eq2"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = UUID('d38f462f-6c27-41d7-978f-69568b988ac4')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('8f38e80a-c18c-4285-840a-d3505a0cb707')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('0dae4f30-b5d1-4845-8559-18b35136c781')
        self.vs[19]["name"] = """pivot"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = UUID('46560db8-e48a-4419-be72-5023b09514cc')
        self.vs[20]["name"] = """pivot"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = UUID('a5f9eaef-70eb-41b8-953d-6d18318ea44e')
        self.vs[21]["type"] = """ruleDef"""
        self.vs[21]["mm__"] = """backward_link"""
        self.vs[21]["GUID__"] = UUID('37276074-6fab-44d4-b18d-f1a96f973f62')
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["GUID__"] = UUID('9b7ad1e0-c51c-4987-9508-c12fa90d66bf')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('8da88938-d1e7-46b2-a121-f1079bf11009')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('d4b30073-6011-464d-a8a7-eff06194438c')
        self.vs[25]["name"] = """parexitpoint"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('f8235ff9-1387-41a7-a877-6d2e86bc920e')
        self.vs[26]["name"] = """instfortrans"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('d64b0ae2-e28e-4bb4-b05a-a60e9a475db1')

