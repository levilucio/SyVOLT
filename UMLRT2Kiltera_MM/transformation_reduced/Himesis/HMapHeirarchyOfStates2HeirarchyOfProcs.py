

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
        self["GUID__"] = UUID('56e78226-f446-4bec-bdee-a2523b966cf7')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """states"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('7356524a-0360-4daf-83cd-a3a875b3627e')
        self.vs[1]["associationType"] = """def"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('583e3d2d-a203-4c81-97d1-cfea6e1964a5')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('9a42ee1f-b1cd-405a-961c-e0635ec5d0e8')
        self.vs[3]["name"] = """localDef1"""
        self.vs[3]["classtype"] = """LocalDef"""
        self.vs[3]["mm__"] = """LocalDef"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('1674f5ec-a7ec-4516-b94c-6a1887e080c0')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('314ffb20-4e59-4b3d-9788-a6c9063ee1c8')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('ade5c6a2-4a73-4d2e-bca0-008641b22a31')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('6ed0edd0-359b-4979-8f19-240d5c0e5d71')
        self.vs[7]["name"] = """procDef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('4954c571-bf25-4726-89b9-9bc96164391c')
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = UUID('d237e24f-0934-4553-a323-31a1e5e601f7')
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = UUID('0d82cc6b-352d-4937-a711-5420bcbc74f7')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('5d3e3f22-d87e-48ae-9765-2db01d90a5de')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('f91a083a-45f1-449f-9f9f-15d2d2cc43ec')
        self.vs[12]["name"] = """state1"""
        self.vs[12]["classtype"] = """State"""
        self.vs[12]["mm__"] = """State"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('c35a9732-e27f-4686-b67a-eced550b0a2c')
        self.vs[13]["name"] = """state2"""
        self.vs[13]["classtype"] = """State"""
        self.vs[13]["mm__"] = """State"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('27d062e5-5feb-4bac-94b7-675bfc6f9ff9')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('f15edd06-cefb-4763-870b-7ae0047b3c98')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('0f6531d5-aa21-49a7-bdce-56abcdc9de12')
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["GUID__"] = UUID('bd47d646-ba94-4d76-915f-94dbf834d6cd')
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["GUID__"] = UUID('b42fe6f2-7c9c-408f-9adc-5d9fdc2a0c25')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('6805eff3-5818-4ee4-83b3-a0037f952cad')
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = UUID('46b7e370-fed4-4c0c-8324-739b85a1b1f0')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('7de4fe1c-52e8-4347-a155-fc415ea273b5')
        self.vs[21]["name"] = """eq1"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = UUID('94dc4157-28d5-4137-b8c8-e0ef52ae00ea')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('b0422a90-a511-4510-825b-19d0b70dd733')
        self.vs[23]["name"] = """eq3"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('c510e81d-097a-45ff-b644-6b8395dcd2d2')
        self.vs[24]["name"] = """isComposite"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'Bool'"""
        self.vs[24]["GUID__"] = UUID('c4659d16-754f-4eaf-b428-d54345657080')
        self.vs[25]["name"] = """pivot"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('54daa7cc-c08b-48d5-b15e-cced6b9e22c1')
        self.vs[26]["name"] = """pivot"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('44bff4cc-392f-45f2-bb21-b477846af26e')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('a7615469-83d1-48f3-a08d-3916c76a8714')
        self.vs[28]["mm__"] = """leftExpr"""
        self.vs[28]["GUID__"] = UUID('27d83df4-d900-4b52-9f55-b7e6695acd24')
        self.vs[29]["mm__"] = """leftExpr"""
        self.vs[29]["GUID__"] = UUID('f06f185c-3884-4014-b22f-8aa5410d576a')
        self.vs[30]["name"] = """true"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('526e352d-e816-47f9-bf9a-cc21a388c09c')
        self.vs[31]["name"] = """localdefcompstate"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = UUID('8b7c7f1d-8199-497f-a8b4-b8db86d818df')
        self.vs[32]["name"] = """procdef"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('e30853f7-64ed-4922-a5e7-b0e3c78d690a')

