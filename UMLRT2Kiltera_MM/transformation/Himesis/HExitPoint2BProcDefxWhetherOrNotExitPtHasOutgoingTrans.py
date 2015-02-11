

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans, self).__init__(name='HExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans', num_nodes=64, edges=[])
        
        # Add the edges
        self.add_edges([(3, 0), (0, 10), (2, 19), (19, 7), (7, 20), (20, 12), (7, 21), (21, 9), (9, 22), (22, 5), (39, 33), (33, 51), (40, 34), (34, 8), (41, 35), (35, 53), (42, 36), (36, 54), (43, 37), (37, 55), (44, 38), (38, 56), (7, 23), (23, 59), (12, 24), (24, 60), (5, 25), (25, 61), (2, 26), (26, 62), (9, 27), (27, 63), (4, 1), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (8, 13), (13, 52), (8, 14), (14, 58), (28, 2), (2, 11), (6, 15), (15, 3), (6, 16), (16, 10), (3, 17), (17, 57), (10, 18), (18, 58), (11, 3), (6, 4), (32, 5), (39, 45), (40, 46), (41, 47), (42, 48), (43, 49), (44, 50), (29, 7), (30, 12), (31, 9), (45, 57), (46, 59), (47, 60), (48, 61), (49, 62), (50, 63)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ExitPoint2BProcDefxWhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = UUID('f775437b-9714-4563-9735-a3facead688f')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """exitPoints"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('062cc345-5a2f-481d-8bb4-bca1f681b0d7')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('efa8e354-e419-4cd3-9a7c-e43e4272bd67')
        self.vs[2]["name"] = """localdef1"""
        self.vs[2]["classtype"] = """LocalDef"""
        self.vs[2]["mm__"] = """LocalDef"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('91ed3e85-fd1a-4a84-817d-10d1dc5f8b5b')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('ffe0975c-0b04-4209-9c24-2d3fedc1d8e3')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('ad24c5b6-d4c2-466f-960b-3819b30424ec')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('4e78170e-92e6-4087-aac8-b8d1bf119e2e')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('8b82584b-395a-46a8-929f-9905a1a2f28d')
        self.vs[7]["name"] = """procdef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('748fddb4-7a84-43af-a2e7-afabfc17a206')
        self.vs[8]["name"] = """concat1"""
        self.vs[8]["mm__"] = """Concat"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = UUID('4fce982f-b449-46c1-90aa-eb18452e8f9a')
        self.vs[9]["name"] = """par1"""
        self.vs[9]["classtype"] = """Par"""
        self.vs[9]["mm__"] = """Par"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('30756ef7-b9d6-462d-a72b-36fb70e3d544')
        self.vs[10]["name"] = """exitpoint1"""
        self.vs[10]["classtype"] = """ExitPoint"""
        self.vs[10]["mm__"] = """ExitPoint"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = UUID('5ce1f6e4-531c-47b6-8060-e9684a574d15')
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('7127bb34-820a-4836-9360-1f0ae0f31bd2')
        self.vs[12]["name"] = """name1"""
        self.vs[12]["classtype"] = """Name"""
        self.vs[12]["mm__"] = """Name"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = UUID('b087d5fb-a6b8-472a-b175-e89bfc489343')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('b4da35ec-16b4-4836-847f-61d8f2239df6')
        self.vs[14]["mm__"] = """hasArgs"""
        self.vs[14]["GUID__"] = UUID('0938c0cc-abf5-4904-8366-186fef6308e5')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('b963c5a1-da50-4806-ab22-604d1ecc2507')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('2c0144b9-36da-46b3-91c5-d2dd179ea2be')
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = UUID('0b1b40ee-dc72-4526-9a1d-39ec4526e2f4')
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = UUID('a36c082b-a105-42ad-b695-b7a6dfd6a0c1')
        self.vs[19]["associationType"] = """def"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('5221deb8-db6e-46a0-b155-4da990f04d9a')
        self.vs[20]["associationType"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('1167ec5e-0e26-4133-804d-2b15d8dd35c0')
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('7355bb04-8ae2-4218-a480-929a3bda504a')
        self.vs[22]["associationType"] = """p"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = UUID('58a3a00a-7e0c-4544-8f78-5f02443c4baf')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('f79c7dbd-b45c-4cd3-9fcf-5e13f93a0858')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('ddf645b1-f75f-4213-8637-c1418cc10c0b')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('1fdbcb64-0ed7-47dd-aa78-691335fe8af9')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('f807d088-5c9a-48e1-bbdf-ee22ee2e97eb')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('830aba40-ae1d-47f4-a87b-1f27ffae867f')
        self.vs[28]["mm__"] = """apply_contains"""
        self.vs[28]["GUID__"] = UUID('10740e24-1840-4836-9610-770a564dc0ee')
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = UUID('99140ac5-01a6-4ae4-a4f9-3ce2315b047e')
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = UUID('8cfacca0-e28d-409b-82ce-aac356676bc9')
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = UUID('177c23e0-67a5-4bf0-98d8-889a267a9e98')
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = UUID('5fb47b29-1df4-4ca3-8a02-3179ca25ef88')
        self.vs[33]["mm__"] = """rightExpr"""
        self.vs[33]["GUID__"] = UUID('c75108e2-e330-4fc3-9149-365d2dc322e0')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('49ac97d7-4f4a-4257-a2f4-ee34a57095de')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('efd49ae5-3000-4267-8af4-defe99e6c08c')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('da50647b-5d15-47de-a7a7-92b8ddde4af3')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('2455348e-915b-4bae-82e6-8be89c1d8bb3')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('08c5f5a5-3a39-4ea9-acd7-9683ad065ce7')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('e02b84de-6ae0-4f03-ad15-54dc5a2563e9')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('1aaed270-b725-4f6d-a859-3a8a39f25bbd')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('6e6b7c38-0c28-4cbc-aa4e-d8ade512eeef')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('1ec6f0a1-bf36-46db-9b63-df3e1c13e985')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('ffac5dfa-e1ec-43ce-bc71-a580ab4d9c78')
        self.vs[44]["name"] = """eq6"""
        self.vs[44]["mm__"] = """Equation"""
        self.vs[44]["GUID__"] = UUID('88b8f7b0-b129-40aa-8d00-7d775510ba5c')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('de550952-1e27-4f4f-8464-43dabef31328')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('5767e67c-d5ed-4fd2-804b-526122b8d71d')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('1bc7c4f2-0d84-4521-925f-2269a7ef94ad')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('188af5bb-95d5-44d3-a337-fe8f46292744')
        self.vs[49]["mm__"] = """leftExpr"""
        self.vs[49]["GUID__"] = UUID('0388510d-e3e1-4a7e-af96-22a942c4eef9')
        self.vs[50]["mm__"] = """leftExpr"""
        self.vs[50]["GUID__"] = UUID('2cfaa352-d051-4219-adc4-392d937556a1')
        self.vs[51]["name"] = """true"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'Bool'"""
        self.vs[51]["GUID__"] = UUID('bd792650-c5bd-411e-9762-7f6c56a16fb6')
        self.vs[52]["name"] = """B"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('12b85692-9e7f-49dd-8ddc-54ab269168da')
        self.vs[53]["name"] = """sh_in"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('59f33540-e39f-4917-86a0-cbee9ee4ae9c')
        self.vs[54]["name"] = """sh_in"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('4a9d7941-3779-4530-9e48-a8f18b9cc8dd')
        self.vs[55]["name"] = """localdefcompstate"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('38eb1a45-6232-4cd5-a518-0084cda3283e')
        self.vs[56]["name"] = """parexitpoint"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('390f5edf-97d0-45f9-ab88-61bafae611bc')
        self.vs[57]["name"] = """isComposite"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'Bool'"""
        self.vs[57]["GUID__"] = UUID('818eeb1e-0814-4918-9027-fcb2adcdf020')
        self.vs[58]["name"] = """name"""
        self.vs[58]["mm__"] = """Attribute"""
        self.vs[58]["Type"] = """'String'"""
        self.vs[58]["GUID__"] = UUID('4737da06-5eba-45dc-992b-ee7f6c75d291')
        self.vs[59]["name"] = """name"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        self.vs[59]["GUID__"] = UUID('81a44f8d-cd78-4dfc-a999-402f32f0d24f')
        self.vs[60]["name"] = """literal"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        self.vs[60]["GUID__"] = UUID('f6d6cd8d-886e-4ac5-a6c8-a4a15b2c0558')
        self.vs[61]["name"] = """channel"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('1e016965-7ddd-4858-835f-661c4f085564')
        self.vs[62]["name"] = """pivot"""
        self.vs[62]["mm__"] = """Attribute"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('fab7a0cd-0524-446c-8016-139ab703b8a3')
        self.vs[63]["name"] = """pivot"""
        self.vs[63]["mm__"] = """Attribute"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('3e509c9f-5ec1-4f68-b821-478c88a53102')

