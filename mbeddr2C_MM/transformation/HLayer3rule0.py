

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HLayer3rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HLayer3rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HLayer3rule0, self).__init__(name='HLayer3rule0', num_nodes=49, edges=[])
        
        # Add the edges
        self.add_edges([(4, 11), (11, 8), (8, 12), (12, 1), (10, 13), (13, 5), (3, 14), (14, 10), (32, 28), (28, 40), (33, 29), (29, 41), (34, 30), (30, 7), (35, 31), (31, 43), (3, 19), (19, 46), (10, 20), (20, 47), (10, 21), (21, 48), (2, 0), (0, 25), (0, 26), (0, 27), (7, 15), (15, 42), (7, 16), (16, 44), (6, 22), (22, 4), (6, 23), (23, 8), (6, 24), (24, 1), (4, 17), (17, 44), (8, 18), (18, 45), (6, 2), (25, 3), (3, 9), (9, 4), (32, 36), (33, 37), (34, 38), (35, 39), (27, 5), (26, 10), (36, 45), (37, 46), (38, 47), (39, 48)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'mbeddr2C_MM'
p2
a.""")
        self["name"] = """layer3rule0"""
        self["GUID__"] = UUID('34f0b291-ac63-406d-9bc8-111b029aaa14')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('cf1341f9-5a77-4414-b416-946ba00686b1')
        self.vs[1]["name"] = """s_"""
        self.vs[1]["classtype"] = """Int32Type"""
        self.vs[1]["mm__"] = """Int32Type"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('d5bb4589-f683-4ca5-ba58-386139e25ec4')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('648f423f-20ec-4203-b539-d6245d7c66a6')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule_T"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('99608a5b-c850-4f38-8137-2d651f985744')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """ImplementationModule"""
        self.vs[4]["mm__"] = """ImplementationModule_S"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('c891b46d-f042-4b57-a67d-ebb3cab50c92')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """VoidType"""
        self.vs[5]["mm__"] = """VoidType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('a428171e-31ab-4b03-817c-83ec6c6ba3ef')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('518018c9-2f63-455d-9428-e943a45cc101')
        self.vs[7]["name"] = """exp_"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = UUID('4f938494-33fb-41c7-ad5d-62d9653d990f')
        self.vs[8]["name"] = """s_"""
        self.vs[8]["classtype"] = """Function"""
        self.vs[8]["mm__"] = """Function"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('a97006d0-a9b6-4b0a-acf8-a2aeb2ca83fe')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('3e53dabf-69d5-4ab2-becb-a9d3db5b75b9')
        self.vs[10]["name"] = """s_"""
        self.vs[10]["classtype"] = """FunctionPrototype"""
        self.vs[10]["mm__"] = """FunctionPrototype"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('25f324e5-f192-4639-bf02-9ec1d22fbac1')
        self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = UUID('a84a2fe1-3ae4-4b25-9254-b61ee203e8b3')
        self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = UUID('fe3840fe-41ec-434e-a91a-f49549099aa9')
        self.vs[13]["associationType"] = """type"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = UUID('6b0a8852-b14c-421b-84c3-7684b124a878')
        self.vs[14]["associationType"] = """contents"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = UUID('5a258d74-a69d-4bfd-8dd3-0a54e580424d')
        self.vs[15]["mm__"] = """hasArgs"""
        self.vs[15]["GUID__"] = UUID('4d4e42b0-2c5f-4194-b8bb-501bd416bd7b')
        self.vs[16]["mm__"] = """hasArgs"""
        self.vs[16]["GUID__"] = UUID('4b264faa-fb14-48ba-9c28-d3a7d685a4df')
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = UUID('66c981da-4f3a-4657-83ef-73e6c1a1640b')
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = UUID('6810f4c2-825b-4e27-86f5-04002fdf1f83')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('77f918e5-ba99-4eab-b944-b084a3c390d3')
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = UUID('80dfb4b9-80a1-44e6-844f-efce0238d903')
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = UUID('b01faa8f-0858-4b87-b059-b5ce07011b4c')
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = UUID('a5004c6e-cc11-4952-946e-7e1bd42c5e23')
        self.vs[23]["mm__"] = """match_contains"""
        self.vs[23]["GUID__"] = UUID('de0f6d52-52a1-4dd0-8490-3262b139984d')
        self.vs[24]["mm__"] = """match_contains"""
        self.vs[24]["GUID__"] = UUID('b9c3bad9-5cce-49c9-9a39-64ef82737adb')
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = UUID('56d560f9-e896-43a9-8b38-f96842a259ee')
        self.vs[26]["mm__"] = """apply_contains"""
        self.vs[26]["GUID__"] = UUID('462f9c40-d822-4a73-ab9b-801d9361453a')
        self.vs[27]["mm__"] = """apply_contains"""
        self.vs[27]["GUID__"] = UUID('ac295906-9a51-44d3-b7d4-1248b26bc386')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('2779bbe9-e846-4f5a-b457-7616f6b6bd7d')
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = UUID('74fadf43-7858-4c0d-8b4f-07a6b5d75196')
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = UUID('4069431e-4ee4-4c19-ab0e-c1729a5d980f')
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = UUID('48377092-de56-4c22-a88f-87d481ab3d84')
        self.vs[32]["name"] = """eq_"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('77943f12-f630-4730-9844-69607063aca2')
        self.vs[33]["name"] = """eq_"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('5f88aa8f-d59d-448d-90f9-8f6741c9e356')
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('6bb5d719-a3be-4651-89c7-42a8e1fd32d8')
        self.vs[35]["name"] = """eq_"""
        self.vs[35]["mm__"] = """Equation"""
        self.vs[35]["GUID__"] = UUID('a9d1450b-db1e-41aa-ab20-7b45a6b66fae')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('b6527f1d-31b4-4fb2-b42b-fda84ba83111')
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = UUID('1a4b5b37-45b2-42d3-b2f0-3db1ee5c1577')
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = UUID('004c827d-e1f6-4430-bd98-4310ca0c0f6e')
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = UUID('a4a851ad-3bae-4929-976b-838510e71cd5')
        self.vs[40]["name"] = """main"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('1642eef2-da8f-44fa-9d68-f0751054d068')
        self.vs[41]["name"] = """ImplementationModule"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('623a7efb-dcb3-4a9f-86bb-a465724c2315')
        self.vs[42]["name"] = """_blockexpr_main_2"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('54673662-ca99-4bcb-b954-d57430220863')
        self.vs[43]["name"] = """Main2Prototype"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = UUID('54e4976b-def7-421c-959d-0ebd70c22ed1')
        self.vs[44]["name"] = """name"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = UUID('f47fc016-b331-4634-b3d7-b1f0f78b3db5')
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = UUID('fa17d642-0b0b-4751-97a7-a2de239fccb1')
        self.vs[46]["name"] = """ApplyAttribute"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = UUID('17f1cc6c-3584-4458-a218-73dc0d22db97')
        self.vs[47]["name"] = """name"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = UUID('2e509bac-07ae-4b34-9221-a3ee15f47fbe')
        self.vs[48]["name"] = """ApplyAttribute"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('618498bc-dcbf-47b5-b6ef-874d4be6c53f')

