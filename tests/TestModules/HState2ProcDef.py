

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
        self["GUID__"] = UUID('1b1d5be4-8b34-4e98-a46a-a78bcdc03a3e')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('9bdde5be-160a-4a83-8b71-8015c6b54eb5')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('7390e96e-473b-4c02-8b8b-6d41af9f3679')
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = UUID('7c924c49-bc38-4c0d-adff-cc425df95a47')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('6ceb3c83-e72f-471f-a0d9-d40e4d27ea09')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('b56c9ea0-9fc1-4474-b5a4-bbeee8ebc9c5')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('715120d3-7f9f-4a9a-8917-3c13b02195e7')
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('996b1872-c3ec-4cd2-8773-311697212c32')
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = UUID('c523b1d2-da87-4d84-97e6-32efbe605f03')
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = UUID('522a7b10-ddc8-4ee5-a17d-34cdfd47c826')
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = UUID('73378c90-36d6-4ce0-be37-5eeb61565a57')
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('a035f562-e2d8-42b1-9e76-00e8bdafea77')
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('ba1d57bd-5ebc-453c-8737-f2063cb4418f')
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('dd65a21a-3701-4f33-acdd-1aa5f8f09d91')
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = UUID('8d28608f-0416-441e-a30c-662ca4b8bdac')
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = UUID('925c2ecf-4adb-4ee2-9d35-4390a55a357e')
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = UUID('c0966f97-3a5f-4488-a320-2d52aa8f18f0')
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = UUID('d51c90f5-2411-4a25-98a4-3227c1e9b7ce')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('6bd0e5a5-2073-425b-bd1f-d72760591315')
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = UUID('772dd40d-8e1c-4275-b5bf-df2171b79ecc')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('9be20a8f-9180-4def-9875-6902cf3d5298')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('5bf32911-420f-4ac0-b6ba-96b6bb5058fe')
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = UUID('e5b15c53-1270-42e9-aea4-df7874b82812')
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = UUID('61f56d12-5736-4af4-9c4a-bb95548627eb')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('79efcd69-50c1-4e4d-9d8c-bcdc8918bb98')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('d57299d0-5cbc-4fda-bde7-d0b032ee25f6')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('75ffc694-cd8e-4f80-a521-329aaf2e6b04')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('416d1060-7daa-48e0-8fe2-c02b50e5c72a')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('8abdca34-b91d-4cb1-a69c-ea8f138f4b33')
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = UUID('ed29442e-3229-4461-b9ff-13d818c91c15')
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = UUID('3a902326-8ceb-4f55-8ded-067b04c8aa13')
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('2ddfba1a-7084-49e5-bcb6-66f449b34e3d')
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('2e789dd1-abf7-4a36-a8ea-aa21ef043e6b')
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('0661ed20-c56f-4ebe-80f3-060a3189576d')
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('3210bca8-8be1-4c46-baf8-84313bac8572')
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('f3ee404b-54c6-4877-8e20-8b425d833296')
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = UUID('847213f7-febc-4349-894c-7f65d27552d6')
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = UUID('a9f09552-5f56-4f33-a6a2-94c793e6fc35')
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = UUID('2e89e043-671a-407b-954a-5d28c081cb02')
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = UUID('444e1fd6-2ca0-4514-be75-58afb33fffb2')
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = UUID('58c2a6b7-3ff7-4b05-a113-5964f2cc0e45')
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('e2ace13c-5a03-413a-a357-da03885f161c')
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('1614944d-40c0-4ec4-b9e1-8d94518c3743')
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('133d3172-187d-4fb4-abd4-d9a620215138')
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = UUID('47720f6e-6c77-4554-bbd2-726aaac29653')
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = UUID('712c4a20-65a1-4821-86cd-526df25ce626')
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = UUID('fbdfcff5-a925-49d5-b6ae-81014d405d4a')
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = UUID('cc689901-8834-4675-9926-5f3177672020')
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = UUID('4adb2bf4-8e9d-4f04-b438-515164fdc8a1')
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = UUID('1cb41eda-c88d-4719-9cb9-2e77e1c13588')
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('9c2b8363-1edc-4c88-b857-806f31bf94fa')
        self.vs[50]["name"] = """pivotout"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('8ca21011-f1ec-42b5-bb28-54c51a2c9bd7')

