

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
        self["GUID__"] = UUID('b052fa19-909c-4a4a-86a8-de3cc7c9ec64')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('50c11696-11df-4fcc-ae13-44df1c706bec')
        self.vs[1]["name"] = """state1"""
        self.vs[1]["classtype"] = """State"""
        self.vs[1]["mm__"] = """State"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('b895f127-ec9d-43a8-bc25-63dbf28145cd')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('e41524af-b128-4746-b1c5-a9bbaf5661c5')
        self.vs[3]["name"] = """listen1"""
        self.vs[3]["classtype"] = """Listen"""
        self.vs[3]["mm__"] = """Listen"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('f1dc1aa7-e872-4b0e-b4af-809f26f6cb3d')
        self.vs[4]["name"] = """triggerS1"""
        self.vs[4]["classtype"] = """Trigger_S"""
        self.vs[4]["mm__"] = """Trigger_S"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('472b59ea-3f52-4bc8-8bf1-c828738ecde0')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('5c1a45fe-772b-4eed-aab4-bc5b108d5dca')
        self.vs[6]["name"] = """listenBranch1"""
        self.vs[6]["classtype"] = """ListenBranch"""
        self.vs[6]["mm__"] = """ListenBranch"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('f1ba87e8-75f5-46ce-b070-6b840453fcb3')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('33431bf0-14a4-4f56-ab33-51bfa71de3de')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('2d3c7f2c-8b0e-44ef-8371-04272e4e8600')
        self.vs[9]["name"] = """signal1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('314020e8-78a7-4c53-a48e-fea9512cc4f2')
        self.vs[10]["associationType"] = """branches"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('1dfbe7e1-a569-4d8b-816a-9e041f33fd01')
        self.vs[11]["associationType"] = """p"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('e89316ae-79e4-447c-a831-4b36e12e3359')
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('7aae0062-bb3e-4e9b-bec4-f719cf14cd34')
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["GUID__"] = UUID('a1e8d642-7866-4a05-bd21-077408b1ede1')
        self.vs[14]["associationType"] = """outgoingTransitions"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('e213543f-41f8-44f3-a0f4-f88d2b5e8b71')
        self.vs[15]["associationType"] = """triggers"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('15d873b6-013c-4b49-bddc-cec0a4e0de79')
        self.vs[16]["associationType"] = """signal"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('975a95a7-8fd9-4d1b-885c-182aa5f9820c')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('915f5dea-70d4-4ffb-b6de-58dd9be937ea')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('4ec5b698-ccff-48c9-9f3b-2ee9c8a8d3c6')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('56f90255-35c8-497c-997e-2a458cb085ca')
        self.vs[20]["mm__"] = """hasAttribute_S"""
        self.vs[20]["GUID__"] = UUID('3c04bd0f-afe4-4463-8fe4-8c737786130b')
        self.vs[21]["mm__"] = """hasAttribute_S"""
        self.vs[21]["GUID__"] = UUID('86cc318f-3293-4600-96d3-96cf0c525aa5')
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = UUID('b80400ed-3801-4d75-8238-95ba302f980c')
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = UUID('4b96578c-921a-4973-a16d-a198a2e03918')
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = UUID('91c2765a-ad0e-4ae0-9658-b66efa788e5d')
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = UUID('954c760a-c931-4210-97bd-bd443eefa14b')
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = UUID('987ddfd0-156f-463b-a9bc-2f2786860856')
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = UUID('5428bb4a-68c6-4908-8938-9bce32c1d058')
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = UUID('6b5f8a56-612d-4d57-a76c-f2da13dabe2e')
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = UUID('c9b0b7ee-9d8b-4210-99cd-a6d512cc57ff')
        self.vs[30]["name"] = """false"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('ee548e65-fcca-4b48-8934-94aab7db0db7')
        self.vs[31]["name"] = """true"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'Bool'"""
        self.vs[31]["GUID__"] = UUID('3e717748-a6ec-4e76-bdf3-22d72cdbecd5')
        self.vs[32]["name"] = """listensimplestate"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('9c1e95bd-5b1d-47e8-b4be-8bcc8a68a419')
        self.vs[33]["name"] = """instfortrans"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = UUID('3488b503-6f39-4980-bd0e-40f6a6a29ad9')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('0646c3b3-1525-49a1-bfd5-7f93a745fd93')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('5edf9492-5510-40eb-a040-067b6b3867a8')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('00bdc1bc-25ce-4bdb-bb2a-0e3b7e819af8')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('879f86af-34c8-46f8-9a0d-e28d4f1ee5b1')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('757e1961-f913-4074-9454-6063910a3dfb')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('f0478a8d-4e6f-4e26-82ab-6834953ffdad')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('0356a1ac-7310-4afa-a97b-b8a80a765506')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('2679fe35-a9a3-443e-807f-b087a96ebd2e')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('38a7f564-1d3d-4ebd-8293-58e145bf0701')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('3b51f17f-48d6-48bb-bfae-b5c6dc81332f')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('5d88e484-3074-4735-bf40-39f2cd26d732')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('5003f242-72df-4803-9e5a-49c673c11b47')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('035ef6e4-baf3-447f-8147-4adaf26b248c')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('c7e4d1f8-8b64-430b-b964-42ee900223b0')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('af75b6c5-7800-4f3b-9e96-5c75c3fd043c')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('0065bdce-c43e-4d01-bcb5-cb8ad31d35ae')
        self.vs[50]["name"] = """hasOutgoingTransitions"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'Bool'"""
        self.vs[50]["GUID__"] = UUID('520d0c94-e633-4d74-8f39-e97c740c1c93')
        self.vs[51]["name"] = """name"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('c51e445f-75fc-45fb-a49b-0a348e25cd0e')
        self.vs[52]["name"] = """channel"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('875bd5f0-460b-47f8-a375-9d43cb5890ff')
        self.vs[53]["name"] = """pivot"""
        self.vs[53]["mm__"] = """Attribute"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('30e03e70-d595-453c-8fd0-b6528d367ba8')
        self.vs[54]["name"] = """pivot"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('06e30000-a28e-446c-b5c3-2b8d57f196dd')

