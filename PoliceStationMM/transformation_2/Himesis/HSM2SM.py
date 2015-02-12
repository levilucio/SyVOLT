

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM, self).__init__(name='HSM2SM', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 5), (2, 10), (10, 6), (5, 0), (0, 6), (17, 11), (11, 25), (18, 12), (12, 26), (7, 1), (1, 2), (5, 13), (13, 4), (6, 14), (14, 8), (4, 15), (15, 25), (8, 16), (16, 26), (4, 3), (3, 8), (19, 4), (17, 23), (18, 24), (7, 19), (7, 20), (20, 8), (23, 21), (24, 22)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM"""
        self["GUID__"] = UUID('943320ab-4c13-46b2-8659-a916704a6d29')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('44d3df32-82f2-4f0f-8698-e3134c1af385')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('545e4768-3894-42af-b793-63caf3319695')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('1f330a0d-f0da-4589-ae78-a9f3d72a6574')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('97b2343f-4839-4e0d-b4a6-16cdb2d89bf5')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """1"""
        self.vs[4]["mm__"] = """Station_S"""
        self.vs[4]["cardinality"] = """s_"""
        self.vs[4]["GUID__"] = UUID('075db98b-8a3a-40bc-b785-c90c40971459')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('baa2cd0c-b582-43b8-b0c3-567a1ab57eba')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Male_T"""
        self.vs[6]["GUID__"] = UUID('c8fafdf0-d5fb-4765-aa5e-6508a497e12a')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('a187d581-1f93-49fa-8246-8e3cdcabfbe1')
        self.vs[8]["name"] = """s_"""
        self.vs[8]["classtype"] = """1"""
        self.vs[8]["mm__"] = """Male_S"""
        self.vs[8]["cardinality"] = """s_"""
        self.vs[8]["GUID__"] = UUID('48a5f62f-d281-463a-9eb4-22a63c60b522')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('090103b0-7c26-4369-b68b-8dc117f2cdd5')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('4188cbb4-c101-448f-9be5-de78e62207b3')
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = UUID('48a84666-951d-4461-9ecb-674340a06556')
        self.vs[12]["mm__"] = """leftExpr"""
        self.vs[12]["GUID__"] = UUID('7ed9306b-e495-400c-bee0-f15a2aca6e53')
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["GUID__"] = UUID('f8b336bd-7977-4dc5-a30b-81946e3ae4f9')
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('f5e8ad89-6a7f-4b6b-8ea9-79bb9a5fb3eb')
        self.vs[15]["mm__"] = """hasAttribute_S"""
        self.vs[15]["GUID__"] = UUID('77a5a352-c428-4989-8104-21933dc4a19b')
        self.vs[16]["mm__"] = """hasAttribute_S"""
        self.vs[16]["GUID__"] = UUID('7b011782-412d-4b40-8b9b-9d6a8b650bd0')
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('489358bd-b1e1-4e95-969e-4e9e0c701560')
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('da28abfb-07c6-4621-87cd-a15154b122cc')
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = UUID('a7a19687-d1ae-4cef-9abc-96c8b64b56ad')
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = UUID('867d18d4-48c0-4918-84d2-8db502c91d52')
        self.vs[21]["name"] = """somestation"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["GUID__"] = UUID('ae91b2ec-ed09-418a-a477-6dcaab1b4095')
        self.vs[22]["name"] = """somemale"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["GUID__"] = UUID('9cb6452e-4344-42f5-ab79-26fe23be9f44')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('7723eee2-522b-4075-add4-e72267796f1e')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('578ea478-0d72-426c-843e-9a6374153f4a')
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["GUID__"] = UUID('0bad9196-69f1-4060-b55a-f977b2d8957c')
        self.vs[26]["name"] = """name"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = UUID('eab57f06-6f79-4389-b95f-4519a767ffd7')

