

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
        self["GUID__"] = UUID('30b93dcd-1076-4340-bf9c-d1bfc756e499')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('3d14d446-64b0-498a-915c-3c1e81d6e4bf')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('98e23548-bd82-4c91-8362-5418e55f1f8f')
        self.vs[2]["name"] = """conditionbranch1"""
        self.vs[2]["classtype"] = """ConditionBranch"""
        self.vs[2]["mm__"] = """ConditionBranch"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('ecdb0767-c895-4c26-8f26-7b1470e10e86')
        self.vs[3]["name"] = """in1_1"""
        self.vs[3]["classtype"] = """IN1"""
        self.vs[3]["mm__"] = """IN1"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('b333151a-3009-4b44-88e4-254473b60c23')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('6ae8b865-5915-409b-b00b-345cd17631d7')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('76d32cf4-cf76-426a-b3ff-614484e594e8')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('0176957a-9aa0-421d-8268-5cd239961b98')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('69dd3bc0-2a2d-4bfa-9ca2-bbca437674ce')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('1e1618de-0431-4c7d-a693-6a06966985e8')
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = UUID('563df733-b308-4535-88c4-92c2395e7943')
        self.vs[10]["name"] = """expr1"""
        self.vs[10]["classtype"] = """Expr"""
        self.vs[10]["mm__"] = """Expr"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('164700ec-70ff-4064-90d3-efe1575a9316')
        self.vs[11]["name"] = """conditionset1"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('a98c2d61-ba8c-41fe-b998-91bef07facd9')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('36a7653c-88b2-41be-bddf-4489612b109a')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('b6e14082-a379-477c-879b-abe6260ec895')
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('1ca1d801-0e59-470b-8825-8e1cb123da94')
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["GUID__"] = UUID('aa7e9674-fb93-4bd4-bc15-fc0af860fbe9')
        self.vs[16]["associationType"] = """transitions"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('de686458-c2f0-4380-92ba-9427276177af')
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('8dd1168b-97fb-464b-8ea8-4dbac489e43b')
        self.vs[18]["associationType"] = """src"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = UUID('e582f9d4-febb-47d5-9b74-d2e4bab08a8f')
        self.vs[19]["associationType"] = """branches"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('9109aeed-af5c-4f7c-acd4-0ceaab52e35c')
        self.vs[20]["associationType"] = """if"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('5eed87e1-4691-4ee7-b786-199f6ec28139')
        self.vs[21]["associationType"] = """then"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('78b35c40-0d5e-4410-aae0-54ddda15ef65')
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('c8771454-98ac-4f8a-b445-3e63d874c523')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('3747458c-35e8-4f0e-be01-d826c2643b9c')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('b6c5ec90-3612-4121-9a81-e0f517cba0f2')
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = UUID('db93ce11-01ec-4ebe-93da-bdbea021742f')
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = UUID('b695e7a1-0a58-4d53-b8b5-d4575cf3b628')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('321a08e5-e45c-408a-8d90-8791190bd814')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('fac6c4ce-77de-4472-9fd7-89a11e5e3c9a')
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = UUID('76626e6b-8d2e-47ec-a7bc-c38da0b6e893')
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = UUID('687e8db6-1a0f-48e0-9269-c303d677f9e5')
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = UUID('37e89f59-68a0-46ed-b6dc-f936ddcbbb25')
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = UUID('625ca636-c5a1-4955-b7dc-1f7015dd10cf')
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = UUID('e54e253f-53a7-4af6-9169-fc9ca68b1797')
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = UUID('c52049cd-2ca8-4f52-8c98-9ba8232f7bcb')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('aa66ec12-6e04-4a53-a7b6-7cbec77b12c7')
        self.vs[36]["name"] = """eq1"""
        self.vs[36]["mm__"] = """Equation"""
        self.vs[36]["GUID__"] = UUID('a168b9fa-0f68-435e-8542-8f62ed54e7e6')
        self.vs[37]["name"] = """eq2"""
        self.vs[37]["mm__"] = """Equation"""
        self.vs[37]["GUID__"] = UUID('f33f31be-0bbb-4fac-bfb8-00e6335ba533')
        self.vs[38]["name"] = """eq3"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = UUID('284d6849-e19e-450d-afde-eef1adb9b929')
        self.vs[39]["name"] = """eq4"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('36c4358a-e7a5-4988-a76b-7f0d3ad6fe9e')
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = UUID('3527b1e5-a9e8-40df-9a3c-b64cda1613c4')
        self.vs[41]["mm__"] = """apply_contains"""
        self.vs[41]["GUID__"] = UUID('f208e4c5-1614-4e74-9e46-3c3bb7e15e24')
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = UUID('2b5158fa-3f36-48e7-a873-e096db1cde6d')
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = UUID('0ce720af-c764-4dad-94d2-e16f2652ef3e')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('f6ade1d4-6f70-42d5-9e75-f326f5270b45')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('656e7be3-075d-4e0d-afa6-65b1681021d0')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('81bf76b7-5e16-4a64-a658-d6cf50781e50')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('0802000b-ce56-4cf8-ad00-e7166d7a1dcd')
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('e48c7e82-d932-41cb-8442-d9262e07e86c')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('bf499a75-599c-4840-ad77-9beabda45a87')
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('54a0cd77-8b45-4ed3-9af4-4455af7d95a7')
        self.vs[51]["name"] = """pivot"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('1b4335f7-0a1c-4670-8af9-f5c431f802e1')
        self.vs[52]["name"] = """pivot"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('fba4ece5-8efd-413d-bdaa-193e2bf1c8b6')
        self.vs[53]["name"] = """true"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'Bool'"""
        self.vs[53]["GUID__"] = UUID('d6d5447d-88ee-4f4b-aa3f-63041186e9a3')
        self.vs[54]["name"] = """enp=1"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('d83d51bc-07d9-4fa0-a92f-3a69ad31bbbe')
        self.vs[55]["name"] = """2"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('8889fed8-3e14-4709-8825-07478829b461')
        self.vs[56]["name"] = """instForInTrans"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('6849994c-0e44-4a1f-9ff6-73d4a35472e3')
        self.vs[57]["name"] = """condsetcompstate"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = UUID('f7926c7d-04ca-427b-86de-a702f3cb8cd2')

