

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HTransition2QInstOUT(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2QInstOUT.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstOUT, self).__init__(name='HTransition2QInstOUT', num_nodes=43, edges=[])
        
        # Add the edges
        self.add_edges([(9, 31), (31, 3), (9, 32), (32, 7), (7, 33), (33, 1), (9, 34), (34, 1), (8, 0), (0, 11), (22, 16), (16, 28), (23, 17), (17, 10), (24, 18), (18, 30), (11, 19), (19, 40), (8, 20), (20, 41), (8, 21), (21, 42), (38, 1), (1, 4), (5, 2), (2, 14), (2, 15), (10, 12), (12, 29), (10, 13), (13, 39), (6, 35), (35, 9), (6, 36), (36, 3), (6, 37), (37, 7), (6, 38), (4, 39), (6, 5), (22, 25), (23, 26), (24, 27), (14, 8), (15, 11), (25, 40), (26, 41), (27, 42)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """Transition2QInstOUT"""
        self["GUID__"] = UUID('8b4ed548-48e5-4ac7-a45e-8510efbcaced')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """channelNames"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('c0fc793a-15ba-49d6-a739-7022d51f00da')
        self.vs[1]["name"] = """vertex1"""
        self.vs[1]["classtype"] = """Vertex"""
        self.vs[1]["mm__"] = """Vertex"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('a13270a8-d0fe-4f30-8adf-7a3d0005df0d')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('59a7d91b-ed1f-45ff-a664-610fb0a01f9b')
        self.vs[3]["name"] = """out2_1"""
        self.vs[3]["classtype"] = """OUT2"""
        self.vs[3]["mm__"] = """OUT2"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('73f66814-2273-43ff-b091-c25b0150212c')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('1859842a-c8a6-476a-9764-a9ec0d91459b')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('c5749ca7-7177-41d8-b9ae-325840ee708f')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('713a4ccd-a6f2-41a0-8402-15f3c3baee21')
        self.vs[7]["name"] = """statemachine1"""
        self.vs[7]["classtype"] = """StateMachine"""
        self.vs[7]["mm__"] = """StateMachine"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('eebdcaa0-039a-4d14-a3c2-558dae1475e0')
        self.vs[8]["name"] = """inst1"""
        self.vs[8]["classtype"] = """Inst"""
        self.vs[8]["mm__"] = """Inst"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('f269b185-da3b-4f24-bff5-089721c9c501')
        self.vs[9]["name"] = """transition1"""
        self.vs[9]["classtype"] = """Transition"""
        self.vs[9]["mm__"] = """Transition"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = UUID('c91da4ed-b531-4568-9859-44a0f18cf192')
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('ce49e64a-0db8-475a-b028-79a8ef5bc845')
        self.vs[11]["name"] = """name1"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('d30d7204-2ea8-452e-bb14-10820285cf2f')
        self.vs[12]["mm__"] = """hasArgs"""
        self.vs[12]["GUID__"] = UUID('23d61989-a712-4275-ab94-aeddd65662dc')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('3df1a930-bf5d-43da-948c-fe9c561079c4')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('9371c705-a790-4190-9f0b-6ed307c24ffb')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('3806ddce-a314-473c-b8eb-8906f4854e06')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('39eec431-ec48-4ba9-bc2e-ee70da678c3d')
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = UUID('1a0f2845-46d6-43d7-ab2c-3fb7c2638fb5')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('6e74c9dc-6010-472b-b06f-462e7168e1d9')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('e6618989-5a74-496b-a528-4afa1dcfced5')
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = UUID('9f0b2cff-7d68-4919-b19b-a165eaf03eb7')
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = UUID('78d4ca05-c16e-4c2e-a40a-eed1a9fe6ad5')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('62f77864-e483-41c6-9605-e9e6c4669055')
        self.vs[23]["name"] = """eq1"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('2d1a6ae5-b7b8-4dfa-8d37-c60a2804898d')
        self.vs[24]["name"] = """eq3"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = UUID('c7c92206-2990-4c4d-aeb3-7a430e89d6f3')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('ad88baa9-add9-4176-a0c5-1d4d40edc5c0')
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = UUID('6678ec42-43a0-4b5b-9747-606b65cca1d9')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('2ff1f063-c579-41a5-bd49-a69b4182944e')
        self.vs[28]["name"] = """sh"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('5c976c8c-2204-4957-9489-9d086fbfa3d0')
        self.vs[29]["name"] = """B"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = UUID('b4ad1b85-954f-45b7-980c-40782eab7133')
        self.vs[30]["name"] = """instfortrans"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = UUID('29f80c07-c560-41da-96c9-9cf80410e5ba')
        self.vs[31]["associationType"] = """type"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = UUID('aea50c5d-9f82-46ef-b26c-9e17b289c523')
        self.vs[32]["associationType"] = """owningStateMachine"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = UUID('cb3d3a04-4114-45e6-8a67-c3be05ee6887')
        self.vs[33]["associationType"] = """exitPoints"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = UUID('85b5e594-f100-4b20-88ab-21b545008459')
        self.vs[34]["associationType"] = """dest"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = UUID('ed87ce87-837f-4c99-badb-838e5581fd39')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('b5672513-99f9-46d7-8073-965d3475deb4')
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = UUID('66c996f8-61bf-49e6-b25e-47521a567135')
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = UUID('d06825d6-72a0-4a11-9509-219c2568a5e1')
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = UUID('585d9f8b-11b3-47e9-bb30-3296eb92f87b')
        self.vs[39]["name"] = """name"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('baf0c85c-6975-4883-a56e-f50d921c33f6')
        self.vs[40]["name"] = """literal"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('74a26082-51c5-4b08-b338-7fb204ddddc3')
        self.vs[41]["name"] = """name"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('33d4c682-39e0-4c04-a5ff-e75a509cb3ba')
        self.vs[42]["name"] = """pivot"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('e1d45d91-a620-476d-ae95-9fac4098bbbc')

