

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
        self["GUID__"] = UUID('5873381d-b4dd-48ef-9484-fad35bcc8a23')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('cd34cc6a-a5ce-40ec-84fc-9db87099ff8d')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('13aafb4f-55ea-49a5-bbe6-164cdb149b21')
        self.vs[2]["name"] = """state1"""
        self.vs[2]["classtype"] = """State"""
        self.vs[2]["mm__"] = """State"""
        self.vs[2]["cardinality"] = """+"""
        self.vs[2]["GUID__"] = UUID('f36dfcea-92d2-483d-a286-ff58046a155d')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('1e549049-07b7-4161-8983-5589a58d57ac')
        self.vs[4]["name"] = """listen1"""
        self.vs[4]["classtype"] = """Listen"""
        self.vs[4]["mm__"] = """Listen"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('eee1a615-8c0c-4ea5-9944-09d46eb8e42a')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('78f3d05b-d006-4945-92ac-9df1706b11f0')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('c26a51ad-1949-4210-a8a3-eed7baae6a27')
        self.vs[7]["name"] = """listenbranch1"""
        self.vs[7]["classtype"] = """ListenBranch"""
        self.vs[7]["mm__"] = """ListenBranch"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('ec408632-5a7b-4484-bfdf-dafc98237877')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('728cce42-3323-4d7d-83c0-3940c5e4c958')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('ae111c88-e32a-4f6f-b456-dcd7c4be6495')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('607b38ac-e96a-4cd9-8ee0-f6e87eb099a9')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('e95d9c4c-84ed-4157-b7d3-63a82620c58a')
        self.vs[12]["associationType"] = """p"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('f17e6158-fb09-4901-a1eb-c9917d944220')
        self.vs[13]["associationType"] = """branches"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = UUID('1867b52f-c0ac-46a6-b51b-cd0f49bffb2c')
        self.vs[14]["associationType"] = """p"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = UUID('2764ba28-a5ec-4f65-9af5-c6a5804390cb')
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = UUID('fb903179-a579-4ac1-895d-5ce641f4cbae')
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = UUID('07cb1baf-c7a0-445b-9263-f3f2f54097ab')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('f731a9e6-0998-4750-aa38-e7ecd80c1801')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('3242c8e2-5a87-42a3-9626-160553fbb571')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('46caa794-ae3e-4e37-a4dd-fd50814bde01')
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = UUID('ec0e4c22-938c-43a0-b41b-d796174510ea')
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = UUID('d8ff0132-dff6-4ec3-b260-1b5e43921c03')
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = UUID('70caedef-bdf4-46da-b47f-393a0a075074')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('ab4a9115-1ee3-44b5-83e6-cd2674d225e7')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('e35bd6ed-5c8c-46d9-98e4-9e905ef63264')
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = UUID('eb4d9902-f085-4147-9011-551de3ab6d97')
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = UUID('bd777f6e-ca0d-44f9-b4f6-2b19ec35b4ff')
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = UUID('2521bb06-08ec-4831-a2eb-916055eb92ef')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('e009ad6d-5333-4626-b916-8d02cfad29b2')
        self.vs[29]["name"] = """eq1"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = UUID('4633a30a-0f75-44a0-aef1-7bce21c08c7a')
        self.vs[30]["name"] = """eq2"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('526f85e2-5e63-46b0-bc84-2993b3f02ed3')
        self.vs[31]["name"] = """eq3"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('9bf2aba9-2112-411b-8e86-63a78f5a5efc')
        self.vs[32]["name"] = """eq4"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('63a34b99-b108-4149-bb4e-c85251c60a2e')
        self.vs[33]["name"] = """eq5"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('722433e0-b9e3-4b4c-984c-e1e878dc5672')
        self.vs[34]["name"] = """eq6"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('36e08570-fcc8-4374-91e1-d709a597af61')
        self.vs[35]["name"] = """isComposite"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'Bool'"""
        self.vs[35]["GUID__"] = UUID('9b045ee1-0f0b-4299-ae0c-2fee44c7386a')
        self.vs[36]["name"] = """hasOutgoingTransitions"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'Bool'"""
        self.vs[36]["GUID__"] = UUID('ed291842-ef50-454e-93e7-ac5fcf65ec28')
        self.vs[37]["name"] = """channel"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = UUID('9e614b06-e1cb-468b-9730-58276cd485d8')
        self.vs[38]["name"] = """channel"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = UUID('9eea36f3-a1b7-40a7-a26e-7719f02fd9ef')
        self.vs[39]["name"] = """pivot"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('ef9a8788-f04d-4869-8eab-91366aac96e3')
        self.vs[40]["name"] = """pivot"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('9d2a4fd4-217e-45fe-b101-e3ad56fa88b5')
        self.vs[41]["mm__"] = """leftExpr"""
        self.vs[41]["GUID__"] = UUID('3b850d8b-92f5-4c64-9c2b-2f8bc03c3ecc')
        self.vs[42]["mm__"] = """leftExpr"""
        self.vs[42]["GUID__"] = UUID('eecc9af0-0e8a-4b86-8b4d-d348671db646')
        self.vs[43]["mm__"] = """leftExpr"""
        self.vs[43]["GUID__"] = UUID('3a3ebfaa-acf5-4bef-b99f-e16e2d418cf4')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('abc7b2b5-f6ee-4790-aef3-393ed674ac59')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('f23ca636-46ea-48fc-b333-ec705558d17c')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('52b4f1a1-5d7a-4779-b514-01802ab4c4c1')
        self.vs[47]["name"] = """false"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["Type"] = """'Bool'"""
        self.vs[47]["GUID__"] = UUID('aaf0cc82-ac2e-4058-8fb6-712cdbac46c7')
        self.vs[48]["name"] = """true"""
        self.vs[48]["mm__"] = """Constant"""
        self.vs[48]["Type"] = """'Bool'"""
        self.vs[48]["GUID__"] = UUID('01fe8f40-463f-4b77-a9ee-8c729afb5b14')
        self.vs[49]["name"] = """exit"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('1c50b97b-a1fa-4e29-9a8f-8cfcebeb01d4')
        self.vs[50]["name"] = """exack"""
        self.vs[50]["mm__"] = """Constant"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('9465097b-3941-4379-b7a1-74662179e4de')
        self.vs[51]["name"] = """procdef"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('e826c5ca-d11a-4c46-a024-3bd62c490458')
        self.vs[52]["name"] = """listensimplestate"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('8af104be-734f-4ebe-ac5d-fdfa21ec3475')

