

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HBasicState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef, self).__init__(name='HBasicState2ProcDef', num_nodes=53, edges=[])
        
        # Add the edges
        self.add_edges([(8, 12), (12, 4), (4, 13), (13, 7), (7, 14), (14, 5), (29, 23), (23, 47), (30, 24), (24, 48), (31, 25), (25, 49), (32, 26), (26, 50), (33, 27), (27, 51), (34, 28), (28, 52), (7, 15), (15, 37), (5, 16), (16, 38), (8, 17), (17, 39), (4, 18), (18, 40), (3, 0), (0, 19), (0, 20), (0, 21), (0, 22), (6, 1), (1, 2), (2, 10), (10, 35), (2, 11), (11, 36), (9, 2), (6, 3), (20, 4), (22, 5), (29, 41), (30, 42), (31, 43), (32, 44), (33, 45), (34, 46), (19, 8), (21, 7), (8, 9), (41, 35), (42, 36), (43, 37), (44, 38), (45, 39), (46, 40)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = UUID('62451131-cdd0-4d52-b944-c71b025643a6')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('d6c6d0a7-dd88-4ec6-8b71-06c94129e993')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('34842bec-d3ec-4476-ac8d-ddbc8c1316ea')
        self.vs[2]["name"] = """state1"""
        self.vs[2]["classtype"] = """State"""
        self.vs[2]["mm__"] = """State"""
        self.vs[2]["cardinality"] = """+"""
        self.vs[2]["GUID__"] = UUID('c55571b8-11e5-459e-866a-f70ba675ddbd')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('0be5d576-a25b-43af-8927-39f0c1e0f850')
        self.vs[4]["name"] = """listen1"""
        self.vs[4]["classtype"] = """Listen"""
        self.vs[4]["mm__"] = """Listen"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('62bd2f9a-8f96-4f8f-9002-68bc11e5e0e8')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('d5ed1d01-fda5-4356-a80d-3b58fa9a41ae')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('a00181ff-2cd3-4d11-9824-94475e1f62af')
        self.vs[7]["name"] = """listenbranch1"""
        self.vs[7]["classtype"] = """ListenBranch"""
        self.vs[7]["mm__"] = """ListenBranch"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('199eb0b8-7e02-428f-9f5b-9168117bbecf')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('0faceec4-1547-4540-980c-1284cceb63b2')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('7685f881-8515-4fc0-863b-7074d5055bbb')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('9279038c-e0bc-4d52-8f49-47148d7cb6a7')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('d3ad5998-f586-44d3-9dae-dc95a3f660f1')
        self.vs[12]["associationType"] = """p"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('13db1c45-2d69-407e-9c6f-cbb6e3b7425a')
        self.vs[13]["associationType"] = """branches"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = UUID('2d169280-7e63-418d-a14a-6c751c4e2a0f')
        self.vs[14]["associationType"] = """p"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = UUID('57a7f707-7818-48f2-8434-e6df19e527f9')
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = UUID('bed9514d-19cd-4fa7-b0ba-f8b57d0ff021')
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = UUID('8154aeee-acb7-4c05-8134-f2b801ea6b69')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('6ba8fb73-388e-4792-b03d-6e277530eea5')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('824411ef-8a7f-4481-9ba5-a9d46fb53c72')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('7fca3363-c97e-4090-b7b3-8ac591d21973')
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = UUID('73ee0e10-ac50-4350-937a-82d4813cc727')
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = UUID('6b3d610b-323d-4cd1-a1e2-27cd898cf395')
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = UUID('e15333dc-81c9-4685-96ac-965376ef0069')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('44a14018-2b4f-4847-b152-8c76bbf8659f')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('696ee06c-e48b-4554-a86b-2095c880d35d')
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = UUID('61ec1ab1-ad95-44cd-bc85-3f33a5588763')
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = UUID('66f5c6e4-d739-46f8-9275-d97f4704d64e')
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = UUID('e95fe091-9f3b-42e1-984c-fa7433e6bc90')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('56a0c586-4738-4336-b012-39a49de95236')
        self.vs[29]["name"] = """eq1"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = UUID('0051d109-6bf5-48eb-9668-459f9bd4c767')
        self.vs[30]["name"] = """eq2"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('a5781420-bb9e-4468-a629-9ee0db1b754f')
        self.vs[31]["name"] = """eq3"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('442d389d-aba0-4107-8a49-2f0698122ba6')
        self.vs[32]["name"] = """eq4"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('51556b01-0d49-4d0f-8bf8-98bf6ef5ba41')
        self.vs[33]["name"] = """eq5"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('5d0023d0-97e3-41b7-b476-8a32f9bfa549')
        self.vs[34]["name"] = """eq6"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('96e43c03-f33a-4012-bc82-12821d62b67f')
        self.vs[35]["name"] = """isComposite"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'Bool'"""
        self.vs[35]["GUID__"] = UUID('ae9208e5-fb6b-45f8-a316-281d049b04c8')
        self.vs[36]["name"] = """hasOutgoingTransitions"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'Bool'"""
        self.vs[36]["GUID__"] = UUID('a6605a3b-afe3-451a-83f9-6dbf529e172b')
        self.vs[37]["name"] = """channel"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = UUID('f4227220-ce5d-47c2-ba2c-ca22ca8cf8e9')
        self.vs[38]["name"] = """channel"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = UUID('05cf184c-6b61-4e96-85c5-99015e691423')
        self.vs[39]["name"] = """pivot"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('ca775fc8-1de6-4cda-96d5-e935917931ba')
        self.vs[40]["name"] = """pivot"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('f6aa8be8-17f0-48ec-9ddb-bbbaf5e38d60')
        self.vs[41]["mm__"] = """leftExpr"""
        self.vs[41]["GUID__"] = UUID('7746eb58-64e3-4822-9fa2-f92e96e17d06')
        self.vs[42]["mm__"] = """leftExpr"""
        self.vs[42]["GUID__"] = UUID('83a8c467-f330-423e-9fc4-65eaa2b0bdc3')
        self.vs[43]["mm__"] = """leftExpr"""
        self.vs[43]["GUID__"] = UUID('3bd32900-93c2-474b-ae6b-1056c39d9793')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('4a97e794-db0f-4d4e-8613-ba3752636eaf')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('0e8efcd0-b50e-4cbe-b777-0dd57b39f57e')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('86d4757c-92a1-4dd7-8cc9-70084121a829')
        self.vs[47]["name"] = """false"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["Type"] = """'Bool'"""
        self.vs[47]["GUID__"] = UUID('a1097d3d-1d48-4461-b83b-dca6fa447e20')
        self.vs[48]["name"] = """true"""
        self.vs[48]["mm__"] = """Constant"""
        self.vs[48]["Type"] = """'Bool'"""
        self.vs[48]["GUID__"] = UUID('2f866c90-5c2a-470f-bf50-daae5179e344')
        self.vs[49]["name"] = """exit"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('1ff10b7f-2095-4fb4-9346-b97e47a9eee1')
        self.vs[50]["name"] = """exack"""
        self.vs[50]["mm__"] = """Constant"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('5ebd59b5-48ac-43ea-9f8c-d02f4384fd91')
        self.vs[51]["name"] = """procdef"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('deb6e541-bf50-4c9a-aac6-5ac0fc772695')
        self.vs[52]["name"] = """listensimplestate"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('9ff2be00-5484-469f-9238-c83066bd36da')

