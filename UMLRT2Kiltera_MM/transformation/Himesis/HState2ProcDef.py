

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
        
        super(HState2ProcDef, self).__init__(name='HState2ProcDef', num_nodes=51, edges=[])
        
        # Add the edges
        self.add_edges([(6, 10), (10, 13), (6, 11), (11, 14), (6, 12), (12, 15), (30, 20), (20, 7), (31, 21), (21, 41), (32, 22), (22, 42), (33, 23), (23, 43), (34, 24), (24, 44), (6, 25), (25, 46), (13, 26), (26, 47), (14, 27), (27, 48), (15, 28), (28, 49), (6, 29), (29, 50), (4, 0), (0, 16), (0, 17), (0, 18), (0, 19), (7, 8), (8, 40), (7, 9), (9, 45), (5, 1), (1, 3), (3, 2), (2, 45), (5, 4), (30, 35), (31, 36), (32, 37), (33, 38), (34, 39), (16, 6), (17, 13), (18, 14), (19, 15), (35, 46), (36, 47), (37, 48), (38, 49), (39, 50)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """State2ProcDef"""
        self["GUID__"] = UUID('fee161c6-13a1-4aa3-a351-525a93ec9060')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('d31bca22-17bd-4f7d-afd3-c947a8cee6bc')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('ff2c601e-47cf-4ff1-aec7-bf45b9acc89f')
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = UUID('2a9050cb-c4e7-40fa-94e7-7ddbfa3917c9')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('3b750157-7c10-4e23-b397-3f9a176f5151')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('e985dd97-acf3-4818-8fbf-f4026683be88')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('def29cfc-079c-42cd-97ee-9606fc432450')
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('214bac5a-9d12-45dc-9f58-0ce29d206ee2')
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = UUID('36fc3181-2e94-484f-add7-eeec4e84d144')
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = UUID('ac7e31f9-d1cb-4def-a212-4b86679d272d')
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = UUID('cc8f99bd-b342-4a07-a2c7-c4ab65955bdc')
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('4877cf0e-5681-40e8-9b22-5fea77d87c22')
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('1edd64c9-bae8-40ad-a9f0-c8f6d8520362')
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('bcb749b8-c695-459d-b9eb-59e0a2829d30')
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = UUID('828167bc-22ba-4ec7-89e4-55117ca39916')
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = UUID('f1d1f455-1b4a-4973-a452-25af0436166f')
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('50cfa038-ce25-423a-91a9-48bdb6ccd9e0')
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = UUID('df102b00-b136-4f7b-a840-56375c69594e')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('5aa07b63-f0a2-4aad-82c0-18975c5d4fd4')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('695d5a77-9f46-4eb4-a6ed-ff58e181fce5')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('0101265c-05da-48eb-96f1-339af3c260ae')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('a8550f62-8aab-4372-8bd9-677cff66611d')
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = UUID('1feff598-f660-49a0-a75b-989501651704')
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = UUID('5430bcd1-b36d-4b05-8714-734a1f97c623')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('42b7bf98-1bf2-4962-8b34-57228ec34e71')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('034c2f46-ca1e-4848-95dc-95ede23b1315')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('57fce339-a003-462e-a860-1c932db1769d')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('94955509-6f51-4626-b7bb-5ba64bcf623c')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('e9ba2d87-9619-4645-ad9e-04a4120d2f18')
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = UUID('8b8d7e52-eb44-4242-9000-eb9cdd972955')
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = UUID('3fda2e6d-6047-46d3-a44a-be16f05ab200')
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('33e17b5c-870e-487f-97a1-5ae291ee5dd2')
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('53543a51-b46e-49c8-9c23-fb9dda9bbcad')
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('b13d3655-ece1-433e-9f57-af82371f576a')
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('34851cb3-5d53-4af3-b018-7bdd1de03a3d')
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('d36a74eb-7faf-4931-a066-3f8f6e7143fd')
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = UUID('a371b3a4-15a3-4e15-a03d-cae03d7567d2')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('54e42f46-2ab9-41f9-a7ad-c44fa55f5a35')
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = UUID('41adb462-d3a4-41a8-be7e-360dde801eb0')
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = UUID('faaa814e-1e04-4646-b32d-d4c03490e3f7')
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = UUID('b8f72b66-498d-4252-9aec-2f5503f8c326')
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('629d95fa-7300-4901-af3c-0261b6453963')
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('23e70c41-26c5-4dc9-a5f7-af689b3d1f7b')
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('c9f4ac05-d618-421e-91eb-065e015cebbd')
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = UUID('b31103ee-055b-40d7-8e99-9e2573adc369')
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = UUID('58c356bd-4529-4ba8-a3b9-2118118e3e14')
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = UUID('a8d618fd-a836-4f04-9c63-4a910e443460')
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = UUID('a02b679e-25fe-49ae-8fa5-6273e4b33115')
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = UUID('ddc13e21-8b14-488b-84af-e8774119038e')
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('7ecbce20-9280-4655-922b-b962400ec983')
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('d9ed20de-6e55-4817-81ae-0a88b2b15a4f')
        self.vs[50]["name"] = """pivotout"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('d8cd12d6-568e-41a7-8568-6165f3bcf459')

