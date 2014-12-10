

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
        self["GUID__"] = UUID('8f0cd1e2-c075-44ef-bd83-56fe394e6ee6')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('589388b4-46a1-4207-b0bd-1b7b113be41e')
        self.vs[1]["name"] = """state1"""
        self.vs[1]["classtype"] = """State"""
        self.vs[1]["mm__"] = """State"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('076c0631-5e31-4216-bb12-4c9f6b37204d')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('bfcb9e84-b87d-43bc-969e-62a05fc386d8')
        self.vs[3]["name"] = """listen1"""
        self.vs[3]["classtype"] = """Listen"""
        self.vs[3]["mm__"] = """Listen"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('3195ecd8-5704-4f51-ac96-2dd9d9b0be93')
        self.vs[4]["name"] = """triggerS1"""
        self.vs[4]["classtype"] = """Trigger_S"""
        self.vs[4]["mm__"] = """Trigger_S"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('597cf61d-85da-46ff-8c03-350e71f127ea')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('623ab613-20f4-4d0a-8bac-f335112147b1')
        self.vs[6]["name"] = """listenBranch1"""
        self.vs[6]["classtype"] = """ListenBranch"""
        self.vs[6]["mm__"] = """ListenBranch"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('f34a31be-f118-4b03-9587-e66f7e9101fc')
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('0d3fd4ab-7844-4eff-9041-158e884e5752')
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('cff5d8d9-406b-4abb-9c57-fbf41cfbfbda')
        self.vs[9]["name"] = """signal1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('b8c3bab1-769b-4ef1-88bd-9682500fcac9')
        self.vs[10]["associationType"] = """branches"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('fd401b19-5637-4e84-ab8c-eadcc345fc45')
        self.vs[11]["associationType"] = """p"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('7d5a8bb6-f268-4676-b1fa-2efb09f21931')
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('fee62636-680d-495b-a808-6d560a03bd63')
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["GUID__"] = UUID('8b4cf789-36e4-442c-b3c0-2cb4fe6e033b')
        self.vs[14]["associationType"] = """outgoingTransitions"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('ccd10de8-7aa1-4379-99f9-cee1d619c581')
        self.vs[15]["associationType"] = """triggers"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('f7b319f0-fd17-4c29-9613-786482b54ff0')
        self.vs[16]["associationType"] = """signal"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('5b5f24fc-c201-4a77-af10-445eaff6d083')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('3ace3ac2-a2ff-4f95-b026-0caec96a56f9')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('b9e83216-e46d-47b3-a153-68b95dbb1c0a')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('6c0923b0-36f7-4213-8681-e37b9788d08e')
        self.vs[20]["mm__"] = """hasAttribute_S"""
        self.vs[20]["GUID__"] = UUID('897d7f70-a39d-44b8-ab47-d100b29adefc')
        self.vs[21]["mm__"] = """hasAttribute_S"""
        self.vs[21]["GUID__"] = UUID('f9175c87-85bb-4785-8c55-9f8b7e33988b')
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = UUID('17fe7551-1e4a-4806-abad-5b1b6e905a4c')
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = UUID('635d45e8-99b4-4652-a5e3-16b9355d864b')
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = UUID('0b749878-7dbc-495c-a3a9-3a188437802a')
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = UUID('872581b1-c07d-48fc-a84f-9ebd539c3fc1')
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = UUID('6cdf59ef-527a-4cf6-90df-55529886ec09')
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = UUID('727bf0d2-bbed-416b-be28-7fd3b7d93890')
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = UUID('870bb557-3001-4d15-bad6-8de9235d563d')
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = UUID('37312f6f-b18f-4393-a94d-73d2379ce75c')
        self.vs[30]["name"] = """false"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["GUID__"] = UUID('72c0a74a-989f-4863-8489-a38c0029f309')
        self.vs[31]["name"] = """true"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'Bool'"""
        self.vs[31]["GUID__"] = UUID('8a603bd8-41be-4f24-93b8-c5ed1b7d721d')
        self.vs[32]["name"] = """listensimplestate"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = UUID('227cc54b-cd6e-4255-a871-49e6fbd98d6a')
        self.vs[33]["name"] = """instfortrans"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = UUID('4a9e6e0e-2ace-459a-a131-9fc5e25123ca')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('cada06a6-43ef-412b-9e14-f7af24d2ed75')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('804a57b4-3d3c-4da3-bf97-f3b017bed164')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('4159a02c-316e-440b-ae69-9a6af97f21f5')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('754ee7af-daec-42cd-8016-5c7505f0bf9c')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('77d4a8d9-07a9-4ff8-921d-4f5ee8778730')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('fbbcdfad-067d-491c-8e13-e3f0cae513f9')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('96065f72-de7b-417d-9fb3-dc269e76151a')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('da184158-2d3c-4f1a-96e9-52f84ae5c940')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('297bc960-05a6-4daf-9e53-c06971ef59ff')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('5bf9ac88-ad86-4510-a924-41e59d0e3aba')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('e6726c0b-e89d-4b44-9d6d-9c9584699549')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('a66168b8-bce7-4249-9b69-7be0a11eadac')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('7832435c-3a26-47e9-846b-da835c28a2aa')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('07538a07-a578-4300-934c-b29d8f2b164d')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('df095513-1924-4c52-8e11-4601f38f337d')
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = UUID('9a67994d-8426-4120-b7a6-e819d7f17df4')
        self.vs[50]["name"] = """hasOutgoingTransitions"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'Bool'"""
        self.vs[50]["GUID__"] = UUID('416fbf23-7add-4111-be06-461ca16b57b2')
        self.vs[51]["name"] = """name"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('022deee4-0406-4714-97dd-5953e06e2747')
        self.vs[52]["name"] = """channel"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('be8c1d60-8379-4632-8dda-22596ffe42a1')
        self.vs[53]["name"] = """pivotin"""
        self.vs[53]["mm__"] = """Attribute"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('2d0f64b2-bc69-4f89-99a1-d997a85c3ecc')
        self.vs[54]["name"] = """pivotin"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('6a08bc5d-d0f6-40f9-ab24-63b33565479e')

