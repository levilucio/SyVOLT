

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
        self["GUID__"] = UUID('9518db9e-0c6a-44dd-9629-6b33987c9574')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """states"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('90ad04cb-4d0a-4002-82e9-34e0a1f5c31e')
        self.vs[1]["associationType"] = """def"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('906c5041-3bd7-4869-a1bf-843000045802')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('491f388e-8b7c-4c95-a7cd-303d94f17ff9')
        self.vs[3]["name"] = """localDef1"""
        self.vs[3]["classtype"] = """LocalDef"""
        self.vs[3]["mm__"] = """LocalDef"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('3d7bce4e-dc1d-47bb-a58a-f7dbdb022012')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('42eae13d-04aa-4b59-af50-cab8988be1b2')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('56701428-2cd7-4cba-8c5e-3ce7d69d4f54')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('6350ddee-9661-4974-923f-de9a76a937a6')
        self.vs[7]["name"] = """procDef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('f0e658bc-b79c-441e-81ff-990f29b564d0')
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = UUID('484deb43-6b44-47f4-9fa2-c311f7501d87')
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = UUID('402bc0d2-dc94-465d-9128-f3e487db1939')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('d0e21c20-2720-43e5-a4bd-49beb6935d80')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('2065248d-d30d-4bc5-b0ab-58a3e866883c')
        self.vs[12]["name"] = """state1"""
        self.vs[12]["classtype"] = """State"""
        self.vs[12]["mm__"] = """State"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('e75d916a-c8af-48df-a14c-05c0c0f39f1b')
        self.vs[13]["name"] = """state2"""
        self.vs[13]["classtype"] = """State"""
        self.vs[13]["mm__"] = """State"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('591b651f-5318-4e8f-af88-37556c3da4b9')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('2dee64cd-4dc1-42ef-be45-726a197e64fc')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('549124ed-dcc7-4721-8406-1e303c41219d')
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["GUID__"] = UUID('16f3573b-cde0-4d6d-a148-6f791f4709cd')
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["GUID__"] = UUID('fbf4ca08-2618-4244-afbd-e5eb2b098d40')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('989400c6-3e80-42a6-be00-6844f02d2699')
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = UUID('35e26b3b-9291-462c-a9ab-d887b45395b0')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('6de26094-2a57-4de5-8597-041915fb5a9d')
        self.vs[21]["name"] = """eq1"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = UUID('37b29ffb-d183-4d09-ad87-6f1185d47216')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('898b9ba9-6f70-41d8-8cbd-19c14e290f21')
        self.vs[23]["name"] = """eq3"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('d16d5d09-6c3a-499c-bb62-bfce84a40ccb')
        self.vs[24]["name"] = """isComposite"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'Bool'"""
        self.vs[24]["GUID__"] = UUID('819ad71b-5dc4-428b-bccd-d69c23d24ef5')
        self.vs[25]["name"] = """pivotin"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('ec02af56-9fce-45a2-b77c-8c663b5f8b33')
        self.vs[26]["name"] = """pivotin"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('9205692e-c23a-45f3-bb5f-ba913b38cec5')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('47d19582-71af-42c0-80b8-6ccf3d9ecd23')
        self.vs[28]["mm__"] = """leftExpr"""
        self.vs[28]["GUID__"] = UUID('192c8593-9e0a-4f3a-ac73-4e2ecf06a767')
        self.vs[29]["mm__"] = """leftExpr"""
        self.vs[29]["GUID__"] = UUID('d1525302-59ec-4b8e-932b-86919847a41f')
        self.vs[30]["name"] = """true"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('ca391702-302c-416b-b473-d0223b86129c')
        self.vs[31]["name"] = """localdefcompstate"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = UUID('2c56621a-33cd-4c30-9c90-b64e175cb84f')
        self.vs[32]["name"] = """procdef"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('0afe1740-02da-4782-9ad1-8c44c1a5a038')

