

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
        self["GUID__"] = UUID('e27ee362-3211-4b8c-8395-0a7e6b807e3e')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('a78d129e-5abf-4e83-8185-92ee88ca2719')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('bf5a67b0-1783-41bc-9a6d-51a97974c9cc')
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = UUID('658a8cf4-27d3-4099-b401-38eccdf932d9')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('192abf4e-3bd2-482e-ba68-6a6ab4805115')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('37709238-0d06-4a74-8bc0-79273f611e39')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('0066ceb6-f4de-43a8-bad9-0db73a4cfc64')
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('43c06887-317e-4848-b2be-afef632d99a0')
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = UUID('9ae3b72b-caf7-43b3-a72f-d6a63a19daa5')
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = UUID('d2f06a17-7fa6-4736-b248-505565f9ebef')
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = UUID('fdfb10d0-9e17-42e2-853d-b55ccb3e60b3')
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('8d8e9172-f8d5-41e1-b838-3275a92accf3')
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('90c70c76-7190-428f-a645-59fb4260b116')
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('62e085a1-df25-4e12-9216-ff3b37eea6e7')
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = UUID('b44a89cd-9275-4378-9e51-bb535f3af032')
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = UUID('22877fb2-d217-4958-880f-58dfc60c963b')
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('6c6a99cd-ba42-4704-a34b-b00610ae1439')
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = UUID('761a9149-014c-4a77-b129-c96aa91179f0')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('404fd24d-ad0c-45e0-9e0f-7b58291eb353')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('f88a75d4-6a32-4e3c-abe0-5b6667d7f934')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('edc97816-2853-47eb-8243-e028b6dba108')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('46a958d6-c52a-4fc0-b219-8d7462b69574')
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = UUID('b829e0ba-5e1b-41c8-be16-e1b0931fe593')
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = UUID('cf9b9cec-c0bc-4e24-a594-db864d671da4')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('d1ac0322-9604-4b42-99dd-39d4a3fdaa7a')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('ecd3e6fb-0194-4f69-bce8-d057a826c488')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('10407959-809a-4545-9db4-42801b9f50a1')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('cfe362f4-fdb5-4e60-a982-3753a7ee4b18')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('984b0eb0-f98b-4e59-8842-fdc9a236a699')
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = UUID('23399036-a4e5-4613-b295-fffa112bf3fe')
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = UUID('93a3198e-b2e5-4c73-ba6c-1dcbd1f9187e')
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('97d1eb16-a7c7-4e25-9eaf-e8e95364d079')
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('38c1ff8b-3776-4b5e-97bd-db9dcc330ef1')
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('12dc8448-87f4-441c-9c9a-9f0b66431cfe')
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('55d89fff-5aab-4377-8ace-fad6501cfc38')
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('2504d6b1-2e9c-4156-95b4-73c99bb230d9')
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = UUID('48366cdc-df32-4ec6-aff6-0a78050cb627')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('6d08562e-0da0-449c-9a25-878db29ac80d')
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = UUID('94db10f4-eda7-49c8-88bf-1885cffe0ad1')
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = UUID('9217ef7e-093b-42c3-89d0-262802080a64')
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = UUID('541f8088-5873-42e8-9999-8950279cb3df')
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('3c25fe24-3632-4606-93d2-535461ac1142')
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('2f229848-3263-4387-936d-114829451afd')
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('10873724-1e5a-4b27-a328-3eb4682608f4')
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = UUID('4fa13890-ba37-4e92-a746-99e47f766288')
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = UUID('ef1f8837-147d-4af6-a5bd-968fa13b3289')
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = UUID('4169b69a-4837-477c-b5d7-6d67e8f012f7')
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = UUID('9caa368c-7e65-4db9-af5a-7a4ddaf4fae1')
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = UUID('f8371afd-01c3-461e-b2ea-f1ba2988421d')
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('c8c47a8a-fc86-465a-87f7-11ab991d3dbc')
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('7f31cc06-de4b-4f39-bdc6-d2d317f4fcce')
        self.vs[50]["name"] = """pivot"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('59382aaf-ad0e-4832-abb1-30423d944a12')

