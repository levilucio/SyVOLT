

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMapHeirarchyOfStates2HeirarchyOfProcs(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapHeirarchyOfStates2HeirarchyOfProcs.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapHeirarchyOfStates2HeirarchyOfProcs, self).__init__(name='HMapHeirarchyOfStates2HeirarchyOfProcs', num_nodes=33, edges=[])
        
        # Add the edges
        self.add_edges([(12, 0), (0, 13), (3, 1), (1, 7), (21, 18), (18, 30), (22, 19), (19, 31), (23, 20), (20, 32), (3, 8), (8, 25), (7, 9), (9, 26), (5, 2), (2, 14), (2, 15), (14, 3), (3, 16), (6, 10), (10, 12), (6, 11), (11, 13), (12, 4), (4, 24), (16, 12), (17, 13), (6, 5), (21, 27), (22, 28), (23, 29), (15, 7), (7, 17), (27, 24), (28, 25), (29, 26)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
        self["GUID__"] = UUID('e7cc23f8-71d5-4527-abfa-dfb920b289b5')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """states"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('e42862fa-b0bc-4127-bb77-fe74b426ce94')
        self.vs[1]["associationType"] = """def"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('5240ef8b-def4-4e17-ad94-beafec79caf3')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('b5e65c86-a73d-4e36-afc1-308f255d78fb')
        self.vs[3]["name"] = """localDef1"""
        self.vs[3]["classtype"] = """LocalDef"""
        self.vs[3]["mm__"] = """LocalDef"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('0817fdee-14fd-4ce9-90fd-0b85ea250077')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('588c9f52-7c86-46eb-9d47-d90642cae091')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('63ee9b61-9198-4690-b27b-ebc8e4c15e6b')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('214d3370-a71b-462b-9d93-527d4f5e0f2d')
        self.vs[7]["name"] = """procDef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('d6e402ba-ce93-47b6-beb6-01b5d2f658a3')
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = UUID('5984eea5-61b5-4e31-9c49-b75fc500a31f')
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = UUID('56f5014d-4cc9-4182-aa77-147801e16417')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('717e0019-ecbc-4735-8d13-af1eb5f477e9')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('91df193e-cefe-419d-8058-ec64157c790a')
        self.vs[12]["name"] = """state1"""
        self.vs[12]["classtype"] = """State"""
        self.vs[12]["mm__"] = """State"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('cdfc7d16-b8fb-45bb-8639-8c1b6a4939ed')
        self.vs[13]["name"] = """state2"""
        self.vs[13]["classtype"] = """State"""
        self.vs[13]["mm__"] = """State"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('bcf66b1e-adc5-4523-8fe3-57964862ac66')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('a0384bb9-fb11-4280-a2e3-0cd62de0e4e6')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('d4c6de21-ae93-496b-abea-1c5f7b784ddc')
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["GUID__"] = UUID('6a4ecb87-6962-437c-871e-d211539c5037')
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["GUID__"] = UUID('adc6910e-c0c7-4709-8d1e-f13f801ede20')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('5df1b10e-4068-44e7-80df-2bb9d985432c')
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = UUID('c294e700-af6b-419f-86e9-ec5dd19687cc')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('83f663e7-5309-411d-938a-ba000ad51dbc')
        self.vs[21]["name"] = """eq1"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = UUID('6b42a044-0439-4a17-8d23-2d6518d64f38')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('a525d91f-fcef-4870-922f-b5626b0d9997')
        self.vs[23]["name"] = """eq3"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('c10f7e4e-563c-42b3-be6a-478e45941032')
        self.vs[24]["name"] = """isComposite"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'Bool'"""
        self.vs[24]["GUID__"] = UUID('9843b342-e857-4a4c-b24f-485d95c9c766')
        self.vs[25]["name"] = """pivot"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('1bc0cd25-cd9d-43d3-a487-97a9509d2568')
        self.vs[26]["name"] = """pivot"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('fbe88a41-56e3-40a7-b3a4-ab65b3eae613')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('f92307e7-1af3-49aa-b920-bd6ed4e2ba23')
        self.vs[28]["mm__"] = """leftExpr"""
        self.vs[28]["GUID__"] = UUID('11205297-496b-4fda-b507-49aec6707fed')
        self.vs[29]["mm__"] = """leftExpr"""
        self.vs[29]["GUID__"] = UUID('e0ed7cb8-17cc-4327-a383-cdbbad4fa88c')
        self.vs[30]["name"] = """true"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('3380fc5a-1126-48b3-b882-72bc4e6d2031')
        self.vs[31]["name"] = """localdefcompstate"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = UUID('267cf8ed-9638-4446-8609-1b9d3fd251b3')
        self.vs[32]["name"] = """procdef"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('890e94de-6272-4d75-aab4-26f64b6d4155')

