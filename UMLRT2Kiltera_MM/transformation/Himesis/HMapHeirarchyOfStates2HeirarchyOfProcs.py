

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
        self["GUID__"] = UUID('25702ab9-0726-45de-9ad4-865b0077c48d')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """states"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('41cc4975-067f-4ea0-9e00-c639d9c1e1c5')
        self.vs[1]["associationType"] = """def"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = UUID('10b91aa6-ac6d-4e38-ae69-f3cbbb0871e3')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('ce48949a-8bcf-44a6-a75d-cde60cbac0b8')
        self.vs[3]["name"] = """localDef1"""
        self.vs[3]["classtype"] = """LocalDef"""
        self.vs[3]["mm__"] = """LocalDef"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('dbfe88d3-fc02-4377-945b-c75881b94a14')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('a60c90d3-8e43-46ff-bbd0-5d7aeecf8999')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('85eb959b-df8e-4b33-8aea-c90d4e6383d5')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('cff6f655-28a4-43e7-a99e-e39e740c3ffa')
        self.vs[7]["name"] = """procDef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('cb927528-0e3b-4e21-b3f1-6d93e3536dbc')
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = UUID('bf1e3f49-f8f5-481e-b345-4c5a931f863f')
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = UUID('892129e9-e8b8-4f15-a25c-381784312bcf')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('93d1006c-9f66-4ca7-9c36-2dc39b57b15e')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('c5f2536e-6b6f-4481-a9b2-bcde3987e3d3')
        self.vs[12]["name"] = """state1"""
        self.vs[12]["classtype"] = """State"""
        self.vs[12]["mm__"] = """State"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('74fe7282-898c-4cd8-9e96-b9befef30ebc')
        self.vs[13]["name"] = """state2"""
        self.vs[13]["classtype"] = """State"""
        self.vs[13]["mm__"] = """State"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('5a1a144e-df65-4676-82a1-b50d7215c8fd')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('baa2ed1c-c160-4621-9b44-ee8315ed06d6')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('16ed6fd8-d1d6-4f82-82c6-1bcf4b68065f')
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["GUID__"] = UUID('2e037b1b-71b4-474c-956c-0c4e5c7a823f')
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["GUID__"] = UUID('bc30c9ea-7c6c-4959-aa78-d6ad6fba524d')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('471719a8-7e72-464b-9539-513004c7166e')
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = UUID('38563595-2b15-4099-9ed8-ac1cb0c1e0d1')
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = UUID('48c08400-ea1b-45cb-86d6-61d2bb583eee')
        self.vs[21]["name"] = """eq1"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = UUID('0a354b55-b057-4914-9ac4-dd27dd5c65da')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('892a55e8-a674-4844-8da9-c70613b791f6')
        self.vs[23]["name"] = """eq3"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('881cca3e-f7db-4f14-b123-89767612ba3b')
        self.vs[24]["name"] = """isComposite"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'Bool'"""
        self.vs[24]["GUID__"] = UUID('732d2fc8-d1bc-442b-9692-f12070f3f07c')
        self.vs[25]["name"] = """pivot"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = UUID('ff265d55-bbed-4776-9354-d46a0e85e131')
        self.vs[26]["name"] = """pivot"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = UUID('201b398d-85f4-4b3d-b1e6-e47a99297323')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('767b34b5-41ac-4eb6-bf4b-d86bf42df3bf')
        self.vs[28]["mm__"] = """leftExpr"""
        self.vs[28]["GUID__"] = UUID('837dda85-1945-4c11-99b0-89187cf3558e')
        self.vs[29]["mm__"] = """leftExpr"""
        self.vs[29]["GUID__"] = UUID('d40feba2-b89c-45eb-9f8b-9430bdf7006e')
        self.vs[30]["name"] = """true"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('faec53a1-5dc3-4461-a19f-1659d343ec72')
        self.vs[31]["name"] = """localdefcompstate"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = UUID('9bbfe8cd-b6ad-45ad-84af-0e0e6c548d39')
        self.vs[32]["name"] = """procdef"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('df340e28-0682-492c-bc6f-8526b80e758e')

