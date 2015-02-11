

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
        self["GUID__"] = UUID('2235c9a9-129a-4ed1-a460-0f86b967f8a8')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('7c50a19b-d4aa-4290-aa5e-123ecb4ac832')
        self.vs[1]["name"] = """state1"""
        self.vs[1]["classtype"] = """State"""
        self.vs[1]["mm__"] = """State"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('8e3701f9-fc9b-42bc-8374-029c4fd9dd78')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('c7c612b3-9d05-4cde-87ab-74d9cbd285c0')
        self.vs[3]["name"] = """listen1"""
        self.vs[3]["classtype"] = """Listen"""
        self.vs[3]["mm__"] = """Listen"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('4dc728e0-04c6-4beb-baa6-1ac7f5bceee9')
        self.vs[4]["name"] = """triggerS1"""
        self.vs[4]["classtype"] = """Trigger_S"""
        self.vs[4]["mm__"] = """Trigger_S"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('dfde2c55-9c6c-4818-8bc2-32e434843634')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('b1a29b71-842d-4318-9563-b6ad34c9d409')
        self.vs[6]["name"] = """listenBranch1"""
        self.vs[6]["classtype"] = """ListenBranch"""
        self.vs[6]["mm__"] = """ListenBranch"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('6c1069ad-4e9c-4d0b-888f-dddde89bf1cc')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('d49ca585-757b-414b-ae72-0bfde8463d4d')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('d875807d-0eb8-46b9-ad2f-0ad0dcb2922b')
        self.vs[9]["name"] = """signal1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('12ec37c8-5cd1-4712-a2e0-584068428bbc')
        self.vs[10]["associationType"] = """branches"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('c89815a2-ca78-45e4-aae0-ec43975786d0')
        self.vs[11]["associationType"] = """p"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('444eb974-af7d-43fa-856e-219737f55d24')
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('cc6d8632-06f2-46f3-897b-d9a7c83696ce')
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["GUID__"] = UUID('71f2ea9e-3026-41aa-a388-e3f65c520f1c')
        self.vs[14]["associationType"] = """outgoingTransitions"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('0de9e65a-a5bf-4c4f-9613-6ccde5c55930')
        self.vs[15]["associationType"] = """triggers"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('d1482174-aa11-4310-8e29-f989e3f55269')
        self.vs[16]["associationType"] = """signal"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('52048509-69a2-467a-98c9-62c8840e5599')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('fca27130-9dcf-4ac7-b467-b6e28eda60cd')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('fbb87123-173c-4a9f-9410-fa6a06ac3f3b')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('05a69141-06c1-482b-b95c-158aaa661a44')
        self.vs[20]["mm__"] = """hasAttribute_S"""
        self.vs[20]["GUID__"] = UUID('d5d0bdf7-27a8-4541-9176-06236ce8e70d')
        self.vs[21]["mm__"] = """hasAttribute_S"""
        self.vs[21]["GUID__"] = UUID('8fb671f3-53ec-4f56-9d10-1f647c535ee2')
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = UUID('c6b6537a-1ac2-415a-814a-1a73ae117009')
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = UUID('f290e23b-d776-416a-9ddf-9e83b2e27005')
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = UUID('d2bf0cca-7b3b-4a6f-bd7a-e442701e4f71')
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = UUID('b3cf78aa-14da-4d10-abba-98367bfa2fe6')
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = UUID('55531a4a-efb2-4c91-8975-5e70d6431c76')
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = UUID('c13af220-7fa8-4057-852e-a3bd8259dee4')
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = UUID('a3ed8c09-d7d8-4710-b54a-8b9c124cb9a3')
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = UUID('ef61b591-7472-46d1-af66-db288cf65aea')
        self.vs[30]["name"] = """false"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('290d0bc4-c092-4fda-9b2e-4a07a39e918b')
        self.vs[31]["name"] = """true"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'Bool'"""
        self.vs[31]["GUID__"] = UUID('f610b38e-25da-4248-9b23-7ea3b868e640')
        self.vs[32]["name"] = """listensimplestate"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('53ca9abc-8581-4f12-ae8a-f0609b718ad1')
        self.vs[33]["name"] = """instfortrans"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = UUID('60adb7c0-48bb-4cb6-b9e0-99d34c6660d0')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('ce5085ca-2e08-437f-8b78-4e4171e3d333')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('4c5a2885-c718-4c8a-801b-cd2fb6f3b18a')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('6be2f8fd-f69a-428a-a6a1-d4d2d19d2711')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('e6d90003-62c0-40dc-aeb0-20078ce7f154')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('d028881f-e276-4f32-b0b7-910d6f62e3e7')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('fdbdc909-8122-421e-85b8-10ad72ebe799')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('2bc82a79-e87d-4c60-8757-208f1c2d65a6')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('6cf3ac7b-5090-432f-993b-01d1571788fd')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('e262fa47-809b-48f9-b8c5-c00fa5245a44')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('257dc74a-348f-4e81-bb69-a820f7a05291')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('86452915-7a11-4cd2-86f1-4d28c0d8767d')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('f3a831da-d39e-46b2-85fb-74e79331a045')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('2de904b8-6bcf-433e-922b-7ee7b2c5a747')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('c8693177-268c-42fb-aef9-24e3ecf5ce8f')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('0a8364fe-97c9-460b-972b-f65b9e5c7ce0')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('fba313f5-7fe3-4d7d-83ad-9170f7c583c2')
        self.vs[50]["name"] = """hasOutgoingTransitions"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'Bool'"""
        self.vs[50]["GUID__"] = UUID('3b657c5b-8e75-4887-a0c0-8d8912800d9e')
        self.vs[51]["name"] = """name"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('48d96b57-5dc1-4a68-8050-41abcc82dd2b')
        self.vs[52]["name"] = """channel"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('fc4da4b3-3fe5-4c87-8a09-c441ff8784c0')
        self.vs[53]["name"] = """pivot"""
        self.vs[53]["mm__"] = """Attribute"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('dac9d5df-04cb-4d98-90b1-0a9fd4eaba8a')
        self.vs[54]["name"] = """pivot"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('613f8d57-2319-4bd7-add8-221094ee6bc0')

