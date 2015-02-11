

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
        self["GUID__"] = UUID('7826b2e8-8436-4f3b-87bf-7820038605ca')
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """1"""
        self.vs[0]["GUID__"] = UUID('7cee5a9b-93b9-48b6-b78f-96a7d8f493d3')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('f89ccec0-616e-4f04-b754-f20a23076fe8')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('32190b46-66f0-42c3-9237-a532a0f22f19')
        self.vs[3]["mm__"] = """MatchModel"""
        self.vs[3]["GUID__"] = UUID('a2a436a3-4541-4857-9c8d-2efe5dc80f33')
        self.vs[4]["name"] = """stateMachine1"""
        self.vs[4]["classtype"] = """StateMachine"""
        self.vs[4]["mm__"] = """StateMachine"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('7da5e571-68a3-44f9-9871-87c8b46c740b')
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('b38f9d12-ddcf-4742-ab4a-30e292b70d0f')
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('ff800d11-c49c-44eb-bdc0-e23862b9b79b')
        self.vs[7]["name"] = """sibling0_1"""
        self.vs[7]["classtype"] = """SIBLING0"""
        self.vs[7]["mm__"] = """SIBLING0"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('fc40c5c4-956c-46d4-aa39-90a46da09336')
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = UUID('7a015a65-7aa5-4384-84c3-f8b0d31b99d6')
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = UUID('ae941113-c9f6-427a-a54c-c75bc06fa944')
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('77ef2e5c-3685-4fbc-91ce-25003220de9b')
        self.vs[11]["name"] = """concat2"""
        self.vs[11]["mm__"] = """Concat"""
        self.vs[11]["Type"] = """'String'"""
        self.vs[11]["GUID__"] = UUID('db39c28d-330a-42d4-b576-51dd4606b79c')
        self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = UUID('97b690c5-0664-47d3-92c4-2af3be566c43')
        self.vs[13]["associationType"] = """dest"""
        self.vs[13]["mm__"] = """directLink_S"""
        self.vs[13]["GUID__"] = UUID('a0e01d7f-7c35-4adf-aa39-d4ccd59343d8')
        self.vs[14]["associationType"] = """owningStateMachine"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('5beb50e5-b316-4861-985c-5371306a58a2')
        self.vs[15]["associationType"] = """channelNames"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = UUID('9b5d958d-56c5-4c00-8509-a7d7b13cf373')
        self.vs[16]["associationType"] = """channelNames"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = UUID('c65312db-1fed-4cab-9d9d-febf488a4c01')
        self.vs[17]["associationType"] = """channelNames"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = UUID('b460ff5e-be0f-4d26-9cfb-1930c497cba4')
        self.vs[18]["associationType"] = """channelNames"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = UUID('7db9e884-29ae-413c-8faa-d0a099285829')
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = UUID('a3630d93-3a1d-4d02-87f4-27370b70e787')
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = UUID('3c26cbd5-580a-4bc5-a9ce-91bb68ca03d1')
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = UUID('1fa8af12-a4bc-4605-8e04-763ad0a6028f')
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = UUID('44a9c860-d5be-4559-a879-b98c829d29a3')
        self.vs[23]["name"] = """name1"""
        self.vs[23]["classtype"] = """Name"""
        self.vs[23]["mm__"] = """Name"""
        self.vs[23]["cardinality"] = """1"""
        self.vs[23]["GUID__"] = UUID('1583fbe5-8276-4dc6-878a-621b8c104a56')
        self.vs[24]["name"] = """name2"""
        self.vs[24]["classtype"] = """Name"""
        self.vs[24]["mm__"] = """Name"""
        self.vs[24]["cardinality"] = """1"""
        self.vs[24]["GUID__"] = UUID('c5625c0c-5bb9-4582-948d-198723eb6611')
        self.vs[25]["name"] = """name3"""
        self.vs[25]["classtype"] = """Name"""
        self.vs[25]["mm__"] = """Name"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = UUID('2823f3f3-49cf-4781-8b64-73af6916dd05')
        self.vs[26]["name"] = """name4"""
        self.vs[26]["classtype"] = """Name"""
        self.vs[26]["mm__"] = """Name"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = UUID('a6973e45-4d13-4c20-b573-c063b3e9cea5')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('77258e4b-382e-4108-9c2e-fd29272cc10f')
        self.vs[28]["mm__"] = """hasArgs"""
        self.vs[28]["GUID__"] = UUID('f2bcecd7-c679-4758-bf7a-0e248f2df9e3')
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = UUID('c5b1421a-d3fd-4b3b-a02c-166277397a76')
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = UUID('2408d83f-7627-4060-836f-0465740a0541')
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = UUID('8cc9dab6-822a-4648-9407-71a80bc79622')
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = UUID('1cd1022d-8b9a-4024-b9e2-b5cba36e094d')
        self.vs[33]["mm__"] = """apply_contains"""
        self.vs[33]["GUID__"] = UUID('0030e6d1-2fd8-435c-9442-c5e0be17a9a8')
        self.vs[34]["mm__"] = """apply_contains"""
        self.vs[34]["GUID__"] = UUID('8f182984-0111-4f08-833e-915322f8644e')
        self.vs[35]["mm__"] = """apply_contains"""
        self.vs[35]["GUID__"] = UUID('bcb7456b-5338-4356-9060-b470723d6400')
        self.vs[36]["mm__"] = """apply_contains"""
        self.vs[36]["GUID__"] = UUID('1ae2705c-091f-4dc9-ae3b-99493f9e6ff7')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('b3f15036-29a2-43f6-a73f-0198d20eb6c9')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('ecb57317-c97f-443c-8e6b-df209b684a19')
        self.vs[39]["mm__"] = """rightExpr"""
        self.vs[39]["GUID__"] = UUID('0ec3c11d-284d-4ca9-a2dc-ac641ddc0152')
        self.vs[40]["mm__"] = """rightExpr"""
        self.vs[40]["GUID__"] = UUID('7ba4a3b3-a13a-49ac-bd20-56af016f4cc8')
        self.vs[41]["mm__"] = """rightExpr"""
        self.vs[41]["GUID__"] = UUID('568d247a-f9f1-45c2-bca0-4dde0ee94b50')
        self.vs[42]["mm__"] = """rightExpr"""
        self.vs[42]["GUID__"] = UUID('54912df3-fa09-47c3-a717-29865d1c3bc1')
        self.vs[43]["mm__"] = """hasAttribute_T"""
        self.vs[43]["GUID__"] = UUID('996e7cf3-27de-434a-b54a-2b8683aac6ca')
        self.vs[44]["mm__"] = """hasAttribute_T"""
        self.vs[44]["GUID__"] = UUID('33100be0-1772-4aa5-8a3e-6d17e0096638')
        self.vs[45]["mm__"] = """hasAttribute_T"""
        self.vs[45]["GUID__"] = UUID('1390b40d-31de-4df1-9421-ba20e2d2764e')
        self.vs[46]["mm__"] = """hasAttribute_T"""
        self.vs[46]["GUID__"] = UUID('b8166f6b-01da-4055-9dfa-ef68d41a23d2')
        self.vs[47]["mm__"] = """hasAttribute_T"""
        self.vs[47]["GUID__"] = UUID('e9f896bb-9727-421a-af2c-83f8a1a82282')
        self.vs[48]["mm__"] = """hasAttribute_T"""
        self.vs[48]["GUID__"] = UUID('32f6c039-a5e4-41b6-968f-e32cead38d54')
        self.vs[49]["name"] = """eq1"""
        self.vs[49]["mm__"] = """Equation"""
        self.vs[49]["GUID__"] = UUID('9ff71085-f12b-4372-ab19-3dadc8d00199')
        self.vs[50]["name"] = """eq2"""
        self.vs[50]["mm__"] = """Equation"""
        self.vs[50]["GUID__"] = UUID('c319e4a2-fc72-49b7-b6cd-ad209b83eb05')
        self.vs[51]["name"] = """eq3"""
        self.vs[51]["mm__"] = """Equation"""
        self.vs[51]["GUID__"] = UUID('09e906d9-49a0-4ed0-af65-1e00ba586c4d')
        self.vs[52]["name"] = """eq4"""
        self.vs[52]["mm__"] = """Equation"""
        self.vs[52]["GUID__"] = UUID('1f97eef1-5bb0-4283-a578-c0082c8686ac')
        self.vs[53]["name"] = """eq5"""
        self.vs[53]["mm__"] = """Equation"""
        self.vs[53]["GUID__"] = UUID('e6a9981e-fa0f-4829-9496-e882fdfc6498')
        self.vs[54]["name"] = """eq6"""
        self.vs[54]["mm__"] = """Equation"""
        self.vs[54]["GUID__"] = UUID('51f24a3b-e1ca-4e99-bf1a-6bbde9e96902')
        self.vs[55]["mm__"] = """leftExpr"""
        self.vs[55]["GUID__"] = UUID('7a0345d7-fcb9-43b1-ae38-35fdc7a27e16')
        self.vs[56]["mm__"] = """leftExpr"""
        self.vs[56]["GUID__"] = UUID('6fd750e9-1b08-43ac-8596-550717e0c064')
        self.vs[57]["mm__"] = """leftExpr"""
        self.vs[57]["GUID__"] = UUID('03a584da-0bd2-44a4-baf9-828cdb5c761f')
        self.vs[58]["mm__"] = """leftExpr"""
        self.vs[58]["GUID__"] = UUID('77ed5614-ea65-415d-8b94-0738d3f56a37')
        self.vs[59]["mm__"] = """leftExpr"""
        self.vs[59]["GUID__"] = UUID('91ced1bd-2f28-430b-bc59-89c474e01f2d')
        self.vs[60]["mm__"] = """leftExpr"""
        self.vs[60]["GUID__"] = UUID('2d09cc0c-8743-47b9-9cb6-7f40b9687666')
        self.vs[61]["name"] = """S"""
        self.vs[61]["mm__"] = """Constant"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('4535ba71-92b4-4299-9943-76b3bbe458d3')
        self.vs[62]["name"] = """exit"""
        self.vs[62]["mm__"] = """Constant"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('826dbd9b-0a48-40a8-87b0-64643e0d93f5')
        self.vs[63]["name"] = """exack"""
        self.vs[63]["mm__"] = """Constant"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('7a073124-2696-4276-b721-1ede24cc213c')
        self.vs[64]["name"] = """1"""
        self.vs[64]["mm__"] = """Constant"""
        self.vs[64]["Type"] = """'String'"""
        self.vs[64]["GUID__"] = UUID('65dfbd29-9db9-4c38-8d60-078f91a1b838')
        self.vs[65]["name"] = """2"""
        self.vs[65]["mm__"] = """Constant"""
        self.vs[65]["Type"] = """'String'"""
        self.vs[65]["GUID__"] = UUID('c503bb60-681a-428a-adc5-ba1f29535f9a')
        self.vs[66]["name"] = """sh"""
        self.vs[66]["mm__"] = """Constant"""
        self.vs[66]["Type"] = """'String'"""
        self.vs[66]["GUID__"] = UUID('119b56e4-b773-4e68-a805-e018ddaf2447')
        self.vs[67]["name"] = """instfortrans"""
        self.vs[67]["mm__"] = """Constant"""
        self.vs[67]["Type"] = """'String'"""
        self.vs[67]["GUID__"] = UUID('27aa52ae-3248-4346-ad77-c4c8c04dc733')
        self.vs[68]["name"] = """name"""
        self.vs[68]["mm__"] = """Attribute"""
        self.vs[68]["Type"] = """'String'"""
        self.vs[68]["GUID__"] = UUID('e39f04d2-4603-4994-bc1a-1cdd705182a3')
        self.vs[69]["name"] = """name"""
        self.vs[69]["mm__"] = """Attribute"""
        self.vs[69]["Type"] = """'String'"""
        self.vs[69]["GUID__"] = UUID('e72008cd-e9fa-4617-b8a3-4ba599597caf')
        self.vs[70]["name"] = """name"""
        self.vs[70]["mm__"] = """Attribute"""
        self.vs[70]["Type"] = """'String'"""
        self.vs[70]["GUID__"] = UUID('1cd4be5c-a202-4a38-91b6-a792563f6288')
        self.vs[71]["name"] = """literal"""
        self.vs[71]["mm__"] = """Attribute"""
        self.vs[71]["Type"] = """'String'"""
        self.vs[71]["GUID__"] = UUID('c0e40653-41ee-4184-86dc-64666c034f21')
        self.vs[72]["name"] = """literal"""
        self.vs[72]["mm__"] = """Attribute"""
        self.vs[72]["Type"] = """'String'"""
        self.vs[72]["GUID__"] = UUID('d1c9f76e-b585-4b18-86db-7c6465d5261a')
        self.vs[73]["name"] = """literal"""
        self.vs[73]["mm__"] = """Attribute"""
        self.vs[73]["Type"] = """'String'"""
        self.vs[73]["GUID__"] = UUID('ea4f65c9-9241-45a2-ae1b-b70269abd555')
        self.vs[74]["name"] = """literal"""
        self.vs[74]["mm__"] = """Attribute"""
        self.vs[74]["Type"] = """'String'"""
        self.vs[74]["GUID__"] = UUID('36fd97a2-aa96-495d-bace-51fd9cdbea14')
        self.vs[75]["name"] = """pivot"""
        self.vs[75]["mm__"] = """Attribute"""
        self.vs[75]["Type"] = """'String'"""
        self.vs[75]["GUID__"] = UUID('4c468953-b938-4631-8776-e0f3aef80900')

