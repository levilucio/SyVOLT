

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions, self).__init__(name='HConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions', num_nodes=58, edges=[])
        
        # Add the edges
        self.add_edges([(4, 16), (16, 8), (8, 17), (17, 3), (8, 18), (18, 0), (11, 19), (19, 2), (2, 20), (20, 10), (2, 21), (21, 7), (36, 28), (28, 53), (37, 29), (29, 9), (38, 30), (30, 56), (39, 31), (31, 57), (10, 22), (22, 50), (7, 23), (23, 51), (11, 24), (24, 52), (34, 0), (0, 12), (5, 1), (1, 40), (1, 41), (1, 42), (1, 43), (9, 25), (25, 54), (9, 26), (26, 48), (9, 27), (27, 55), (6, 32), (32, 4), (6, 33), (33, 8), (6, 34), (6, 35), (35, 3), (41, 2), (12, 48), (4, 13), (13, 49), (15, 4), (6, 5), (36, 44), (37, 45), (38, 46), (39, 47), (40, 11), (42, 10), (43, 7), (7, 14), (14, 8), (44, 49), (45, 50), (46, 51), (47, 52), (11, 15)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ConnectOP_State2CProcDef_Transition2Inst_OtherInTransitions"""
        self["GUID__"] = UUID('b2ce1fd3-5c41-4728-b761-55aa1e0d0757')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('18b8ea8a-85fc-4d78-982a-12aa1884ec35')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('5b03802e-b7b9-4f5e-b3de-922b40484393')
        self.vs[2]["name"] = """conditionbranch1"""
        self.vs[2]["classtype"] = """ConditionBranch"""
        self.vs[2]["mm__"] = """ConditionBranch"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('c1a6a0bf-fa24-4d46-8a50-042192f14538')
        self.vs[3]["name"] = """in1_1"""
        self.vs[3]["classtype"] = """IN1"""
        self.vs[3]["mm__"] = """IN1"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('21faf13c-0810-421b-912c-dfc7a7dfd513')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('ff70f313-7ab2-4a33-afd3-1c7695c1c615')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('2c00dffb-ee5a-49a4-8e75-43f7171816c3')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('11ba830e-c19c-4313-8e90-06fbf3e856a9')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('0cf77539-875a-4a6b-aaee-a70abdca18e3')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('b3c14691-4354-4f83-a900-6af37b747437')
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = UUID('43a1efdf-6230-433b-bc39-6ecf23555200')
        self.vs[10]["name"] = """expr1"""
        self.vs[10]["classtype"] = """Expr"""
        self.vs[10]["mm__"] = """Expr"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('c009eaa9-3264-407f-a6db-ca5550ac198f')
        self.vs[11]["name"] = """conditionset1"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('40dafae7-c1c6-4aad-90d3-a6093b77b806')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('463bd845-a0c0-4f25-96e3-01a405d770be')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('a548cd2e-9328-45a1-90e7-97ff4d1ee706')
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('dee40e51-6cf2-41a9-b424-e0f91a068222')
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["GUID__"] = UUID('d92deedd-0aac-4541-b76d-67d8024eb18c')
        self.vs[16]["associationType"] = """transitions"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('f33d60dc-91d0-424d-a055-3ea120debf98')
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('f32bd676-f039-4a8e-9dd1-d7af4cfe538e')
        self.vs[18]["associationType"] = """src"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = UUID('438d3c27-3485-4e78-b49d-2545c63cdd88')
        self.vs[19]["associationType"] = """branches"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('59af035d-8e26-4545-b416-fafcad77f398')
        self.vs[20]["associationType"] = """if"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('5e66d8d8-35fa-4294-a03b-0e6aefe3e62d')
        self.vs[21]["associationType"] = """then"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('9ec3b6cf-0f41-44d6-b8b0-4bd0977732a5')
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('6511acb9-8c6d-42af-aa46-7a4d290d7124')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('ea4587f3-0965-477c-8273-2e582f2cd78f')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('8f948af7-dd31-4cd5-af6c-82ba35c2f449')
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = UUID('c53c1fdc-aca4-4a87-af6e-99ed6caa54dc')
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = UUID('993fe88a-c83d-4b24-b462-2da983bbd14d')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('bea3eb7a-54e2-4b5f-a1cb-d8fecb5f7427')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('387f3285-0afb-4eba-bdec-332371cc6f82')
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = UUID('b4eab3cd-51c4-4693-8d73-f87931acf31c')
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = UUID('82f21440-7dcf-40e7-a97f-4e0ec788c100')
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = UUID('22a6839f-5074-40c5-80d4-625665aa7859')
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = UUID('de9364c5-82f3-4db9-8809-fe93194b2585')
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = UUID('75b7a064-cfa4-4c91-9abd-930893e0d635')
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = UUID('a81cef95-d9f6-406b-8d59-5e1ed076872f')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('1720e8f4-f859-4470-b7b0-ff159b053a38')
        self.vs[36]["name"] = """eq1"""
        self.vs[36]["mm__"] = """Equation"""
        self.vs[36]["GUID__"] = UUID('5436e4cd-1f8e-42e9-84a3-a2bcb3f0f2aa')
        self.vs[37]["name"] = """eq2"""
        self.vs[37]["mm__"] = """Equation"""
        self.vs[37]["GUID__"] = UUID('39fb1f35-8b24-4185-beda-b6b2eb678b6d')
        self.vs[38]["name"] = """eq3"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = UUID('c3363a2e-90bd-4abe-a9b4-4936b453a80b')
        self.vs[39]["name"] = """eq4"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('45a00140-7d6f-4379-ad10-99ac303078a4')
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = UUID('0d23858b-832a-4d5d-ae2d-e1b2f50d30b6')
        self.vs[41]["mm__"] = """apply_contains"""
        self.vs[41]["GUID__"] = UUID('5eababe0-a5b8-49ad-8fa7-8d9b89e580c9')
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = UUID('f3ed85a0-c203-4955-a72a-aef5dacdf4ee')
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = UUID('220abf4e-c29c-413f-997c-4ead53781cdf')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('37562e5e-48fb-468d-b27f-ce00360c91ea')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('43bb27f6-1b9f-4e09-8b20-a0a09055a0cc')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('a6b2b582-0252-4534-8806-17d669393d6c')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('60ecb6d5-0477-4e7a-934f-35f477ee8da0')
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('7d88ccdb-38b1-4c0f-b915-9d1a68143c5d')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('db518655-df8e-43e4-91fc-0826bfcca77d')
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('d95ed638-6461-4aab-a871-359ef6635c15')
        self.vs[51]["name"] = """pivotin"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('74fc896e-4555-4024-8939-5f8f0dae0d4c')
        self.vs[52]["name"] = """pivotin"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('be78a9f1-82f7-4c3a-857e-b78797faf31c')
        self.vs[53]["name"] = """true"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'Bool'"""
        self.vs[53]["GUID__"] = UUID('ecac76f7-a053-48d1-94da-30abc0933e8d')
        self.vs[54]["name"] = """enp="""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('1fed2e17-a098-4feb-9b98-7ccbf8a29fb6')
        self.vs[55]["name"] = """"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('6860ab1f-83d0-4817-a0a4-b6904d683f35')
        self.vs[56]["name"] = """instForInTrans"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('3ebc70af-7ccb-4408-aa6f-6251c3335192')
        self.vs[57]["name"] = """condsetcompstate"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = UUID('33f322c6-00bc-4334-aa99-d043858e2899')

