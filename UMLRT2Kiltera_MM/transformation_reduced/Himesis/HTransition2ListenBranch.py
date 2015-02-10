

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HTransition2ListenBranch(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2ListenBranch.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2ListenBranch, self).__init__(name='HTransition2ListenBranch', num_nodes=55, edges=[])
        
        # Add the edges
        self.add_edges([(1, 14), (14, 8), (8, 15), (15, 4), (4, 16), (16, 9), (3, 10), (10, 6), (6, 11), (11, 7), (39, 34), (34, 30), (40, 35), (35, 31), (41, 36), (36, 51), (42, 37), (37, 32), (43, 38), (38, 33), (6, 17), (17, 52), (3, 18), (18, 53), (7, 19), (19, 54), (2, 0), (0, 23), (0, 24), (0, 25), (5, 26), (26, 1), (5, 27), (27, 8), (5, 28), (28, 9), (5, 29), (29, 4), (1, 20), (20, 49), (1, 21), (21, 50), (9, 22), (22, 51), (12, 1), (5, 2), (23, 3), (3, 12), (39, 44), (40, 45), (41, 46), (42, 47), (43, 48), (24, 6), (25, 7), (7, 13), (13, 8), (44, 49), (45, 50), (46, 52), (47, 53), (48, 54)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """Transition2ListenBranch"""
        self["GUID__"] = UUID('6ce3acad-0ae8-4ea0-ac7b-77b4f27a4c8f')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('acacc3c9-455d-45f9-8be4-95d6a3968a71')
        self.vs[1]["name"] = """state1"""
        self.vs[1]["classtype"] = """State"""
        self.vs[1]["mm__"] = """State"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('26e71373-3ed3-4aae-b794-c5249be6d39f')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('b0e52405-e7c5-4df5-b05e-876bdc44d0e4')
        self.vs[3]["name"] = """listen1"""
        self.vs[3]["classtype"] = """Listen"""
        self.vs[3]["mm__"] = """Listen"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('01afda33-3c13-45c4-94aa-bd4c5c96c82f')
        self.vs[4]["name"] = """triggerS1"""
        self.vs[4]["classtype"] = """Trigger_S"""
        self.vs[4]["mm__"] = """Trigger_S"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('444f8933-c56c-45c3-82b9-ea03a2492e8e')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('afc27aac-6ff0-4d0f-893d-7892b339f6f8')
        self.vs[6]["name"] = """listenBranch1"""
        self.vs[6]["classtype"] = """ListenBranch"""
        self.vs[6]["mm__"] = """ListenBranch"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('555486e9-e0da-4a90-96a7-beafce82d20b')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('c28a6191-c932-4ac4-99dd-acb1b4dd2d97')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('ea7a089c-2b67-4c8e-a4cf-a1e387a599f6')
        self.vs[9]["name"] = """signal1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('05e5cd66-3234-40bd-a0fb-03e2a1b3ce33')
        self.vs[10]["associationType"] = """branches"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('edad9a4a-2b2d-4e23-8b5d-f9b0e79fa6f7')
        self.vs[11]["associationType"] = """p"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('a11466ed-4d4c-4c08-8e9e-690cc4c9eeed')
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('95c80366-5763-4d7c-b53f-1431757ef3bb')
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["GUID__"] = UUID('8cf0850c-2699-49b9-a9df-b44337cdc3d3')
        self.vs[14]["associationType"] = """outgoingTransitions"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('39893d0c-3f69-45d0-bd87-5785f4d87c3c')
        self.vs[15]["associationType"] = """triggers"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('486bd237-221b-472b-b182-f4523f5c2e8a')
        self.vs[16]["associationType"] = """signal"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('cab14aee-6969-4ccb-850d-f7e9720d8d70')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('b4ccd6dd-ece8-43a3-a9c3-4c292612a61b')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('c49928c3-e05f-4624-bb05-f93ef59df327')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('e32c721d-81ac-4880-afbe-0f0bf9c4b940')
        self.vs[20]["mm__"] = """hasAttribute_S"""
        self.vs[20]["GUID__"] = UUID('0d02f392-f614-4925-a7fb-06ca428892e7')
        self.vs[21]["mm__"] = """hasAttribute_S"""
        self.vs[21]["GUID__"] = UUID('f023d35a-574c-4581-a7ce-85c675a9f0b0')
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = UUID('8fbb9dff-b6b3-477e-b236-6f0fdcd6a111')
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = UUID('9e1048f2-202a-4c63-8a86-3ff459dbf9f2')
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = UUID('f9f774b3-defb-44d6-819d-608826d7b394')
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = UUID('3085a092-5e06-4e7b-a2ea-6b7aa50f424c')
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = UUID('de4dee8b-9211-4119-9900-66f18cfce212')
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = UUID('d9589ada-f529-4df4-8bea-99bd556de5fa')
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = UUID('6cf54057-b034-4342-b2e7-244f472147d9')
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = UUID('c4fa8713-2182-4ae0-b527-08c4401360a7')
        self.vs[30]["name"] = """false"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('463e55e8-a59b-4c68-98cb-db38191ab592')
        self.vs[31]["name"] = """true"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'Bool'"""
        self.vs[31]["GUID__"] = UUID('69d02f4e-9e1c-4590-a4cf-8d6f8c51235f')
        self.vs[32]["name"] = """listensimplestate"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('c8d37ac6-6ad6-4904-8886-3ec33e0b49a0')
        self.vs[33]["name"] = """instfortrans"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = UUID('dd2cb99b-1539-4efe-9304-583304735a13')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('3c599539-4bfa-4d7a-9f4a-b9f426899251')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('54d2f7ce-3478-477d-84ba-9d69634195c3')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('7cbe7edb-d258-4f8d-b7ee-7fd8a3343567')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('dc32cc71-8948-41fb-9930-17eef594560a')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('2e1c9e80-3730-4b8d-9869-514ee7c8834b')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('74fe344b-2d58-48e5-bfdc-1929224fbe2f')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('949c5a74-f807-4935-9cc4-b65d77fe515f')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('fb7bc389-8626-47b7-b73b-ad6815845afa')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('f45ce80c-5a64-44ec-b1b2-280d50332742')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('dcb9fc5b-e508-436a-8e89-4c820b9e4f59')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('e2dfce4e-4dd4-4be4-97a4-277d25442328')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('4c87b3f8-9eef-4863-9b60-bfdeb8b5d620')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('c65d5860-ad46-4f61-b07b-4b04669e1641')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('4f436a98-c80e-450c-8832-ea1114bd640c')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('298a7775-cbf4-4c1e-a0b3-2377dd376bf0')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('0aca15d5-d39a-450c-a988-447d433e46b8')
        self.vs[50]["name"] = """hasOutgoingTransitions"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'Bool'"""
        self.vs[50]["GUID__"] = UUID('be6da996-6dd6-4003-9d40-29364a4956e2')
        self.vs[51]["name"] = """name"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('844e7963-a33a-4cd6-8d2a-01ca465a3cae')
        self.vs[52]["name"] = """channel"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('9d3efed0-2940-4b43-98d8-21220572fe93')
        self.vs[53]["name"] = """pivot"""
        self.vs[53]["mm__"] = """Attribute"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('b9c271d0-fd0d-40d0-9be1-85d77bcb282e')
        self.vs[54]["name"] = """pivot"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('9f6f871a-2b82-47d4-b377-846b17365428')

