

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2ProcDef, self).__init__(name='HState2ProcDef', num_nodes=57, edges=[])
        
        # Add the edges
        self.add_edges([(5, 9), (9, 15), (5, 10), (10, 16), (5, 11), (11, 17), (27, 22), (22, 6), (28, 23), (23, 38), (29, 24), (24, 39), (30, 25), (25, 40), (31, 26), (26, 41), (5, 42), (42, 49), (15, 43), (43, 50), (16, 44), (44, 51), (17, 45), (45, 52), (5, 46), (46, 53), (5, 47), (47, 56), (3, 0), (0, 18), (0, 19), (0, 20), (0, 21), (6, 7), (7, 37), (6, 8), (8, 48), (4, 1), (1, 2), (2, 12), (12, 48), (2, 13), (13, 54), (2, 14), (14, 55), (4, 3), (27, 32), (28, 33), (29, 34), (30, 35), (31, 36), (18, 5), (19, 15), (20, 16), (21, 17), (32, 49), (33, 50), (34, 51), (35, 52), (36, 53)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """State2ProcDef"""
        self["GUID__"] = UUID('83605342-dc03-4fac-bfbc-aec39dca2d8f')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('f9d1828a-34a2-43ea-ac75-d112607a65a0')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('6d634f84-b41c-41c7-8aa5-a9f9b5f3553d')
        self.vs[2]["name"] = """state1"""
        self.vs[2]["classtype"] = """State"""
        self.vs[2]["mm__"] = """State"""
        self.vs[2]["cardinality"] = """+"""
        self.vs[2]["GUID__"] = UUID('4f9bbe8c-96e8-4e8d-837f-1d0172523241')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('3b733697-1fc1-4923-b938-e350917965ed')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('3e43978f-be7f-4fd4-82aa-f8d3afdcc25a')
        self.vs[5]["name"] = """procdef1"""
        self.vs[5]["classtype"] = """ProcDef"""
        self.vs[5]["mm__"] = """ProcDef"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('7c685ec3-ba62-4b35-9527-c14fdf4ed322')
        self.vs[6]["name"] = """concat1"""
        self.vs[6]["mm__"] = """Concat"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = UUID('754c469f-806a-4653-accb-edaa2b906093')
        self.vs[7]["mm__"] = """hasArgs"""
        self.vs[7]["GUID__"] = UUID('74c647dc-a10d-4c7d-8bfd-e911b1388343')
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = UUID('ef7fea39-679a-4402-a951-7799eba0dd24')
        self.vs[9]["associationType"] = """channelNames"""
        self.vs[9]["mm__"] = """directLink_T"""
        self.vs[9]["GUID__"] = UUID('9d7e0ea7-211b-442c-a5ff-0a0ce009eb54')
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('7801474f-8a35-4f94-8af2-992bc20a8def')
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('bffc30fc-9352-48cb-af3f-8c1c668e663f')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('db7b607e-8a3f-489b-af49-2ad44b54e100')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('b139a2d8-0be9-4ac8-9d7d-064635ecd75e')
        self.vs[14]["mm__"] = """hasAttribute_S"""
        self.vs[14]["GUID__"] = UUID('e35cfec4-4332-4bf9-88ad-7d725cb19c2a')
        self.vs[15]["name"] = """name1"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('5b3a0f69-bec1-4032-840a-1c0c055302a1')
        self.vs[16]["name"] = """name2"""
        self.vs[16]["classtype"] = """Name"""
        self.vs[16]["mm__"] = """Name"""
        self.vs[16]["cardinality"] = """1"""
        self.vs[16]["GUID__"] = UUID('6c76f462-e7f5-4301-9185-5ce93572b10f')
        self.vs[17]["name"] = """name3"""
        self.vs[17]["classtype"] = """Name"""
        self.vs[17]["mm__"] = """Name"""
        self.vs[17]["cardinality"] = """1"""
        self.vs[17]["GUID__"] = UUID('72111b40-ee81-450a-9e54-d201a6b7b665')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('f0a95df7-4899-4503-ae2b-6d5083465763')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('0616f1db-94ab-4149-9936-64c10d6970df')
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = UUID('849d6d41-acd4-4674-a6d8-1b0c8c065b2b')
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = UUID('50bc3753-54d6-4be6-a8d0-96eb2fe92609')
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = UUID('30261a24-3669-4924-91ae-c956c873d87d')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('ef06bcb4-d6fe-404a-b137-1b43edd13e7c')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('96e7677c-5cec-41f4-802b-87a614790359')
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = UUID('1500465b-1b49-4afa-b6d2-e49ff0be1ef0')
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = UUID('37315f89-189f-4e4b-809c-910cf67ca99c')
        self.vs[27]["name"] = """eq1"""
        self.vs[27]["mm__"] = """Equation"""
        self.vs[27]["GUID__"] = UUID('9bc4e826-a85a-402c-89ba-da9a1d9995cb')
        self.vs[28]["name"] = """eq2"""
        self.vs[28]["mm__"] = """Equation"""
        self.vs[28]["GUID__"] = UUID('6f2fa1d8-cafe-4275-9716-2c3a6e50a853')
        self.vs[29]["name"] = """eq3"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = UUID('1cc543c6-57cd-4294-893e-167677fbd63b')
        self.vs[30]["name"] = """eq4"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('1bb14a63-4932-4c68-8a3f-44ae863637e5')
        self.vs[31]["name"] = """eq5"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('1f69b2c4-12cf-460f-8324-cf74494c40b5')
        self.vs[32]["mm__"] = """leftExpr"""
        self.vs[32]["GUID__"] = UUID('8475ab8d-5af5-44a4-810d-6c2f52716e7e')
        self.vs[33]["mm__"] = """leftExpr"""
        self.vs[33]["GUID__"] = UUID('d7852046-9569-4866-ab49-e7ee26d5f68b')
        self.vs[34]["mm__"] = """leftExpr"""
        self.vs[34]["GUID__"] = UUID('f25df314-a5fb-4a59-883f-b81d4ae86431')
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = UUID('8523d787-09e2-4d49-8c12-9de7c1f70ceb')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('e916d1a0-181c-4bfa-98e9-d5a7b506b836')
        self.vs[37]["name"] = """S"""
        self.vs[37]["mm__"] = """Constant"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = UUID('a398a7af-9670-4d3a-836a-a5bfed26b583')
        self.vs[38]["name"] = """enp"""
        self.vs[38]["mm__"] = """Constant"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = UUID('c8163fe1-f99f-42d6-9ba4-ce8b8c91d65f')
        self.vs[39]["name"] = """exit"""
        self.vs[39]["mm__"] = """Constant"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('96eef8ec-9a0c-464f-ba2d-592a38108659')
        self.vs[40]["name"] = """exack"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('514e1a89-e3b5-4582-be2c-c517aedc4fe9')
        self.vs[41]["name"] = """procdef"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('9a4dcb7a-3e42-4780-a023-6ff89fa3535a')
        self.vs[42]["mm__"] = """hasAttribute_T"""
        self.vs[42]["GUID__"] = UUID('712c222c-6f73-4c3f-a099-66aa89023ab6')
        self.vs[43]["mm__"] = """hasAttribute_T"""
        self.vs[43]["GUID__"] = UUID('b01047dd-8e3a-4cfd-86a5-e33abc8b4114')
        self.vs[44]["mm__"] = """hasAttribute_T"""
        self.vs[44]["GUID__"] = UUID('cb04dfa9-1623-4ab5-883c-96774de13afd')
        self.vs[45]["mm__"] = """hasAttribute_T"""
        self.vs[45]["GUID__"] = UUID('efb7392c-9bcd-4f20-aec1-6741edd7e4c9')
        self.vs[46]["mm__"] = """hasAttribute_T"""
        self.vs[46]["GUID__"] = UUID('2b665356-c63d-4d69-a191-c3e610f1920b')
        self.vs[47]["mm__"] = """hasAttribute_T"""
        self.vs[47]["GUID__"] = UUID('95a56e56-009a-475b-be47-87eae04d2b39')
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('f6e1437c-aec6-478e-a219-61a956eec835')
        self.vs[49]["name"] = """name"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('89ace4f0-41df-4819-a7f9-8f128e9ba4db')
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('2fe95c72-0617-42fc-af4d-1a38ae658581')
        self.vs[51]["name"] = """literal"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('f3ac6cf6-74fd-4806-a53a-a9cb10e24b1d')
        self.vs[52]["name"] = """literal"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('a23f8321-e355-4653-a576-af0475aeef92')
        self.vs[53]["name"] = """pivotout"""
        self.vs[53]["mm__"] = """Attribute"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('b98787e0-0f93-414b-9144-76204673b58b')
        self.vs[54]["name"] = """isComposite"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'Integer'"""
        self.vs[54]["GUID__"] = UUID('4ca59740-02e0-4e73-ab5e-1fd264e4468b')
        self.vs[55]["name"] = """hasOutgoingTransitions"""
        self.vs[55]["mm__"] = """Attribute"""
        self.vs[55]["Type"] = """'Integer'"""
        self.vs[55]["GUID__"] = UUID('9467a311-7649-4d52-9338-90be1a524b70')
        self.vs[56]["name"] = """pivotin"""
        self.vs[56]["mm__"] = """Attribute"""
        self.vs[56]["Type"] = """'Integer'"""
        self.vs[56]["GUID__"] = UUID('2f63cbe2-28e7-4f56-9e71-597ea80cc78d')

