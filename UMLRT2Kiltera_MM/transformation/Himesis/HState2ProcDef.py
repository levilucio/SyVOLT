

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
        self["GUID__"] = UUID('e8616c6d-be6c-48d6-afea-2d9f842b38cc')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('6a336ff8-4537-4a50-aaca-dbc46e1b9ddd')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('7c5e3de0-7554-4400-8103-77d5deab2c2d')
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = UUID('7ac72798-bf54-4e7b-b417-dc2ef20e6e8b')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('0ba04532-3021-4410-a156-48a18194688c')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('c31141e9-a616-4fa5-8c60-bf07c4b2d795')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('f6c101d2-e91e-4691-9aab-6d540ac64fde')
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('1dbf79ff-ff74-418b-812b-3ca4ce3a987f')
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = UUID('c68aeb4e-cefb-478d-ae85-550c716d02d1')
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = UUID('7700aa66-fbae-4f25-bfbe-c950b2fdf8e8')
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = UUID('2de8ceb8-8765-4cfd-915f-ad6b49a9af36')
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('042c3d3c-4f5c-49aa-ba09-b572230ffbb0')
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('0549dbc0-269a-4eac-8534-40adb5099a5a')
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('080ddd9f-f98a-47b0-b40c-8a8b2881d455')
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = UUID('720cd999-d4a6-4d03-b06a-ecab278cc4f6')
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = UUID('ee72afc0-bd23-4d27-817b-d7c0c4fe5761')
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('e0ccd5c6-f952-4b2f-98a4-ba207390a7cf')
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = UUID('f703b9f9-0a95-47f1-837d-8225c36abf95')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('204e38c9-4355-4c8f-a581-5ee1134212da')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('5d9b5305-427c-4ce7-a544-3fac7ec731c5')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('b55a582f-9eb1-4896-a715-4874e7bed6d6')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('0e707224-485d-41fa-84fb-ca917be32fe2')
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = UUID('bbcd34f5-e178-4a05-84cf-cb58c71c1da4')
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = UUID('214ccd1b-b4d4-4fdc-9f6e-7a7b1838970b')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('fd2206eb-1a3f-475c-9a58-2673b46a57e1')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('9ddf703a-31f4-4f19-a4dc-cc1bcbc20550')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('3f704755-c8f2-44ff-ad25-5f355a9f4546')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('622bd556-27a6-4522-9ebe-982c0a1f4e1e')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('03bc94ac-d85b-4bd3-854c-96a2bd56fe68')
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = UUID('5516450c-6104-45ee-beaf-e343d74e48fd')
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = UUID('f77e0f25-6cf1-4ffc-ae43-212e933a39f8')
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('45e19ba4-e9ba-432b-b2c9-c31d2d00cd4c')
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('e82a9f16-a2f6-4ac9-a46c-76bdd7494c71')
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('b981fc7e-7aaa-486c-bab8-a44845126584')
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('21e0c84b-4632-42d5-b6a1-8d3c424ede36')
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('8e96f59a-c0f5-4b5b-9d93-05d39cf4dd1b')
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = UUID('ed98c6a3-20b1-4ff2-ae76-06ab7cfc3904')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('fdfa2c92-64fd-4fcb-b998-45ecb09eab4b')
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = UUID('b63037b1-3fa4-415c-b2f4-1f6445879a56')
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = UUID('5bf158d0-b801-4cbb-ad0c-bc809961a637')
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = UUID('e073a02a-e0de-4107-8bd8-d452e5db7e05')
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('14c78667-2389-4d2e-9d53-edb8490190a8')
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('8df55399-7358-4c3b-b24d-69a1880d4759')
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('638c7ec6-32b2-4266-b9c6-b1790d162285')
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = UUID('ce27759b-523e-4b06-b4c6-059893a4db4b')
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = UUID('ccacdc91-e495-400a-bd87-81446871792b')
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = UUID('54706f46-01e6-4fd9-985f-1941745643a8')
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = UUID('de8b4441-fbfc-4cf8-bbe9-7fd1f555756e')
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = UUID('9b80a987-2732-40aa-ba04-9789a624d5ca')
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('ae963185-63be-46f9-ad13-c2f5864a8054')
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('216ce4c3-e1b3-4400-834e-1dd0dc214464')
        self.vs[50]["name"] = """pivot"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('d4bf2f1a-8541-4000-8be0-6d176b4e90fd')

