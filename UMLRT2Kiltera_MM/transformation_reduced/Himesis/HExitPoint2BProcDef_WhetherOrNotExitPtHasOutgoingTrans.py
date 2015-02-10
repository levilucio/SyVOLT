

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, self).__init__(name='HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans', num_nodes=64, edges=[])
        
        # Add the edges
        self.add_edges([(3, 0), (0, 10), (2, 19), (19, 7), (7, 20), (20, 12), (7, 21), (21, 9), (9, 22), (22, 5), (39, 33), (33, 51), (40, 34), (34, 8), (41, 35), (35, 53), (42, 36), (36, 54), (43, 37), (37, 55), (44, 38), (38, 56), (7, 23), (23, 59), (12, 24), (24, 60), (5, 25), (25, 61), (2, 26), (26, 62), (9, 27), (27, 63), (4, 1), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (8, 13), (13, 52), (8, 14), (14, 58), (28, 2), (2, 11), (6, 15), (15, 3), (6, 16), (16, 10), (3, 17), (17, 57), (10, 18), (18, 58), (11, 3), (6, 4), (32, 5), (39, 45), (40, 46), (41, 47), (42, 48), (43, 49), (44, 50), (29, 7), (30, 12), (31, 9), (45, 57), (46, 59), (47, 60), (48, 61), (49, 62), (50, 63)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = UUID('9a5d8e88-0fdd-4097-9880-99d97ae786f8')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """exitPoints"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('e5d4918f-5b4c-43e4-85b9-d102cc9864da')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('c1bd8725-071e-40c8-ab6d-a32fed65a6bd')
        self.vs[2]["name"] = """localdef1"""
        self.vs[2]["classtype"] = """LocalDef"""
        self.vs[2]["mm__"] = """LocalDef"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('8ac072f6-5da2-49b3-a0fe-0edbc84fbb79')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('3fb586b2-c58f-4a53-83b9-01c06ab1e45d')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('cc03af79-ed8e-40df-903a-7863def6ab5e')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('57b80b6d-ba84-4d17-9fb9-eb5e5da69a0f')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('17dc0457-f713-49be-bec8-3bfe3a6e4cd7')
        self.vs[7]["name"] = """procdef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('441ecffe-46e9-4eb1-8fff-48bfa3a0bc6c')
        self.vs[8]["name"] = """concat1"""
        self.vs[8]["mm__"] = """Concat"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = UUID('bcbbeeab-4acd-43bf-91a2-f41784257055')
        self.vs[9]["name"] = """par1"""
        self.vs[9]["classtype"] = """Par"""
        self.vs[9]["mm__"] = """Par"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('17383f55-8caf-4770-8c3d-0655d59922f9')
        self.vs[10]["name"] = """exitpoint1"""
        self.vs[10]["classtype"] = """ExitPoint"""
        self.vs[10]["mm__"] = """ExitPoint"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = UUID('af91e5a2-67c4-4b0a-b528-66315fa1f67a')
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('f4eca68b-0262-4d69-a6da-678cf1a57853')
        self.vs[12]["name"] = """name1"""
        self.vs[12]["classtype"] = """Name"""
        self.vs[12]["mm__"] = """Name"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = UUID('935df064-d28f-4545-a4e1-4c5574a1ffe1')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('10114e57-be9c-4a17-ac52-dc79d7141380')
        self.vs[14]["mm__"] = """hasArgs"""
        self.vs[14]["GUID__"] = UUID('7de42cea-8467-424e-8a88-2b8e1adf592e')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('70a122f5-4130-4a3f-802b-93f2bab1699a')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('be1e450e-d08a-429c-8469-7d0e8df105e1')
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = UUID('ef987f62-e5dc-432b-ae8d-c4581462b5e0')
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = UUID('263ba6a8-158c-44b2-a356-b50b1c26cf07')
        self.vs[19]["associationType"] = """def"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('940cde40-c2de-4ccb-904f-e1e43b4a7768')
        self.vs[20]["associationType"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('26aa638a-5489-423a-b896-641f036da3af')
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('02fc4d15-b9f1-41b4-97f2-6d2554ffa689')
        self.vs[22]["associationType"] = """p"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = UUID('0ff7da8c-f4c3-49a5-8199-4caf67d8f015')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('3254c8a6-ddc9-450a-b129-c6fb0f2efd1e')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('283e1252-32f7-4374-91a0-eecc4f052f58')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('d50460df-9db5-4cb2-9acc-0a07c5cdd52e')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('27886f57-6681-4071-9060-5929041d2ff6')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('b3028bc6-a6ca-4a83-996a-ce14ca07f938')
        self.vs[28]["mm__"] = """apply_contains"""
        self.vs[28]["GUID__"] = UUID('c1aec743-36dc-470d-abfd-eade12295dc6')
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = UUID('89c851cc-f7e6-4dc9-a86f-0a4baacc6051')
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = UUID('7d974bb3-d836-4df7-8a23-33d3247e8c1c')
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = UUID('e23a4608-f92b-4e41-aa37-720ef5664425')
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = UUID('abc73ad4-af9d-4f49-af48-9d925af0c8ca')
        self.vs[33]["mm__"] = """rightExpr"""
        self.vs[33]["GUID__"] = UUID('54875937-3bca-4836-8a48-54391648c336')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('4d1b1494-4a67-4145-9082-c7c7d71d8379')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('1e4f92d5-732d-4e97-8d09-e4676d1ce6a4')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('8ac35cd5-e46e-4041-bbdd-3b7041fbfd28')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('c39d81e8-4156-4573-ab09-7d01e79ab104')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('68b3e83f-a7a3-4d3b-bf3f-0f2806f2f184')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('d906a172-b00a-4525-a678-b5b18f359c5f')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('4357d276-109b-4e9f-a92d-5321e76de0d6')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('baad9574-0b56-4e62-b7cf-2a00fc9cb97c')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('9215c223-9f38-4d4c-9cbe-84632295ccb3')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('6ef66628-5bbc-421f-9143-da57c8ae2b3a')
        self.vs[44]["name"] = """eq6"""
        self.vs[44]["mm__"] = """Equation"""
        self.vs[44]["GUID__"] = UUID('b306bebe-0c24-43c7-9aa4-03adb32cfa6c')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('078ee05e-91ae-41c5-85dd-39063a9ffb2c')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('363fa974-a805-48f4-9847-e0b2ec143b95')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('6bd64e10-bbce-49eb-8182-90791435a253')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('74c5bf8d-4dde-43f2-828f-c65199149079')
        self.vs[49]["mm__"] = """leftExpr"""
        self.vs[49]["GUID__"] = UUID('bcbf3c36-6a5b-4104-b8c0-81c1d0cb5a8d')
        self.vs[50]["mm__"] = """leftExpr"""
        self.vs[50]["GUID__"] = UUID('f00f4772-96b0-4b17-8f17-2aff80d8791f')
        self.vs[51]["name"] = """true"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'Bool'"""
        self.vs[51]["GUID__"] = UUID('aa093a42-3a6f-4922-990e-2c6330548f18')
        self.vs[52]["name"] = """B"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('6f0c44af-0d82-4815-b6ee-add57e2868f9')
        self.vs[53]["name"] = """sh_in"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('dd1070e6-dcb4-4a88-8080-d80a17920742')
        self.vs[54]["name"] = """sh_in"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('cb3a80a8-be67-4725-8b8a-054291eee685')
        self.vs[55]["name"] = """localdefcompstate"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('97a1b5a3-fad3-44ed-921f-00e4a80f0eab')
        self.vs[56]["name"] = """parexitpoint"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('c4ff3de8-2fad-45ba-b68a-f56ee7645390')
        self.vs[57]["name"] = """isComposite"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'Bool'"""
        self.vs[57]["GUID__"] = UUID('cf5d178a-8ede-4d08-8e9b-624d1c7dd450')
        self.vs[58]["name"] = """name"""
        self.vs[58]["mm__"] = """Attribute"""
        self.vs[58]["Type"] = """'String'"""
        self.vs[58]["GUID__"] = UUID('7a794fe1-5113-43ca-a4dd-f38021fa612b')
        self.vs[59]["name"] = """name"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        self.vs[59]["GUID__"] = UUID('9bc9d43e-ec8d-4e41-9533-9cbac2c5f30e')
        self.vs[60]["name"] = """literal"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        self.vs[60]["GUID__"] = UUID('99fdc4b3-4793-4cec-8fab-bb50911c7677')
        self.vs[61]["name"] = """channel"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('6182d17d-3b01-4123-878c-20974483cf0d')
        self.vs[62]["name"] = """pivot"""
        self.vs[62]["mm__"] = """Attribute"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('30ce1a1c-946d-498c-be97-deeced6db219')
        self.vs[63]["name"] = """pivot"""
        self.vs[63]["mm__"] = """Attribute"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('89268a57-1bee-4910-abb8-5ae26d960406')

