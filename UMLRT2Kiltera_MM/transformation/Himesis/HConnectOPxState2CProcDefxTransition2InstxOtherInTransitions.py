

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions, self).__init__(name='HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions', num_nodes=58, edges=[])
        
        # Add the edges
        self.add_edges([(4, 16), (16, 8), (8, 17), (17, 3), (8, 18), (18, 0), (11, 19), (19, 2), (2, 20), (20, 10), (2, 21), (21, 7), (36, 28), (28, 53), (37, 29), (29, 9), (38, 30), (30, 56), (39, 31), (31, 57), (10, 22), (22, 50), (7, 23), (23, 51), (11, 24), (24, 52), (34, 0), (0, 12), (5, 1), (1, 40), (1, 41), (1, 42), (1, 43), (9, 25), (25, 54), (9, 26), (26, 48), (9, 27), (27, 55), (6, 32), (32, 4), (6, 33), (33, 8), (6, 34), (6, 35), (35, 3), (41, 2), (12, 48), (4, 13), (13, 49), (15, 4), (6, 5), (36, 44), (37, 45), (38, 46), (39, 47), (40, 11), (42, 10), (43, 7), (7, 14), (14, 8), (44, 49), (45, 50), (46, 51), (47, 52), (11, 15)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions"""
        self["GUID__"] = UUID('188148b4-766e-40d4-a779-a6f27409f409')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('3559e80d-a85a-4645-9c49-dc2cab822aef')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('d171817b-9ece-48b3-a719-633053c22177')
        self.vs[2]["name"] = """conditionbranch1"""
        self.vs[2]["classtype"] = """ConditionBranch"""
        self.vs[2]["mm__"] = """ConditionBranch"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('285ddb43-868d-4db5-a7af-7578cc0a3f00')
        self.vs[3]["name"] = """in1_1"""
        self.vs[3]["classtype"] = """IN1"""
        self.vs[3]["mm__"] = """IN1"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('d51e94c8-e625-4a02-aa61-807e3d305c9e')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('23a887be-b7db-4a99-bb80-9392ffa216e1')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('461fe50f-9a31-4010-889b-4fc7ad88be3c')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('18867822-b125-4c46-88df-041f039281db')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('78e11412-8e31-4603-b14e-6c017290e7fc')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('be2d8fc3-a8cc-4d4a-9839-3c9267731e55')
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = UUID('a9c2cfdb-a25c-48e2-b671-9ba3c0865192')
        self.vs[10]["name"] = """expr1"""
        self.vs[10]["classtype"] = """Expr"""
        self.vs[10]["mm__"] = """Expr"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('4374707d-d134-4a70-91fb-5e02e60c6562')
        self.vs[11]["name"] = """conditionset1"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('59f6fb56-d3bb-4aa4-a841-1e7a6063d712')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('a41d23b9-54ab-4b06-af4c-76a28c21cf27')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('2202879a-4227-453f-b7ef-b1346c889221')
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('925f5d33-b995-4dee-a927-86997f5291d7')
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["GUID__"] = UUID('cfbffb02-1c81-4e62-ab66-d85643e23bef')
        self.vs[16]["associationType"] = """transitions"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('deb363c7-90f9-47c0-af9d-f53e08fac81b')
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('62ede9cf-efbd-4f03-900a-73fb005c4f30')
        self.vs[18]["associationType"] = """src"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = UUID('c0a75c92-9c4b-49c6-84a8-48e87916b578')
        self.vs[19]["associationType"] = """branches"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('e7cdb327-6c79-42f2-8414-2a8c7ee46f91')
        self.vs[20]["associationType"] = """if"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('b3ec1f27-4cc3-41d9-8797-c561b63a0202')
        self.vs[21]["associationType"] = """then"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('f2e93501-3e84-460c-ba04-9045a575a988')
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('b3b8cbb2-4481-47a3-858e-8449ddeab414')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('4a081bf6-1e33-45cd-97bd-7f29a39acdcb')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('3bf20314-66a7-4858-be88-a35d8d43ebb5')
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = UUID('39f6df06-e325-4ac6-93c4-c8a0ea61eefa')
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = UUID('6e917fba-bbbf-4d79-acd2-2379acf81cbd')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('63fecf90-22b6-47df-8d81-d8ba79532e8f')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('262c3a75-56d0-4e8d-b99a-b874ea842bbb')
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = UUID('699168ab-fa52-4ddc-ab5f-fad491bbfc31')
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = UUID('9ff242d4-7d7e-4208-b03b-7fd9a1589864')
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = UUID('7be51de3-a841-48a5-80c0-0bdeb3e0dd8f')
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = UUID('f4fb4e5e-c48f-4dcf-8529-86ed2f6097f2')
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = UUID('3a46bfcf-b9ce-46f3-ab38-f4654babeb3c')
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = UUID('ab8eceba-06a2-41d1-a779-9aca2f45d319')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('c55a8723-1028-4391-baff-bb79c408cc4f')
        self.vs[36]["name"] = """eq1"""
        self.vs[36]["mm__"] = """Equation"""
        self.vs[36]["GUID__"] = UUID('298bf2bb-d4a1-494d-94a8-85a513cb22c8')
        self.vs[37]["name"] = """eq2"""
        self.vs[37]["mm__"] = """Equation"""
        self.vs[37]["GUID__"] = UUID('552bafaa-3767-4ef6-b3f7-afe14f8acd92')
        self.vs[38]["name"] = """eq3"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = UUID('d28c6340-5259-4992-9b03-02e3fcf367e4')
        self.vs[39]["name"] = """eq4"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('d1e9e875-2c5c-4fcc-8991-9ca25dd96e16')
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = UUID('94c61cda-d5ec-41ef-bdea-e04888cebbd0')
        self.vs[41]["mm__"] = """apply_contains"""
        self.vs[41]["GUID__"] = UUID('0d8e693c-b2af-4a6d-82b9-a32f244fd634')
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = UUID('ac72e2aa-ad11-42a5-9fe1-a792211a27f2')
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = UUID('571bc9a8-5ea3-43da-afdc-d1ef7d67138b')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('990cfb2c-9c3f-4c75-925c-e0ddb0e6be78')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('0ff4aa8a-320e-4b46-9408-8589708ed142')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('956228d1-5949-48a8-a1f9-204c2227e971')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('b38579b4-b421-4bc7-ada9-937647fb1a1e')
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('6c807a36-91f1-4724-a469-dbf68e427d0f')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('ac4e4071-4c4f-46ee-8fd6-79e8d5c3bd37')
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('6ba61771-4496-40f0-8588-039cc8a0a31f')
        self.vs[51]["name"] = """pivot"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('01ea6036-b06d-4959-89a8-0931128f367d')
        self.vs[52]["name"] = """pivot"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('98b265f3-609a-4072-8499-90598c696c78')
        self.vs[53]["name"] = """true"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'Bool'"""
        self.vs[53]["GUID__"] = UUID('73a1bc3e-013f-49e7-96be-192958fbc5ab')
        self.vs[54]["name"] = """enp=xox"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('25e78298-c826-44b9-acef-19388d93b73e')
        self.vs[55]["name"] = """xox"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('e6227651-1326-491b-a009-dcc052f71625')
        self.vs[56]["name"] = """instForInTrans"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('270dea8c-b15d-49c1-a368-15a9a7269a62')
        self.vs[57]["name"] = """condsetcompstate"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = UUID('832ba850-ca31-439d-a089-186e7d675042')

