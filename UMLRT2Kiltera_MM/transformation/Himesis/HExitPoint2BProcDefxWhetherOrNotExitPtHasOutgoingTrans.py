

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans, self).__init__(name='HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans', num_nodes=64, edges=[])
        
        # Add the edges
        self.add_edges([(3, 0), (0, 10), (2, 19), (19, 7), (7, 20), (20, 12), (7, 21), (21, 9), (9, 22), (22, 5), (39, 33), (33, 51), (40, 34), (34, 8), (41, 35), (35, 53), (42, 36), (36, 54), (43, 37), (37, 55), (44, 38), (38, 56), (7, 23), (23, 59), (12, 24), (24, 60), (5, 25), (25, 61), (2, 26), (26, 62), (9, 27), (27, 63), (4, 1), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (8, 13), (13, 52), (8, 14), (14, 58), (28, 2), (2, 11), (6, 15), (15, 3), (6, 16), (16, 10), (3, 17), (17, 57), (10, 18), (18, 58), (11, 3), (6, 4), (32, 5), (39, 45), (40, 46), (41, 47), (42, 48), (43, 49), (44, 50), (29, 7), (30, 12), (31, 9), (45, 57), (46, 59), (47, 60), (48, 61), (49, 62), (50, 63)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = UUID('5ed59b4a-ef3c-4535-888f-b34b2d404293')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """exitPoints"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('b2fcdbf6-d455-49e9-a219-3e6685a450b2')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('b3b091b0-a770-44a7-9138-dd8c00e27f73')
        self.vs[2]["name"] = """localdef1"""
        self.vs[2]["classtype"] = """LocalDef"""
        self.vs[2]["mm__"] = """LocalDef"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('8fcb1277-b57a-4a2e-96dd-e171c34b42d7')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('005cd0f8-04c4-4552-a1b7-b056eb4de85f')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('a8a5d24d-f94a-4252-b863-682c949ae727')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('9eabeb02-759f-419a-9af0-5cded97a8421')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('050fa991-fa6b-4272-984c-eb79be140f4f')
        self.vs[7]["name"] = """procdef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('160d4b07-ff0b-4882-8483-047cbf7358b8')
        self.vs[8]["name"] = """concat1"""
        self.vs[8]["mm__"] = """Concat"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = UUID('76805876-b4d7-472f-a78e-b2bee4043359')
        self.vs[9]["name"] = """par1"""
        self.vs[9]["classtype"] = """Par"""
        self.vs[9]["mm__"] = """Par"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('32f37c11-fc4a-46e4-8b1a-d834e949fd86')
        self.vs[10]["name"] = """exitpoint1"""
        self.vs[10]["classtype"] = """ExitPoint"""
        self.vs[10]["mm__"] = """ExitPoint"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = UUID('15c795c3-834f-4abe-8cc7-45d209685542')
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('db1dcf35-8322-4579-a07a-3c035ad8583b')
        self.vs[12]["name"] = """name1"""
        self.vs[12]["classtype"] = """Name"""
        self.vs[12]["mm__"] = """Name"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = UUID('bc2176cd-96f6-413d-8db0-aee2b5df8c95')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('aba35862-88ea-4ab0-b613-43ac67746911')
        self.vs[14]["mm__"] = """hasArgs"""
        self.vs[14]["GUID__"] = UUID('bb459943-fe6f-4f90-9e15-8d404384d015')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('11cd49e5-ec40-4f5a-9834-167a44b6415a')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('9e12ffed-94a0-42d3-b37d-156143955259')
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = UUID('8ee14f30-c4d6-4f7b-9e7e-563f478e7e69')
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = UUID('4921b2c8-44cd-4612-9ada-f6f12ab591ce')
        self.vs[19]["associationType"] = """def"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('90690db6-2815-46ad-b369-83ea06f22127')
        self.vs[20]["associationType"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('9479cd5e-4f53-49b5-bf62-996f8a450501')
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('65503127-b816-44b5-a5db-3598547d4707')
        self.vs[22]["associationType"] = """p"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = UUID('18a3fd1b-8d7e-4b9a-9948-413db26318fb')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('0528180e-2be7-4f9b-acd1-b8f08fffa9c9')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('fbda5dfa-93fc-43b2-ac03-965f718cb316')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('75e43d85-63e3-4f44-8bec-80dc960ca2d9')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('7d2b285f-edf0-4e54-9537-2cb93de717b4')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('422b2366-50fe-42c1-9759-b8cfb866ae0c')
        self.vs[28]["mm__"] = """apply_contains"""
        self.vs[28]["GUID__"] = UUID('b34ac182-84a0-4496-81e6-4cee277dc3d0')
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = UUID('7b0c594d-c37c-45a8-9f8c-48e0226382e3')
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = UUID('6c4d4e3d-9588-48c4-9b73-cb710b576a80')
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = UUID('67f9e3e6-a067-4193-a234-a6c2c33e5621')
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = UUID('002827f8-2801-4574-b257-4d0dfb0424e4')
        self.vs[33]["mm__"] = """rightExpr"""
        self.vs[33]["GUID__"] = UUID('62f3faa6-a847-41f0-bdd1-fea453801c99')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('1b49490f-bfd9-46b2-9134-b91cfb87209f')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('64b85194-7683-412b-9750-c498a81106be')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('3a76e913-f052-4504-84d2-e4737304f2be')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('58949c51-73c8-4530-b080-aa5ab7f249a0')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('23d47e58-962b-4748-937c-83b623928497')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('19cdc31c-97b4-46cc-9f36-c29c579f0193')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('2d519a05-f023-4a8c-a4e0-f5f96eb0a6fc')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('acf6dabf-99cf-4fd3-a5d8-7d5415a72559')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('177b2715-a21f-4712-8450-ea7ccbd88afd')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('92183b6e-ed55-451d-9b59-e7286a3dbc54')
        self.vs[44]["name"] = """eq6"""
        self.vs[44]["mm__"] = """Equation"""
        self.vs[44]["GUID__"] = UUID('f74143a7-74ea-428e-8fe3-2e0b48bb08bd')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('34b9a194-5f33-43cd-bee2-201c61f0d31a')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('8efda67a-37cb-4d36-92fd-c20af1510bb4')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('5b41d04a-5f07-431d-8a15-c5caf15bbef4')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('912bb955-d353-425c-8348-1fdee561dfec')
        self.vs[49]["mm__"] = """leftExpr"""
        self.vs[49]["GUID__"] = UUID('f36e9882-7066-4e6f-a07c-c6e4ed899084')
        self.vs[50]["mm__"] = """leftExpr"""
        self.vs[50]["GUID__"] = UUID('23828380-a8e3-4b67-a9ae-8cdbc606a4a4')
        self.vs[51]["name"] = """true"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'Bool'"""
        self.vs[51]["GUID__"] = UUID('bf6c95e8-be5f-4f3a-bad5-c4627a25848b')
        self.vs[52]["name"] = """B"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('8ce83a9d-f7eb-4890-a83f-524441e0124f')
        self.vs[53]["name"] = """sh_in"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('c79aa21d-0fc2-40a9-aec3-3e331bc2ed96')
        self.vs[54]["name"] = """sh_in"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('c344f275-e0fb-43c5-9c65-1e41fbae4df2')
        self.vs[55]["name"] = """localdefcompstate"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('b81a4197-3c68-4419-9957-698f693ebe4a')
        self.vs[56]["name"] = """parexitpoint"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('bc9525a2-adff-448c-85ff-6ba96acd9742')
        self.vs[57]["name"] = """isComposite"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'Bool'"""
        self.vs[57]["GUID__"] = UUID('d028e820-77a1-4f87-be2c-7d027370418e')
        self.vs[58]["name"] = """name"""
        self.vs[58]["mm__"] = """Attribute"""
        self.vs[58]["Type"] = """'String'"""
        self.vs[58]["GUID__"] = UUID('8da733bf-641e-4032-8a9e-34834314f3dd')
        self.vs[59]["name"] = """name"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        self.vs[59]["GUID__"] = UUID('4dda01df-fbc2-4d8c-8fbb-5ef2f51af765')
        self.vs[60]["name"] = """literal"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        self.vs[60]["GUID__"] = UUID('af3f5cd1-ba3f-40ad-9d38-bb7f1fdc29e8')
        self.vs[61]["name"] = """channel"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('0c8190ea-d1e7-49e7-9280-e090da441f25')
        self.vs[62]["name"] = """pivot"""
        self.vs[62]["mm__"] = """Attribute"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('7e3ae7a0-8d11-4b27-b902-bef4bca9021f')
        self.vs[63]["name"] = """pivot"""
        self.vs[63]["mm__"] = """Attribute"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('e5f67fb9-0c50-491b-92c5-5015f98476c8')

