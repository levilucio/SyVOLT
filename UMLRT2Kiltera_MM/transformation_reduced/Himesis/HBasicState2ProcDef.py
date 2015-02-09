

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HBasicState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef, self).__init__(name='HBasicState2ProcDef', num_nodes=53, edges=[])
        
        # Add the edges
        self.add_edges([(8, 12), (12, 4), (4, 13), (13, 7), (7, 14), (14, 5), (29, 23), (23, 47), (30, 24), (24, 48), (31, 25), (25, 49), (32, 26), (26, 50), (33, 27), (27, 51), (34, 28), (28, 52), (7, 15), (15, 37), (5, 16), (16, 38), (8, 17), (17, 39), (4, 18), (18, 40), (3, 0), (0, 19), (0, 20), (0, 21), (0, 22), (6, 1), (1, 2), (2, 10), (10, 35), (2, 11), (11, 36), (9, 2), (6, 3), (20, 4), (22, 5), (29, 41), (30, 42), (31, 43), (32, 44), (33, 45), (34, 46), (19, 8), (21, 7), (8, 9), (41, 35), (42, 36), (43, 37), (44, 38), (45, 39), (46, 40)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = UUID('bc8da8f4-6500-4462-ab6c-29a0e49f1222')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('d66e30a9-d745-4680-b687-ee0ffc4916bb')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('5b44394f-ed77-4f93-b163-18cfd7d5b429')
        self.vs[2]["name"] = """state1"""
        self.vs[2]["classtype"] = """State"""
        self.vs[2]["mm__"] = """State"""
        self.vs[2]["cardinality"] = """+"""
        self.vs[2]["GUID__"] = UUID('3012d267-feb9-4748-b74e-e91056b85228')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('f8c54198-b5bd-49d4-a6b3-12727ca55922')
        self.vs[4]["name"] = """listen1"""
        self.vs[4]["classtype"] = """Listen"""
        self.vs[4]["mm__"] = """Listen"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('6a97b30e-a214-474e-a65b-503a8b143618')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('7f232bf7-5a7f-4224-8fa3-1cbdffde0d32')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('43339e57-f2f8-4809-bcd1-309114864f80')
        self.vs[7]["name"] = """listenbranch1"""
        self.vs[7]["classtype"] = """ListenBranch"""
        self.vs[7]["mm__"] = """ListenBranch"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('e0d19d9a-d66f-4768-89fb-9a19bd9004bc')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('088fd105-9105-4ef1-a256-879e34cb8519')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('5120a558-79dd-47de-8842-819a8b768b58')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('8d3ea17a-819f-490b-a938-da50d2290119')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('70191e2b-3a0f-455c-b75b-c9d4ea6a479b')
        self.vs[12]["associationType"] = """p"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('7f9fcaa8-8810-4d14-a5ea-b82c7e37a4c0')
        self.vs[13]["associationType"] = """branches"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = UUID('1b3a7ce9-9914-4ca6-90e1-ee238093fc0d')
        self.vs[14]["associationType"] = """p"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = UUID('dffe0786-06ce-48f2-aacf-66923dd056ea')
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = UUID('51834f92-5a85-4db0-9e85-4e93e1c30b11')
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = UUID('c60c345b-b402-458c-b8f0-700f7377b91a')
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = UUID('e78aa84f-101c-4343-8ff9-4f82905a062b')
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = UUID('42e37b7a-ba7e-46dd-8ae1-923e85b16afe')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('d0e956a8-de28-4156-9a9a-2df798b27cf6')
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = UUID('6672d46a-f947-4382-bb54-5071648b23ba')
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = UUID('0d1452d7-1322-445d-a134-2280aef4bfce')
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = UUID('629b6622-ad47-4bfc-96c0-8ce7570e8be1')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('e8d41b9b-eb54-4d1d-9144-5b8c0b89e0e2')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('b31b7e57-2473-4ec9-99ce-1c8c62ec8457')
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = UUID('b0a7fa7e-318d-4d1b-bd60-7bd91d94d888')
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = UUID('9b85ea2d-a017-4c07-abd0-d65a8d282814')
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = UUID('c4141c56-b907-49d1-a64a-fca6eb60d8da')
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = UUID('58f724c6-4363-4728-81e1-699816c5f975')
        self.vs[29]["name"] = """eq1"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = UUID('24109be7-bd49-4e1f-af95-d6e3ca61c8aa')
        self.vs[30]["name"] = """eq2"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = UUID('e9e8ce4a-373a-4903-8702-bef13e769bb8')
        self.vs[31]["name"] = """eq3"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = UUID('7c0f9dc9-ff1e-41e0-8aaa-ca008508cfdf')
        self.vs[32]["name"] = """eq4"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = UUID('ace37e5d-80ae-43bf-95ce-d97e6a8a089c')
        self.vs[33]["name"] = """eq5"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = UUID('7577802c-4da7-4c07-804b-64eb34a0f85e')
        self.vs[34]["name"] = """eq6"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = UUID('bf7b5530-8570-4cce-9692-72be5eb11cdd')
        self.vs[35]["name"] = """isComposite"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'Bool'"""
        self.vs[35]["GUID__"] = UUID('6c12abeb-a14e-45f7-a8f8-9fffc4d1da7a')
        self.vs[36]["name"] = """hasOutgoingTransitions"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'Bool'"""
        self.vs[36]["GUID__"] = UUID('b63caabd-4ad4-4b8c-8ee2-5fdc635a5d17')
        self.vs[37]["name"] = """channel"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = UUID('64698796-8c81-4112-b484-b3b3cec25b19')
        self.vs[38]["name"] = """channel"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = UUID('5f7d851e-6760-4b03-981b-ab8157a55e79')
        self.vs[39]["name"] = """pivotin"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('ea63e387-4401-4459-92f1-4008239d576f')
        self.vs[40]["name"] = """pivotout"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('112f4f22-32a0-42b1-b3ce-37f41ee596bb')
        self.vs[41]["mm__"] = """leftExpr"""
        self.vs[41]["GUID__"] = UUID('f6c31312-f3e4-4cd2-bedf-1bebe7cf6087')
        self.vs[42]["mm__"] = """leftExpr"""
        self.vs[42]["GUID__"] = UUID('12aa1a99-b7db-473e-b842-0ca4c257a580')
        self.vs[43]["mm__"] = """leftExpr"""
        self.vs[43]["GUID__"] = UUID('9f1172df-f03c-4405-8ac1-0aa0f8933357')
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = UUID('e2e74508-528e-4d9d-9ca0-d80ac7972c1b')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('b487b571-f232-407c-a51a-f7e92bd77380')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('5e5dbafa-dbf6-42f8-a4e6-881f508e6cca')
        self.vs[47]["name"] = """false"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["Type"] = """'Bool'"""
        self.vs[47]["GUID__"] = UUID('3b447b03-1160-4ca3-a688-ac89f25ac52e')
        self.vs[48]["name"] = """true"""
        self.vs[48]["mm__"] = """Constant"""
        self.vs[48]["Type"] = """'Bool'"""
        self.vs[48]["GUID__"] = UUID('a5fff7e5-0bcc-4839-a363-2b0dd2a2b6b7')
        self.vs[49]["name"] = """exit"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = UUID('711fe26a-0550-4135-b08e-b15a4f8762af')
        self.vs[50]["name"] = """exack"""
        self.vs[50]["mm__"] = """Constant"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = UUID('d6684611-ce79-4e4b-9150-1e53bd491e3b')
        self.vs[51]["name"] = """procdef"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = UUID('c005919f-108f-4d54-8e89-1091d9e779fd')
        self.vs[52]["name"] = """listensimplestate"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('c433d296-cc96-431a-be8a-b7561f3f481d')

