

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HState2HProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HState2HProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2HProcDef, self).__init__(name='HState2HProcDef', num_nodes=120, edges=[])
        
        # Add the edges
        self.add_edges([(1, 92), (92, 8), (8, 93), (93, 18), (8, 94), (94, 19), (8, 95), (95, 20), (8, 96), (96, 11), (11, 97), (97, 15), (15, 98), (98, 7), (11, 99), (99, 16), (16, 100), (100, 9), (9, 101), (101, 13), (9, 102), (102, 12), (12, 103), (103, 17), (17, 104), (104, 14), (44, 32), (32, 80), (45, 33), (33, 81), (46, 34), (34, 82), (47, 35), (35, 83), (48, 36), (36, 84), (49, 37), (37, 85), (50, 38), (38, 86), (51, 39), (39, 87), (52, 40), (40, 88), (53, 41), (41, 89), (54, 42), (42, 90), (55, 43), (43, 91), (8, 21), (21, 57), (18, 22), (22, 58), (19, 23), (23, 59), (20, 24), (24, 60), (15, 25), (25, 61), (16, 26), (26, 62), (13, 27), (27, 63), (17, 28), (28, 64), (14, 29), (29, 65), (1, 30), (30, 66), (11, 31), (31, 67), (5, 0), (0, 105), (0, 106), (0, 107), (0, 108), (0, 109), (0, 110), (0, 111), (0, 112), (0, 113), (0, 114), (0, 115), (0, 116), (0, 117), (0, 118), (0, 119), (105, 1), (110, 1), (1, 10), (6, 2), (2, 4), (4, 3), (3, 56), (10, 4), (6, 5), (113, 11), (117, 12), (116, 13), (119, 14), (44, 68), (45, 69), (46, 70), (47, 71), (48, 72), (49, 73), (50, 74), (51, 75), (52, 76), (53, 77), (54, 78), (55, 79), (111, 7), (106, 8), (107, 18), (108, 19), (109, 20), (112, 15), (114, 16), (115, 9), (118, 17), (68, 56), (69, 57), (70, 58), (71, 59), (72, 60), (73, 61), (74, 62), (75, 63), (76, 64), (77, 65), (78, 66), (79, 67)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """State2HProcDef"""
        self["GUID__"] = UUID('edab377d-154d-4e5e-88e0-fb3895de81ef')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('7e89e81f-05bc-49e5-8508-6d26bc111c60')
        self.vs[1]["name"] = """localdef1"""
        self.vs[1]["classtype"] = """LocalDef"""
        self.vs[1]["mm__"] = """LocalDef"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('116a2063-3196-4f32-970a-02054f755d04')
        self.vs[2]["mm__"] = """match_contains"""
        self.vs[2]["GUID__"] = UUID('f35e2517-c0ae-4913-bebf-0c8cd8cf8d38')
        self.vs[3]["mm__"] = """hasAttribute_S"""
        self.vs[3]["GUID__"] = UUID('043bcd01-5c4e-43c2-916b-a1404d44f3fd')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('0bbcbdcf-e093-46ea-87c3-82c0ee6e1396')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('b42034a5-23b2-49e2-8775-4021da8c6c35')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('9596d86c-0be9-46b9-a838-b9f5fdadf932')
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('974d7d9d-1592-447b-b2af-962ffcba1f8e')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('6295bdd4-05eb-48bd-aa36-0ac319bf04ee')
        self.vs[9]["name"] = """seq1"""
        self.vs[9]["classtype"] = """Seq"""
        self.vs[9]["mm__"] = """Seq"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('3fb43550-ed23-4df9-a4ac-c4ef6480c1e6')
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = UUID('8f8acbbc-0927-4fde-ab61-460a0cb70690')
        self.vs[11]["name"] = """listen1"""
        self.vs[11]["classtype"] = """Listen"""
        self.vs[11]["mm__"] = """Listen"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('642ff074-5745-4043-bd11-03eeeb1d55a5')
        self.vs[12]["name"] = """listen2"""
        self.vs[12]["classtype"] = """Listen"""
        self.vs[12]["mm__"] = """Listen"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = UUID('88e88afe-52c7-407e-8385-652717983033')
        self.vs[13]["name"] = """triggerT1"""
        self.vs[13]["classtype"] = """Trigger_T"""
        self.vs[13]["mm__"] = """Trigger_T"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = UUID('b87e99fd-d93b-4c83-b5b5-cd82e3ce3161')
        self.vs[14]["name"] = """triggerT2"""
        self.vs[14]["classtype"] = """Trigger_T"""
        self.vs[14]["mm__"] = """Trigger_T"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = UUID('53f78f9a-8a3c-4f7e-b899-c27d109e4667')
        self.vs[15]["name"] = """listenbranch1"""
        self.vs[15]["classtype"] = """ListenBranch"""
        self.vs[15]["mm__"] = """ListenBranch"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('59fecf9a-9002-48d9-98ad-896649c49e70')
        self.vs[16]["name"] = """listenbranch2"""
        self.vs[16]["classtype"] = """ListenBranch"""
        self.vs[16]["mm__"] = """ListenBranch"""
        self.vs[16]["cardinality"] = """1"""
        self.vs[16]["GUID__"] = UUID('54d69d6d-8bab-48b4-8bfd-5fa7c3bc06c2')
        self.vs[17]["name"] = """listenbranch3"""
        self.vs[17]["classtype"] = """ListenBranch"""
        self.vs[17]["mm__"] = """ListenBranch"""
        self.vs[17]["cardinality"] = """1"""
        self.vs[17]["GUID__"] = UUID('66ef7473-361e-4f1b-8d6c-0d8dafea2d36')
        self.vs[18]["name"] = """name1"""
        self.vs[18]["classtype"] = """Name"""
        self.vs[18]["mm__"] = """Name"""
        self.vs[18]["cardinality"] = """1"""
        self.vs[18]["GUID__"] = UUID('7febbd98-65b8-4643-b0b1-8b244d9a4015')
        self.vs[19]["name"] = """name2"""
        self.vs[19]["classtype"] = """Name"""
        self.vs[19]["mm__"] = """Name"""
        self.vs[19]["cardinality"] = """1"""
        self.vs[19]["GUID__"] = UUID('22de018e-3ec8-4833-a852-c44d79490e57')
        self.vs[20]["name"] = """name3"""
        self.vs[20]["classtype"] = """Name"""
        self.vs[20]["mm__"] = """Name"""
        self.vs[20]["cardinality"] = """1"""
        self.vs[20]["GUID__"] = UUID('8a4df7c7-ebb8-4a6f-8b61-7faa137f02d1')
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = UUID('6d78a87f-72f3-4001-b512-7b32b199161e')
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = UUID('142a1f4f-cf68-47ee-a932-ff057df30a75')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('e3cfc7de-4f77-43fd-b05c-1d050986b624')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('060f22e9-502d-495d-bca4-1acb4e471628')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('2af8f2cc-ef07-42ca-bdf8-8491300f4c6a')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('645ecda2-a639-4c31-8d2d-c0fc4baa195d')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('15508599-37c0-4da7-aaca-8834fee9e789')
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = UUID('cdd062ce-e00a-466c-af40-f83a44042077')
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = UUID('52a9f9da-2000-4459-99a3-ab47818708ed')
        self.vs[30]["mm__"] = """hasAttribute_T"""
        self.vs[30]["GUID__"] = UUID('71f900de-acf8-461c-8bfc-39a3954f8e25')
        self.vs[31]["mm__"] = """hasAttribute_T"""
        self.vs[31]["GUID__"] = UUID('87998916-3c4c-4c84-a570-bd19621776b5')
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = UUID('081f05fe-0c95-48b9-af4f-9307acd54a68')
        self.vs[33]["mm__"] = """rightExpr"""
        self.vs[33]["GUID__"] = UUID('0a6fc2f3-a240-452b-b750-cff5ee990c70')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('860a466e-81af-407f-b3c2-09b0238ed77c')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('2f4bc9bb-9695-4b3f-b384-46ef2a0dc2b9')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('7dc5bda3-eb78-44b5-8cf5-1d60191b214e')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('39d42fc6-6865-4573-8a68-84854db5fd1f')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('cb679877-86a2-463f-8878-4d91e4cb4d03')
        self.vs[39]["mm__"] = """rightExpr"""
        self.vs[39]["GUID__"] = UUID('9632f93b-3094-40a3-bfa4-d709dd75199d')
        self.vs[40]["mm__"] = """rightExpr"""
        self.vs[40]["GUID__"] = UUID('3e1adbb2-4f5b-4946-9cc1-6ac8c3627968')
        self.vs[41]["mm__"] = """rightExpr"""
        self.vs[41]["GUID__"] = UUID('46e1bd07-7858-4075-bfef-e67cfef819e2')
        self.vs[42]["mm__"] = """rightExpr"""
        self.vs[42]["GUID__"] = UUID('956957b2-9b8a-4b40-b1c6-6ebb9dc15e51')
        self.vs[43]["mm__"] = """rightExpr"""
        self.vs[43]["GUID__"] = UUID('a4629feb-2bb9-4f8d-9bc6-019f8aa0f628')
        self.vs[44]["name"] = """eq1"""
        self.vs[44]["mm__"] = """Equation"""
        self.vs[44]["GUID__"] = UUID('3007b503-fc60-45ac-bc8f-e776d8240404')
        self.vs[45]["name"] = """eq2"""
        self.vs[45]["mm__"] = """Equation"""
        self.vs[45]["GUID__"] = UUID('6bff5ab3-4db4-454c-8541-d94c7a583869')
        self.vs[46]["name"] = """eq3"""
        self.vs[46]["mm__"] = """Equation"""
        self.vs[46]["GUID__"] = UUID('999a3d65-a990-41df-ba87-c1df5c54bcdc')
        self.vs[47]["name"] = """eq4"""
        self.vs[47]["mm__"] = """Equation"""
        self.vs[47]["GUID__"] = UUID('d7c24159-e216-4310-8db6-c8a06ca2abfa')
        self.vs[48]["name"] = """eq5"""
        self.vs[48]["mm__"] = """Equation"""
        self.vs[48]["GUID__"] = UUID('cea17ac5-f9ac-4d12-b4f2-e0e5fd5d4281')
        self.vs[49]["name"] = """eq6"""
        self.vs[49]["mm__"] = """Equation"""
        self.vs[49]["GUID__"] = UUID('9473dd48-dc5c-4726-bd9d-2f20b2604cc2')
        self.vs[50]["name"] = """eq7"""
        self.vs[50]["mm__"] = """Equation"""
        self.vs[50]["GUID__"] = UUID('0df7da2d-1b67-4246-8601-c69f896a20be')
        self.vs[51]["name"] = """eq8"""
        self.vs[51]["mm__"] = """Equation"""
        self.vs[51]["GUID__"] = UUID('17dfb4ea-39dd-4121-bc23-e384d865b511')
        self.vs[52]["name"] = """eq9"""
        self.vs[52]["mm__"] = """Equation"""
        self.vs[52]["GUID__"] = UUID('a0c08349-4e5a-4f83-9fba-bb26ee6a4b84')
        self.vs[53]["name"] = """eq10"""
        self.vs[53]["mm__"] = """Equation"""
        self.vs[53]["GUID__"] = UUID('ec860161-9980-4f89-9015-25d1d975d492')
        self.vs[54]["name"] = """eq11"""
        self.vs[54]["mm__"] = """Equation"""
        self.vs[54]["GUID__"] = UUID('6c121af6-6c89-41f7-874b-725dfe4b9172')
        self.vs[55]["name"] = """eq12"""
        self.vs[55]["mm__"] = """Equation"""
        self.vs[55]["GUID__"] = UUID('aa7652bb-fb31-4ece-a797-8395ef0f52db')
        self.vs[56]["name"] = """isComposite"""
        self.vs[56]["mm__"] = """Attribute"""
        self.vs[56]["Type"] = """'Bool'"""
        self.vs[56]["GUID__"] = UUID('b12b7a33-d3b7-4512-b96d-e2871a44e690')
        self.vs[57]["name"] = """name"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = UUID('3c9177f0-a11b-4387-bb19-50260bf9061a')
        self.vs[58]["name"] = """literal"""
        self.vs[58]["mm__"] = """Attribute"""
        self.vs[58]["Type"] = """'String'"""
        self.vs[58]["GUID__"] = UUID('240bc21a-3a4d-49fe-ba68-b553d62b2262')
        self.vs[59]["name"] = """literal"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        self.vs[59]["GUID__"] = UUID('e4128b45-c1af-4118-a9df-97b5fbb42950')
        self.vs[60]["name"] = """literal"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        self.vs[60]["GUID__"] = UUID('0f2fb68d-1f30-4c39-84eb-67850c988aa7')
        self.vs[61]["name"] = """channel"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('9677547e-856f-499c-9cc5-dd2f0060be52')
        self.vs[62]["name"] = """channel"""
        self.vs[62]["mm__"] = """Attribute"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('646b35a6-2ebd-4b54-a761-b6eed4e5d9d5')
        self.vs[63]["name"] = """channel"""
        self.vs[63]["mm__"] = """Attribute"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('444e6fbc-d40f-4df6-a870-ac5c6c0f1352')
        self.vs[64]["name"] = """channel"""
        self.vs[64]["mm__"] = """Attribute"""
        self.vs[64]["Type"] = """'String'"""
        self.vs[64]["GUID__"] = UUID('97c410f6-057e-4d53-8927-519c7b670e25')
        self.vs[65]["name"] = """channel"""
        self.vs[65]["mm__"] = """Attribute"""
        self.vs[65]["Type"] = """'String'"""
        self.vs[65]["GUID__"] = UUID('4e8471bd-b481-43ad-986a-821fee1a90d2')
        self.vs[66]["name"] = """pivot"""
        self.vs[66]["mm__"] = """Attribute"""
        self.vs[66]["Type"] = """'String'"""
        self.vs[66]["GUID__"] = UUID('d5822b9f-12d8-4064-906d-c85c9b1ac9c9')
        self.vs[67]["name"] = """pivot"""
        self.vs[67]["mm__"] = """Attribute"""
        self.vs[67]["Type"] = """'String'"""
        self.vs[67]["GUID__"] = UUID('48cbcf9e-9d69-4815-b15f-faf1ba6fa8a6')
        self.vs[68]["mm__"] = """leftExpr"""
        self.vs[68]["GUID__"] = UUID('afa27fd8-e6a0-47d1-9f7b-5b25402d561c')
        self.vs[69]["mm__"] = """leftExpr"""
        self.vs[69]["GUID__"] = UUID('bde17477-41c4-4722-a382-e2e7b53eea38')
        self.vs[70]["mm__"] = """leftExpr"""
        self.vs[70]["GUID__"] = UUID('d3e133c9-1d36-4fab-b9e5-a34e15f87c26')
        self.vs[71]["mm__"] = """leftExpr"""
        self.vs[71]["GUID__"] = UUID('8c5504ad-88c4-4e52-9fbd-e2359f06cbdd')
        self.vs[72]["mm__"] = """leftExpr"""
        self.vs[72]["GUID__"] = UUID('0678d793-c645-495a-9402-b651603a066e')
        self.vs[73]["mm__"] = """leftExpr"""
        self.vs[73]["GUID__"] = UUID('336bcaf9-04fe-42ea-8ff8-98fbd567f56e')
        self.vs[74]["mm__"] = """leftExpr"""
        self.vs[74]["GUID__"] = UUID('dd6f9af3-ea2d-465e-b94b-39520591cd30')
        self.vs[75]["mm__"] = """leftExpr"""
        self.vs[75]["GUID__"] = UUID('ae5dbbc8-8234-4e60-83da-64a4ec812d27')
        self.vs[76]["mm__"] = """leftExpr"""
        self.vs[76]["GUID__"] = UUID('7560e5fd-ae14-4cfb-9465-490866fce8b6')
        self.vs[77]["mm__"] = """leftExpr"""
        self.vs[77]["GUID__"] = UUID('afe6b539-8aac-4fcc-9742-b1095250f5af')
        self.vs[78]["mm__"] = """leftExpr"""
        self.vs[78]["GUID__"] = UUID('cf0a7ad6-f044-4889-a348-a7bd7e3794b6')
        self.vs[79]["mm__"] = """leftExpr"""
        self.vs[79]["GUID__"] = UUID('b8a107fc-1c91-4a46-a548-cef599e8de28')
        self.vs[80]["name"] = """true"""
        self.vs[80]["mm__"] = """Constant"""
        self.vs[80]["Type"] = """'Bool'"""
        self.vs[80]["GUID__"] = UUID('18875bb1-cd25-4911-b516-b398fb0872c6')
        self.vs[81]["name"] = """H"""
        self.vs[81]["mm__"] = """Constant"""
        self.vs[81]["Type"] = """'String'"""
        self.vs[81]["GUID__"] = UUID('a591598d-2dd9-468a-830a-460017e20621')
        self.vs[82]["name"] = """exit_in"""
        self.vs[82]["mm__"] = """Constant"""
        self.vs[82]["Type"] = """'String'"""
        self.vs[82]["GUID__"] = UUID('f6edd02c-c1d8-4d8b-a473-d0e9c716b661')
        self.vs[83]["name"] = """exack_in"""
        self.vs[83]["mm__"] = """Constant"""
        self.vs[83]["Type"] = """'String'"""
        self.vs[83]["GUID__"] = UUID('29d46245-1894-4516-8fcf-3f51428a3912')
        self.vs[84]["name"] = """sh_in"""
        self.vs[84]["mm__"] = """Constant"""
        self.vs[84]["Type"] = """'String'"""
        self.vs[84]["GUID__"] = UUID('a37fc773-dcf4-4e21-affd-ae181da25ced')
        self.vs[85]["name"] = """sh_in"""
        self.vs[85]["mm__"] = """Constant"""
        self.vs[85]["Type"] = """'String'"""
        self.vs[85]["GUID__"] = UUID('95204256-fa5a-4350-b43d-2b9d5df8b6ab')
        self.vs[86]["name"] = """exit"""
        self.vs[86]["mm__"] = """Constant"""
        self.vs[86]["Type"] = """'String'"""
        self.vs[86]["GUID__"] = UUID('36fa6d9a-b5d0-46b5-b935-597e1d6e0664')
        self.vs[87]["name"] = """exit_in"""
        self.vs[87]["mm__"] = """Constant"""
        self.vs[87]["Type"] = """'String'"""
        self.vs[87]["GUID__"] = UUID('817b94d7-f538-4dc6-9ae0-fca6748b463f')
        self.vs[88]["name"] = """exack_in"""
        self.vs[88]["mm__"] = """Constant"""
        self.vs[88]["Type"] = """'String'"""
        self.vs[88]["GUID__"] = UUID('eb8bec8a-2cb7-41fb-9f8b-c2aa77d11b9a')
        self.vs[89]["name"] = """exack"""
        self.vs[89]["mm__"] = """Constant"""
        self.vs[89]["Type"] = """'String'"""
        self.vs[89]["GUID__"] = UUID('24ec177e-72c4-4992-9f52-68c7b8314270')
        self.vs[90]["name"] = """localdefcompstate"""
        self.vs[90]["mm__"] = """Constant"""
        self.vs[90]["Type"] = """'String'"""
        self.vs[90]["GUID__"] = UUID('9c7b5a83-0e05-46a0-ba5f-0ca2ae8df3cd')
        self.vs[91]["name"] = """listenhproc"""
        self.vs[91]["mm__"] = """Constant"""
        self.vs[91]["Type"] = """'String'"""
        self.vs[91]["GUID__"] = UUID('a80ef3b4-eb3d-4aae-a4cc-173071064823')
        self.vs[92]["associationType"] = """def"""
        self.vs[92]["mm__"] = """directLink_T"""
        self.vs[92]["GUID__"] = UUID('6e9c78a8-350b-4f24-a920-cf32904cd66d')
        self.vs[93]["associationType"] = """channelNames"""
        self.vs[93]["mm__"] = """directLink_T"""
        self.vs[93]["GUID__"] = UUID('62152e7a-58b6-40a7-bcf5-b149720bfec0')
        self.vs[94]["associationType"] = """channelNames"""
        self.vs[94]["mm__"] = """directLink_T"""
        self.vs[94]["GUID__"] = UUID('2074ab86-fc27-4c21-a07a-f7cbe0e1a898')
        self.vs[95]["associationType"] = """channelNames"""
        self.vs[95]["mm__"] = """directLink_T"""
        self.vs[95]["GUID__"] = UUID('b705eca3-afe1-4737-b850-7a706d8a1687')
        self.vs[96]["associationType"] = """p"""
        self.vs[96]["mm__"] = """directLink_T"""
        self.vs[96]["GUID__"] = UUID('144646e1-bd7d-4798-8ab9-ce9dc55c3ab1')
        self.vs[97]["associationType"] = """branches"""
        self.vs[97]["mm__"] = """directLink_T"""
        self.vs[97]["GUID__"] = UUID('29903cfb-a4e4-492e-84e7-b3a2428ba655')
        self.vs[98]["associationType"] = """p"""
        self.vs[98]["mm__"] = """directLink_T"""
        self.vs[98]["GUID__"] = UUID('68015c54-bdbd-43b5-93c6-4c580871a725')
        self.vs[99]["associationType"] = """branches"""
        self.vs[99]["mm__"] = """directLink_T"""
        self.vs[99]["GUID__"] = UUID('3fcb4d24-616b-4a9a-81e8-08d244a19a3f')
        self.vs[100]["associationType"] = """p"""
        self.vs[100]["mm__"] = """directLink_T"""
        self.vs[100]["GUID__"] = UUID('3433f954-aeee-44b0-8b94-74763149752d')
        self.vs[101]["associationType"] = """p"""
        self.vs[101]["mm__"] = """directLink_T"""
        self.vs[101]["GUID__"] = UUID('4d5cad55-fa69-4b1e-8f4c-87d6d6c7f678')
        self.vs[102]["associationType"] = """p"""
        self.vs[102]["mm__"] = """directLink_T"""
        self.vs[102]["GUID__"] = UUID('e41514f4-29b8-47d6-9413-6d25d23d14d2')
        self.vs[103]["associationType"] = """branches"""
        self.vs[103]["mm__"] = """directLink_T"""
        self.vs[103]["GUID__"] = UUID('ee1edcde-999f-495d-ba48-6d6118072259')
        self.vs[104]["associationType"] = """p"""
        self.vs[104]["mm__"] = """directLink_T"""
        self.vs[104]["GUID__"] = UUID('6fddaff4-5617-4513-a475-9981c1bfc809')
        self.vs[105]["mm__"] = """apply_contains"""
        self.vs[105]["GUID__"] = UUID('b6632bb7-22ea-4e02-b13d-3590648fe451')
        self.vs[106]["mm__"] = """apply_contains"""
        self.vs[106]["GUID__"] = UUID('0d9513e6-3ddd-4c3f-bfb0-27d700872008')
        self.vs[107]["mm__"] = """apply_contains"""
        self.vs[107]["GUID__"] = UUID('28d2fa19-f94b-4f0b-b8f8-9b943c2c2823')
        self.vs[108]["mm__"] = """apply_contains"""
        self.vs[108]["GUID__"] = UUID('b0ed04ab-99d8-4a6b-a824-132db2a6d0c2')
        self.vs[109]["mm__"] = """apply_contains"""
        self.vs[109]["GUID__"] = UUID('8a701a8e-528e-4896-a718-04be6f464228')
        self.vs[110]["mm__"] = """apply_contains"""
        self.vs[110]["GUID__"] = UUID('1f533177-1065-4bb5-baed-3260d1690870')
        self.vs[111]["mm__"] = """apply_contains"""
        self.vs[111]["GUID__"] = UUID('173c8b58-9906-449a-b0a6-c3fbe53c1cdc')
        self.vs[112]["mm__"] = """apply_contains"""
        self.vs[112]["GUID__"] = UUID('0a64aafe-37ea-45a9-acf7-2dcd8991b6e8')
        self.vs[113]["mm__"] = """apply_contains"""
        self.vs[113]["GUID__"] = UUID('cf10d02b-9a26-4775-b41d-aaeed1f9961f')
        self.vs[114]["mm__"] = """apply_contains"""
        self.vs[114]["GUID__"] = UUID('5d7dc218-e4df-4103-9690-ff1cbaf652eb')
        self.vs[115]["mm__"] = """apply_contains"""
        self.vs[115]["GUID__"] = UUID('fedab432-1953-437c-b761-49291b5b9df2')
        self.vs[116]["mm__"] = """apply_contains"""
        self.vs[116]["GUID__"] = UUID('374be68d-8466-4d3b-97bd-52db92d9498f')
        self.vs[117]["mm__"] = """apply_contains"""
        self.vs[117]["GUID__"] = UUID('b17f51aa-09fc-4c84-90db-06dde9023aba')
        self.vs[118]["mm__"] = """apply_contains"""
        self.vs[118]["GUID__"] = UUID('804a8aac-2342-4a45-a8eb-44b740d9ece9')
        self.vs[119]["mm__"] = """apply_contains"""
        self.vs[119]["GUID__"] = UUID('57e88c98-2a99-4c58-89aa-b7bb5f712fd8')

