

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
        self["GUID__"] = UUID('0553715f-1a5b-4c04-afd9-eb76b6e17658')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('337dd579-cd89-421b-b495-4738947cc01d')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('e7f93226-3d58-4969-89cd-154a1df4db07')
        self.vs[2]["name"] = """conditionbranch1"""
        self.vs[2]["classtype"] = """ConditionBranch"""
        self.vs[2]["mm__"] = """ConditionBranch"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('92938745-d7b5-43f1-88fa-7643408a50ff')
        self.vs[3]["name"] = """in1_1"""
        self.vs[3]["classtype"] = """IN1"""
        self.vs[3]["mm__"] = """IN1"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('1fb22137-e19c-4ce1-9af6-9061b985c407')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('21b4ea3a-f3b2-41d1-a05e-c83c625997dc')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('f57c909a-3ff2-4d0b-b3a4-64fa997588f7')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('b14017a6-6a1b-4d88-9656-208b5a0b403c')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('4fb3c685-c37a-4f46-ac3b-751fd392d0e7')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('14cf12e8-3487-4e4e-864b-3b2c8cd1f7a5')
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = UUID('85673274-e943-47a0-95be-1dffec0fcf50')
        self.vs[10]["name"] = """expr1"""
        self.vs[10]["classtype"] = """Expr"""
        self.vs[10]["mm__"] = """Expr"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('2509da62-ab73-4314-88c0-51db45c5fae6')
        self.vs[11]["name"] = """conditionset1"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('10a11b41-6a4e-40b4-a2e7-f04cf720d328')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('eba5972c-d88d-4cd4-b12d-898c90afc3b2')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('6ce45289-2e93-4505-9cec-1f5680da34f6')
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('00d9d791-f971-4f1f-ade2-45df424edfca')
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["GUID__"] = UUID('64d6b961-9265-483c-b55d-70507d859ded')
        self.vs[16]["associationType"] = """transitions"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('4dcb4e63-bdb1-4ce5-b413-299e7ff75d99')
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('367a8648-36df-4995-a55c-0921e470bb2b')
        self.vs[18]["associationType"] = """src"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = UUID('58e0cdca-98e4-4300-ab7c-7fb502fead9e')
        self.vs[19]["associationType"] = """branches"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('0de15b12-ee8f-4aa4-a2aa-a054f123e357')
        self.vs[20]["associationType"] = """if"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('309c81be-7e7b-4dfc-a0f1-c8f792003517')
        self.vs[21]["associationType"] = """then"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('9eb03c24-8f1d-476d-aa4c-adb6385340e2')
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('2b6daa8c-41d2-42e3-a4eb-3aad8a861299')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('1287eccf-d4e4-46bb-abaa-b5b34e62c242')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('4c57507e-1a14-4efb-a46d-c655453e35b8')
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = UUID('e4c2d482-8668-4d7c-bf33-abc390357cc5')
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = UUID('8338c642-a39d-4b00-aaa8-dfc6d44d4dca')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('53376475-8ae0-4cde-8e77-5e84be98534d')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('63d941f3-2baf-40a8-b4b7-26105ff00b0e')
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = UUID('33ddafed-f238-4ebe-b8a7-18df72236530')
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = UUID('dd9f00d3-b200-4854-b598-0da922a035da')
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = UUID('0762961c-83f6-406f-ae7d-0a15895603b3')
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = UUID('a9c805ad-85cb-4ab2-a7df-7f9e4e64ff95')
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = UUID('3e929fa2-be8b-4f68-9cec-7cc514b25d62')
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = UUID('6fe9b1ac-fceb-4359-83f0-4b5e9973901d')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('6a172ab6-3587-4b7e-93ff-0089fb024794')
        self.vs[36]["name"] = """eq1"""
        self.vs[36]["mm__"] = """Equation"""
        self.vs[36]["GUID__"] = UUID('809c6a82-b1fa-4873-bb50-84b43be271ad')
        self.vs[37]["name"] = """eq2"""
        self.vs[37]["mm__"] = """Equation"""
        self.vs[37]["GUID__"] = UUID('032f05d4-5353-4990-a4c1-2a99d766d31f')
        self.vs[38]["name"] = """eq3"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = UUID('ea6fc406-21d8-40a8-aee8-0228174e017b')
        self.vs[39]["name"] = """eq4"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('eca6e664-b857-4b9d-b58e-81f10f062059')
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = UUID('a2be7800-36bb-44a1-b44b-c6711710b293')
        self.vs[41]["mm__"] = """apply_contains"""
        self.vs[41]["GUID__"] = UUID('909b6572-f252-41b7-94b4-35a32fe00d7d')
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = UUID('914e9b6b-0bfc-4139-a7e7-71e94802dac3')
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = UUID('650d866f-077d-4731-a8ed-c47c39a158d9')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('22efba07-2046-406f-90a7-44bc85ef1e37')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('7615a341-2e27-48a9-8224-70db66010ec1')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('9a0e94a3-3324-449a-9f1e-71d0587e2f4c')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('d32401e4-e425-4328-850a-b55cbab17ff4')
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('3d0f9d40-f2ca-4dee-98d5-2122d88b24c4')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('bedf2c15-3f1e-460c-9594-170866112716')
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('1a7a69c4-c09b-494a-a39c-c0e555f976d1')
        self.vs[51]["name"] = """pivot"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('3c27f9d1-dfa5-4c85-8bbd-68f8e06b4887')
        self.vs[52]["name"] = """pivot"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('ecca4811-a6b8-40fe-a71e-afac9996d04a')
        self.vs[53]["name"] = """true"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'Bool'"""
        self.vs[53]["GUID__"] = UUID('2cfa8c6c-ec3c-463e-b5c9-bb2b2ace426a')
        self.vs[54]["name"] = """enp=1"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('a30c9a18-dece-471e-a7b2-25ccd82d8f25')
        self.vs[55]["name"] = """2"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('82067c6c-42b8-4114-9d8e-b8125f4f874a')
        self.vs[56]["name"] = """instForInTrans"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('fb41c6ff-6eb9-45ba-845c-7aa210491412')
        self.vs[57]["name"] = """condsetcompstate"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = UUID('8d16021f-db17-4193-9cad-fed2a73daf2b')

