

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
        self["GUID__"] = UUID('90b30536-61e6-4eb2-9da2-06bc4b7d21a5')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('332722eb-ce13-461f-9f50-f51973a68b7e')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('d0467889-2f64-43f3-bcb7-989a4da3fcd2')
        self.vs[2]["name"] = """conditionbranch1"""
        self.vs[2]["classtype"] = """ConditionBranch"""
        self.vs[2]["mm__"] = """ConditionBranch"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('82b5e417-3bc5-46f5-849e-4f94bf56b611')
        self.vs[3]["name"] = """in1_1"""
        self.vs[3]["classtype"] = """IN1"""
        self.vs[3]["mm__"] = """IN1"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('5b0f7da9-b603-4e5c-a428-269b518238b3')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('2ca9f116-2391-4017-9b51-2463ad5ae6d9')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('4484f4f4-20c8-4025-9735-04ac5f87b2bd')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('abf566bc-470e-43ab-86ad-3c9429d062b2')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('45343365-6598-4db3-a901-711048865d81')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('8d443f71-b344-4e07-8a60-fba3887a6be4')
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = UUID('1d94db0f-3be7-4498-8eb7-406c18a46e8b')
        self.vs[10]["name"] = """expr1"""
        self.vs[10]["classtype"] = """Expr"""
        self.vs[10]["mm__"] = """Expr"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('fc87e57d-af99-49ea-b663-0bf00c9d0b89')
        self.vs[11]["name"] = """conditionset1"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('ef0dfc3d-4161-4655-ab1f-2d5ef626a353')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('a3013666-c72b-4ce5-99d7-76fb52687640')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('3b1456bc-789e-4ae4-a606-c7d2b52853aa')
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('2b910a1c-4555-4129-acb2-1a4485af3b10')
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["GUID__"] = UUID('b21e22af-c184-4428-9cfe-f6812d0d0d57')
        self.vs[16]["associationType"] = """transitions"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('52180eb5-94d3-4bdf-b1e8-12258981a833')
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('c39b6ee5-cf59-403c-8336-b4509ef59800')
        self.vs[18]["associationType"] = """src"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = UUID('cf8034e1-5958-4e29-aa6e-b8c06e18a9f9')
        self.vs[19]["associationType"] = """branches"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('b6226e7e-cbad-4513-906e-3c4ef0e65113')
        self.vs[20]["associationType"] = """if"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('1e7094d7-18e7-48eb-8191-22e926703a19')
        self.vs[21]["associationType"] = """then"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('cd00b466-624b-4185-8f42-e73c1606aa6a')
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('fc9e6e75-1f10-4396-b381-49bf2843d873')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('0f2e991b-728e-4a1d-a3d6-a8454431a447')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('b0798530-88f9-44df-9921-265b66f598d6')
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = UUID('019db758-a496-4527-bbae-43f7abd237ea')
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = UUID('1890004b-b8f2-43cd-9244-58cad480856c')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('38b97d7d-c6ad-4cee-b5d6-cd0ff14c2f30')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('c32e5e41-dbe8-4b9a-ba5f-57181d742055')
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = UUID('0720b860-f697-4f10-97e1-013adfeadfd8')
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = UUID('37ccf6be-05db-42ee-aacc-6f66ceadcb8a')
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = UUID('b83177c1-6b02-4453-9612-5452e664f592')
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = UUID('dc7d31a1-0c58-46ea-9f63-7e7ed6e9456b')
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = UUID('57464d9a-3354-4cd8-aa0c-c666418c24bd')
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = UUID('c5dd3f1f-6f5a-4587-8d4d-01a7aa3b8966')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('de30451d-7fb1-4d6f-83e6-70fb86bab5dc')
        self.vs[36]["name"] = """eq1"""
        self.vs[36]["mm__"] = """Equation"""
        self.vs[36]["GUID__"] = UUID('d3b2e467-f92d-42d1-8936-0a6661de61b6')
        self.vs[37]["name"] = """eq2"""
        self.vs[37]["mm__"] = """Equation"""
        self.vs[37]["GUID__"] = UUID('f33a74ce-b6c5-4954-bf4d-b70f838f686e')
        self.vs[38]["name"] = """eq3"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = UUID('dd9ad26c-7485-44e1-bfda-c138f09026d0')
        self.vs[39]["name"] = """eq4"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('8ec54046-f7dd-4715-a8a5-c029e40c4ac4')
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = UUID('16808581-b5e5-4130-a1a8-532415546d2a')
        self.vs[41]["mm__"] = """apply_contains"""
        self.vs[41]["GUID__"] = UUID('857ec5a4-6cc3-4703-8893-4bc257660158')
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = UUID('26fea89e-1ae4-46b4-97ac-9dcd253fcdec')
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = UUID('7e38a994-3d58-4945-8359-875042d17a31')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('941f21a9-1cdb-4a9c-9fe1-d72f26e4fd20')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('d26caf7f-48df-4d00-ab43-5e7d7588a7c9')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('eacf4878-31a1-442e-9e04-027c2c3e20b2')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('5caa473e-1592-45e7-b0a9-9504692fdb95')
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('bab14aea-29b0-412e-9381-ab6029985678')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('ed55ff18-3198-48e8-a43d-f8b94737575e')
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('af34e9a4-db76-4def-8afb-0bb46dca60b1')
        self.vs[51]["name"] = """pivot"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('f5136bbc-bb56-4248-9000-54b47a766392')
        self.vs[52]["name"] = """pivot"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('a5c01c19-5648-4ba6-b602-ae161692ca91')
        self.vs[53]["name"] = """true"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'Bool'"""
        self.vs[53]["GUID__"] = UUID('ee873069-7212-44d0-bc85-2f66faa40d6b')
        self.vs[54]["name"] = """enp=1"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('73124ca5-c8dd-4950-b853-982dfa66e0df')
        self.vs[55]["name"] = """2"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('070cbb9f-4fcd-4e29-853a-97dbeffca400')
        self.vs[56]["name"] = """instForInTrans"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('2b6989ea-f52a-4953-a1fc-5c066b95afbf')
        self.vs[57]["name"] = """condsetcompstate"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = UUID('127f615d-f529-4168-ad34-f1e524a11b0e')

