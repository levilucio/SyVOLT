

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HTransition2QInstSIBLING(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2QInstSIBLING.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstSIBLING, self).__init__(name='HTransition2QInstSIBLING', num_nodes=76, edges=[])
        
        # Add the edges
        self.add_edges([(6, 12), (12, 7), (6, 13), (13, 0), (0, 14), (14, 4), (5, 15), (15, 23), (5, 16), (16, 24), (5, 17), (17, 25), (5, 18), (18, 26), (49, 37), (37, 10), (50, 38), (38, 62), (51, 39), (39, 63), (52, 40), (40, 11), (53, 41), (41, 66), (54, 42), (42, 67), (5, 43), (43, 70), (23, 44), (44, 71), (24, 45), (45, 72), (25, 46), (46, 73), (26, 47), (47, 74), (5, 48), (48, 75), (22, 0), (0, 8), (2, 1), (1, 32), (1, 33), (1, 34), (1, 35), (1, 36), (10, 27), (27, 61), (10, 28), (28, 69), (11, 29), (29, 64), (11, 30), (30, 68), (11, 31), (31, 65), (3, 19), (19, 6), (3, 20), (20, 7), (3, 21), (21, 4), (3, 22), (8, 68), (4, 9), (9, 69), (3, 2), (49, 55), (50, 56), (51, 57), (52, 58), (53, 59), (54, 60), (32, 5), (33, 26), (34, 25), (35, 24), (36, 23), (55, 70), (56, 71), (57, 72), (58, 73), (59, 74), (60, 75)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """Transition2QInstSIBLING"""
        self["GUID__"] = UUID('5d4342cb-8a17-457e-a17b-7ad509b2d16d')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """1"""
        self.vs[0]["GUID__"] = UUID('a2aab970-df16-4c7a-9937-9b0222afd077')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('4d26971a-bd6b-4a57-9ce1-3a37da3c3178')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('0ad4cf53-5830-49b2-8729-ed500db6c0be')
        self.vs[3]["mm__"] = """MatchModel"""
        self.vs[3]["GUID__"] = UUID('61cf2b86-ba23-484a-915f-e1cb3875daf8')
        self.vs[4]["name"] = """stateMachine1"""
        self.vs[4]["classtype"] = """StateMachine"""
        self.vs[4]["mm__"] = """StateMachine"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('0685155c-5bc0-4179-897e-a4b51c8974bc')
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('fb2bce71-9a85-42d9-9ac4-3432eb1d0822')
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('f4877a20-4287-4be3-841f-bc515877103a')
        self.vs[7]["name"] = """sibling0_1"""
        self.vs[7]["classtype"] = """SIBLING0"""
        self.vs[7]["mm__"] = """SIBLING0"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('93be0793-ccb6-4944-b330-d742752a6d12')
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = UUID('4ea54b66-8376-4429-ba53-ac38071b76e3')
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = UUID('aa804d46-6652-4140-a7a5-db8162e036b1')
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('32ef1abb-83dc-4843-b09f-75724ca88e07')
        self.vs[11]["name"] = """concat2"""
        self.vs[11]["mm__"] = """Concat"""
        self.vs[11]["Type"] = """'String'"""
        self.vs[11]["GUID__"] = UUID('9fddf72c-377c-43af-bf31-586e77b9437c')
        self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = UUID('60c298e1-6e2a-4e4d-a430-1e65fe57bbae')
        self.vs[13]["associationType"] = """dest"""
        self.vs[13]["mm__"] = """directLink_S"""
        self.vs[13]["GUID__"] = UUID('ec9873b9-9a22-469c-aea6-aa51d2017a1c')
        self.vs[14]["associationType"] = """owningStateMachine"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('370ff889-eefa-4838-bc82-7f82386d011d')
        self.vs[15]["associationType"] = """channelNames"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = UUID('901ea3f1-7558-4f87-9eca-4a8d43fd4a8d')
        self.vs[16]["associationType"] = """channelNames"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = UUID('c1a7a9ad-fa62-4864-8f96-a7abbafaadc2')
        self.vs[17]["associationType"] = """channelNames"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = UUID('1db29fc8-bd54-452f-ade5-e907ec1e6893')
        self.vs[18]["associationType"] = """channelNames"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = UUID('559c4a6c-dc3f-4686-b280-eb6374e9885f')
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = UUID('4ba5fdbe-2f41-4fb6-8c89-7d8a42387343')
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = UUID('826e3fc5-8bbe-4eea-809c-11267b0c34ee')
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = UUID('c8682e95-7246-4a94-a221-b0f9c4cdfd74')
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = UUID('305391a3-e166-4df5-aead-7a3e670a959a')
        self.vs[23]["name"] = """name1"""
        self.vs[23]["classtype"] = """Name"""
        self.vs[23]["mm__"] = """Name"""
        self.vs[23]["cardinality"] = """1"""
        self.vs[23]["GUID__"] = UUID('d1207f4d-e720-4f3b-a605-f919a2cd47da')
        self.vs[24]["name"] = """name2"""
        self.vs[24]["classtype"] = """Name"""
        self.vs[24]["mm__"] = """Name"""
        self.vs[24]["cardinality"] = """1"""
        self.vs[24]["GUID__"] = UUID('b71a2249-fdb5-4f87-b702-57a88286934a')
        self.vs[25]["name"] = """name3"""
        self.vs[25]["classtype"] = """Name"""
        self.vs[25]["mm__"] = """Name"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = UUID('ad42c2aa-e779-42cc-a359-cc6d81f04952')
        self.vs[26]["name"] = """name4"""
        self.vs[26]["classtype"] = """Name"""
        self.vs[26]["mm__"] = """Name"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = UUID('32bc0eb2-9e96-4352-93db-ad3032400504')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('b835749a-1def-4ae0-890f-3f87df2101ce')
        self.vs[28]["mm__"] = """hasArgs"""
        self.vs[28]["GUID__"] = UUID('e8ba6b8a-1f8f-40e6-b625-7745db34bdad')
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = UUID('33175af8-a333-4d61-836d-39b617028f35')
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = UUID('9c8df9a2-a4b7-460f-8bfe-11a41e4720b0')
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = UUID('00359ae8-84f0-4e95-a506-469bb2df3719')
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = UUID('6eaa6e8e-873f-44a6-9afd-191dc03ddc49')
        self.vs[33]["mm__"] = """apply_contains"""
        self.vs[33]["GUID__"] = UUID('53345f92-b2f9-4166-83aa-be13a6c4baab')
        self.vs[34]["mm__"] = """apply_contains"""
        self.vs[34]["GUID__"] = UUID('c53b48bb-74df-4dab-a1cb-863af80a7fbe')
        self.vs[35]["mm__"] = """apply_contains"""
        self.vs[35]["GUID__"] = UUID('489544e4-ce30-487e-ba36-5722475e3227')
        self.vs[36]["mm__"] = """apply_contains"""
        self.vs[36]["GUID__"] = UUID('54fa55c8-8926-4137-bf41-13fe63af9e6b')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('80e3bb4d-2b51-4f62-aa72-028e460dce01')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('b13c5c7a-a180-4d2e-8103-9fd019a63d86')
        self.vs[39]["mm__"] = """rightExpr"""
        self.vs[39]["GUID__"] = UUID('55a98282-2b31-45c6-bc92-8520a0384b2c')
        self.vs[40]["mm__"] = """rightExpr"""
        self.vs[40]["GUID__"] = UUID('4a30546f-f1a6-4b64-b55d-1894f0c13cf5')
        self.vs[41]["mm__"] = """rightExpr"""
        self.vs[41]["GUID__"] = UUID('e709d2ca-eeec-4de1-b46e-d0954d194548')
        self.vs[42]["mm__"] = """rightExpr"""
        self.vs[42]["GUID__"] = UUID('34d59ae6-330a-4190-8b34-f672799d7c67')
        self.vs[43]["mm__"] = """hasAttribute_T"""
        self.vs[43]["GUID__"] = UUID('07d3018f-dd3f-4578-bef8-c4df45f4d23b')
        self.vs[44]["mm__"] = """hasAttribute_T"""
        self.vs[44]["GUID__"] = UUID('9ab049e1-59c3-4e71-976a-c02a0e7e4273')
        self.vs[45]["mm__"] = """hasAttribute_T"""
        self.vs[45]["GUID__"] = UUID('9e90fdc1-4b4a-4062-b586-d35aa1d79ee4')
        self.vs[46]["mm__"] = """hasAttribute_T"""
        self.vs[46]["GUID__"] = UUID('a24ba8ec-2a69-4d1d-aff5-c7b6556ee13c')
        self.vs[47]["mm__"] = """hasAttribute_T"""
        self.vs[47]["GUID__"] = UUID('0f2baba1-c80c-4f2a-9632-171f28a4951f')
        self.vs[48]["mm__"] = """hasAttribute_T"""
        self.vs[48]["GUID__"] = UUID('af358e5e-4607-4fc3-a140-26b5c7c87c20')
        self.vs[49]["name"] = """eq1"""
        self.vs[49]["mm__"] = """Equation"""
        self.vs[49]["GUID__"] = UUID('fd4fe0eb-758a-4ad5-86ca-0b00eb39a514')
        self.vs[50]["name"] = """eq2"""
        self.vs[50]["mm__"] = """Equation"""
        self.vs[50]["GUID__"] = UUID('c7bcaf7f-6492-4f57-9852-69e945c9a891')
        self.vs[51]["name"] = """eq3"""
        self.vs[51]["mm__"] = """Equation"""
        self.vs[51]["GUID__"] = UUID('8184ee4c-4f2f-4bec-995f-44fa18be89a2')
        self.vs[52]["name"] = """eq4"""
        self.vs[52]["mm__"] = """Equation"""
        self.vs[52]["GUID__"] = UUID('6a12db47-3e0c-4695-83da-56468ffead71')
        self.vs[53]["name"] = """eq5"""
        self.vs[53]["mm__"] = """Equation"""
        self.vs[53]["GUID__"] = UUID('365f2b52-1855-4a30-b153-c21a41e46857')
        self.vs[54]["name"] = """eq6"""
        self.vs[54]["mm__"] = """Equation"""
        self.vs[54]["GUID__"] = UUID('4283f9a9-0c7b-4ef5-87ed-7502137e38fe')
        self.vs[55]["mm__"] = """leftExpr"""
        self.vs[55]["GUID__"] = UUID('6b965c81-1b1f-4f86-a977-5e34c3566cda')
        self.vs[56]["mm__"] = """leftExpr"""
        self.vs[56]["GUID__"] = UUID('33a62f08-b9ea-4814-8dde-472c56e4e5f2')
        self.vs[57]["mm__"] = """leftExpr"""
        self.vs[57]["GUID__"] = UUID('29e90d79-bec3-4f25-b7e2-9c44677461a5')
        self.vs[58]["mm__"] = """leftExpr"""
        self.vs[58]["GUID__"] = UUID('cb73614a-5c19-436c-8df5-3d20b774d5f9')
        self.vs[59]["mm__"] = """leftExpr"""
        self.vs[59]["GUID__"] = UUID('c5671a13-a3ae-43f5-bfac-2345552a310e')
        self.vs[60]["mm__"] = """leftExpr"""
        self.vs[60]["GUID__"] = UUID('e20cba17-68d5-4cea-b41c-13a2ba386ac4')
        self.vs[61]["name"] = """S"""
        self.vs[61]["mm__"] = """Constant"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('4dcc6a30-2337-463a-9af4-00252023a026')
        self.vs[62]["name"] = """exit"""
        self.vs[62]["mm__"] = """Constant"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('7c450b78-851d-4128-9715-651180a37c59')
        self.vs[63]["name"] = """exack"""
        self.vs[63]["mm__"] = """Constant"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('bc000160-7b2f-4fc5-9378-4fea82ceefc6')
        self.vs[64]["name"] = """1"""
        self.vs[64]["mm__"] = """Constant"""
        self.vs[64]["Type"] = """'String'"""
        self.vs[64]["GUID__"] = UUID('6dae9584-967c-4945-854b-c6ef52d56522')
        self.vs[65]["name"] = """2"""
        self.vs[65]["mm__"] = """Constant"""
        self.vs[65]["Type"] = """'String'"""
        self.vs[65]["GUID__"] = UUID('751a5008-0397-453f-ac8b-a88fa9cb5adf')
        self.vs[66]["name"] = """sh"""
        self.vs[66]["mm__"] = """Constant"""
        self.vs[66]["Type"] = """'String'"""
        self.vs[66]["GUID__"] = UUID('29f9f6f1-ae8c-4902-a2f0-7fe7e38ea10e')
        self.vs[67]["name"] = """instfortrans"""
        self.vs[67]["mm__"] = """Constant"""
        self.vs[67]["Type"] = """'String'"""
        self.vs[67]["GUID__"] = UUID('0ee9a272-7e1e-4a03-920c-7884f6f5973f')
        self.vs[68]["name"] = """name"""
        self.vs[68]["mm__"] = """Attribute"""
        self.vs[68]["Type"] = """'String'"""
        self.vs[68]["GUID__"] = UUID('27e219b1-3608-4538-a255-977c0ab33549')
        self.vs[69]["name"] = """name"""
        self.vs[69]["mm__"] = """Attribute"""
        self.vs[69]["Type"] = """'String'"""
        self.vs[69]["GUID__"] = UUID('a4c2f944-817e-4499-955b-de8b4f49889a')
        self.vs[70]["name"] = """name"""
        self.vs[70]["mm__"] = """Attribute"""
        self.vs[70]["Type"] = """'String'"""
        self.vs[70]["GUID__"] = UUID('46c37b42-32b9-4397-9a0a-17a4a475d850')
        self.vs[71]["name"] = """literal"""
        self.vs[71]["mm__"] = """Attribute"""
        self.vs[71]["Type"] = """'String'"""
        self.vs[71]["GUID__"] = UUID('644769c6-cd63-43db-8edf-e7125d37d37e')
        self.vs[72]["name"] = """literal"""
        self.vs[72]["mm__"] = """Attribute"""
        self.vs[72]["Type"] = """'String'"""
        self.vs[72]["GUID__"] = UUID('f0232cda-af35-45cd-aa9a-24c4a998766f')
        self.vs[73]["name"] = """literal"""
        self.vs[73]["mm__"] = """Attribute"""
        self.vs[73]["Type"] = """'String'"""
        self.vs[73]["GUID__"] = UUID('be19cbe4-6265-4e6b-8cd5-3b6b28087db2')
        self.vs[74]["name"] = """literal"""
        self.vs[74]["mm__"] = """Attribute"""
        self.vs[74]["Type"] = """'String'"""
        self.vs[74]["GUID__"] = UUID('2b04a2f2-9539-459e-a1f7-c4948049caf0')
        self.vs[75]["name"] = """pivot"""
        self.vs[75]["mm__"] = """Attribute"""
        self.vs[75]["Type"] = """'String'"""
        self.vs[75]["GUID__"] = UUID('b3c6d048-cab2-4435-831e-81c6adfd4414')
