

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
        self["GUID__"] = UUID('78502d93-2aa8-4673-8040-443189b75867')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('8add7e58-4f3a-4326-8990-2a01ed85c739')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('571f8dbb-475e-463e-8887-3f7cf0a0536d')
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = UUID('ecba80aa-2e71-4866-a4b3-83158b720a88')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('a4696d60-f104-4f32-a6ee-cf3f67b679e0')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('7e8ebe3c-3991-470f-974b-2315ff9bf9a7')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('5c8a6cec-5ca1-4dad-ab5b-bb155f5ca259')
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('81d844d7-0d79-4799-a44f-c1d43ba7d462')
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = UUID('1cda59bb-c9dc-46d6-adca-79ed83b12c26')
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = UUID('a34d1b7c-f900-4b28-af8f-a65196dbfae3')
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = UUID('9c701599-0c18-4d01-8cbf-ab7b4610abaa')
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('c12b0338-e593-4e2e-9069-f34fe10f872e')
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('7d2c8b2e-aeae-4f0a-8f3f-f4c58c0cc508')
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('5c74b636-4687-44ac-ac92-b2aefd438283')
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = UUID('0362c5b2-f9da-4965-b9d7-f1b3cc727a7f')
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = UUID('588a28b8-ad74-4546-ac72-dd6b6884fc82')
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('52123033-ee9c-4e64-9383-affddac62ac0')
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = UUID('d492c643-4c79-4964-844d-147da9b489ae')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('50c18e94-e19b-42b3-8b33-1d96a37f08c6')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('e3986ffb-9c82-4951-a7e7-e9abfd5fd1ef')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('938616b7-fe71-40eb-ad7c-1cc5dc54a50d')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('bab200f5-bc28-4dd8-8af6-7e765d53c30c')
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = UUID('12c09355-c612-4dae-b1e2-b2d1f9ab150e')
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = UUID('91c1ceeb-d4dc-4c0b-a717-67e0519b417f')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('29b2deda-85e6-4024-bcd7-122e41b64440')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('1ea30f45-e180-42d6-a5f2-e87113611af7')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('3c5b17b8-cedd-4b1d-b791-fe5c680c7db0')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('bcc74f78-d666-48de-8ed4-0343795d79b9')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('7e9aaeaa-c6e6-4d5d-b832-9d1df7a2eff3')
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = UUID('f0ba2922-0963-41c8-b5ba-81d2e47db1ca')
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = UUID('a9d1751b-4308-4494-a6a4-01f211c8a62b')
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('67a49252-5855-44d8-9490-0a3dbce5bfed')
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('5c871fcb-179f-48cd-9229-fa803c819574')
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('9a99a013-116f-4d40-a12b-039674f32b93')
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('532c9f20-da83-4d35-953d-7223fcd22907')
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('0bb6282c-5410-4de6-9dc2-911d5aae0067')
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = UUID('1626c837-74d4-4cc4-844e-ce1536bc8fac')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('9ffca102-e8fe-4cfc-ab77-26d881a2f076')
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = UUID('de798926-96c9-4f33-83a4-cc114da7a36b')
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = UUID('81eb325a-97f6-48e1-b44a-74011ab6e078')
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = UUID('4b9a4f62-5702-4269-844f-3e5357d0c848')
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('0c6ac74c-b589-4d65-8ad3-3075c90b2f23')
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('b94a46a1-5232-4363-8d12-c7c6d1d72748')
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('2a4230cf-b625-4933-9b71-e2ae36698897')
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = UUID('879d6bb5-cb9d-46f9-9100-f05a4177482c')
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = UUID('cf8854ef-ff6d-4148-8fe4-a5eb17775c95')
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = UUID('afdcec56-a4b5-49eb-a91f-4782236a94fa')
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = UUID('d1ded168-67b3-46b8-9884-6922ff5fe0b4')
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = UUID('8cb890c3-999d-44c9-9c8a-e14cc1bcbb54')
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('cc294ea7-ee66-4076-8d9e-df2684988b60')
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('f1adcf7d-4b56-4840-840c-7d83949dd7c9')
        self.vs[50]["name"] = """pivotout"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('8204b7c1-c62e-467f-90e0-6c2931f8d9a5')

