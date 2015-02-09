

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
        self["GUID__"] = UUID('84363cb9-09d2-4a2e-bd1f-71b678f2325d')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """channelNames"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('286c80e6-7c5b-4808-a506-1fb0ce999f35')
        self.vs[1]["name"] = """vertex1"""
        self.vs[1]["classtype"] = """Vertex"""
        self.vs[1]["mm__"] = """Vertex"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('2e8b7bfb-b357-4d7c-97d4-56a3cf30129a')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('91d5a461-d009-4995-a227-7c3f05a95223')
        self.vs[3]["name"] = """out2_1"""
        self.vs[3]["classtype"] = """OUT2"""
        self.vs[3]["mm__"] = """OUT2"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('e8809eb9-74e3-4d76-8d5a-5901757cfca2')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('0a1ceb04-5b18-41a4-9e53-cf6ab5af8425')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('cb907a76-7255-4362-9fc3-ef07187eff34')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('8131ac71-be0e-4095-bfb0-ecd7351e0a88')
        self.vs[7]["name"] = """statemachine1"""
        self.vs[7]["classtype"] = """StateMachine"""
        self.vs[7]["mm__"] = """StateMachine"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('aea5bcf5-de75-4586-9456-66395bb09ab9')
        self.vs[8]["name"] = """inst1"""
        self.vs[8]["classtype"] = """Inst"""
        self.vs[8]["mm__"] = """Inst"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('b60b04d3-9215-4bca-8546-c7d393dcaa99')
        self.vs[9]["name"] = """transition1"""
        self.vs[9]["classtype"] = """Transition"""
        self.vs[9]["mm__"] = """Transition"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = UUID('bbde16ff-eb08-46a4-8ce0-92f9760acc27')
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('6ff598bb-fe44-4868-92d7-d6392ec8c5b6')
        self.vs[11]["name"] = """name1"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('3d66ecc2-38a9-4263-9631-8c2ef8e323fb')
        self.vs[12]["mm__"] = """hasArgs"""
        self.vs[12]["GUID__"] = UUID('2ebfe760-c2e3-4134-80f7-8d768c53efd4')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('63a56c7c-8bf5-476d-ae31-f3ed36f92d12')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('cb92926e-9a56-4d2a-b014-584b53ca63b3')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('350e491a-152e-420b-b302-dc8caa90e8cf')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('e5a80c1f-9677-483c-ae38-cf958d04fc54')
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = UUID('f6cff0ea-fb7f-464f-b49e-38d6156446a8')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('55d5d1f4-f388-4e5f-975e-ebec645c1311')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('8530e0e4-a21b-4872-8fdc-f4e4aefd6ffc')
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = UUID('7a06b2d8-06c0-4a21-a21b-e70a80d1c886')
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = UUID('bece98a8-69ee-4ae5-9d79-ed5997f863e0')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('0a3594da-2b14-4230-8510-0eb248f8644e')
        self.vs[23]["name"] = """eq1"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('507bd2b4-23d4-44a7-acc8-b7b2ae727b5d')
        self.vs[24]["name"] = """eq3"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = UUID('b369c647-c5f2-4a3a-914f-de01850c2055')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('b307f68f-3543-4cdb-a58c-5be1737202ec')
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = UUID('d0bdb9bd-5a8d-4045-982a-3f2b246df293')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('088f14d5-937a-4f87-a2ea-3b1a54ed21ce')
        self.vs[28]["name"] = """sh"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('e5b7902e-f87d-4174-958b-ea9a8e23e86e')
        self.vs[29]["name"] = """B"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = UUID('9b01abbb-b7f6-4a4e-99fd-7b76a33a32be')
        self.vs[30]["name"] = """instfortrans"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = UUID('0710dfde-03db-4feb-acb8-bffb8930d0fb')
        self.vs[31]["associationType"] = """type"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = UUID('4caea9e4-1bbe-4e29-82d7-4df703989026')
        self.vs[32]["associationType"] = """owningStateMachine"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = UUID('7f9cb2eb-3c87-4222-ab15-3a876bf63d14')
        self.vs[33]["associationType"] = """exitPoints"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = UUID('f598eefc-51f9-4afd-8bef-5b6ef8105563')
        self.vs[34]["associationType"] = """dest"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = UUID('45759f36-6d45-4f44-b39a-2065f3a52675')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('f96ad0f8-e83e-4d41-8f34-03712cbd731c')
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = UUID('88a28ead-2ed6-4178-823f-fe70a5698733')
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = UUID('2358d446-0ec0-413d-88c6-2d1129811a97')
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = UUID('907fea08-9888-4f57-9be7-bfbd0f02f6a3')
        self.vs[39]["name"] = """name"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('8d2a57fa-ab40-49b8-a77e-ae70ddaca6c8')
        self.vs[40]["name"] = """literal"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('d6a59a92-b61e-42af-bb45-e01b37d0fb96')
        self.vs[41]["name"] = """name"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('0be2e1ff-a3a9-45f1-8202-f7a35c03ce80')
        self.vs[42]["name"] = """pivotout"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('005eecdf-6ed7-4763-99e8-e9d1c99a4117')

