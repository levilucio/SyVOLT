

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, self).__init__(name='HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans', num_nodes=64, edges=[])
        
        # Add the edges
        self.add_edges([(3, 0), (0, 10), (2, 19), (19, 7), (7, 20), (20, 12), (7, 21), (21, 9), (9, 22), (22, 5), (39, 33), (33, 51), (40, 34), (34, 8), (41, 35), (35, 53), (42, 36), (36, 54), (43, 37), (37, 55), (44, 38), (38, 56), (7, 23), (23, 59), (12, 24), (24, 60), (5, 25), (25, 61), (2, 26), (26, 62), (9, 27), (27, 63), (4, 1), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (8, 13), (13, 52), (8, 14), (14, 58), (28, 2), (2, 11), (6, 15), (15, 3), (6, 16), (16, 10), (3, 17), (17, 57), (10, 18), (18, 58), (11, 3), (6, 4), (32, 5), (39, 45), (40, 46), (41, 47), (42, 48), (43, 49), (44, 50), (29, 7), (30, 12), (31, 9), (45, 57), (46, 59), (47, 60), (48, 61), (49, 62), (50, 63)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = UUID('1183d5ee-c357-4119-8219-2e753a67efac')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """exitPoints"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('178dd6db-65cb-41a2-8ddb-d76300cc3c9a')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('2d3701f7-1de2-4a9b-9e9f-1fa12ee39a15')
        self.vs[2]["name"] = """localdef1"""
        self.vs[2]["classtype"] = """LocalDef"""
        self.vs[2]["mm__"] = """LocalDef"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('201aa44d-31b2-4134-861b-14fe9bb34e26')
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = UUID('efd74ade-6037-4638-bd4a-de435dbe54c4')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('7a63fc9a-9309-481e-a1ab-628212797861')
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('3d7eba1d-adaa-4968-bc48-eabad05ec6c9')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('1835505e-54fe-41bb-afc7-96c16500fd25')
        self.vs[7]["name"] = """procdef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('5e9bf28f-d761-44e7-a656-62dfc73f486f')
        self.vs[8]["name"] = """concat1"""
        self.vs[8]["mm__"] = """Concat"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = UUID('e60ca335-e483-4437-8412-18a412905253')
        self.vs[9]["name"] = """par1"""
        self.vs[9]["classtype"] = """Par"""
        self.vs[9]["mm__"] = """Par"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('5e0c244f-3db3-4c75-a7aa-d564224a59bd')
        self.vs[10]["name"] = """exitpoint1"""
        self.vs[10]["classtype"] = """ExitPoint"""
        self.vs[10]["mm__"] = """ExitPoint"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = UUID('9990bcd6-06fd-4300-911b-c0e5e2a0f557')
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('f13854ac-a020-4a4d-871c-dc4ff41a39cd')
        self.vs[12]["name"] = """name1"""
        self.vs[12]["classtype"] = """Name"""
        self.vs[12]["mm__"] = """Name"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = UUID('ac13fe6a-6123-457e-b365-3f356ec2bf0b')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('6e1e4eb4-8d77-4af2-8e25-9cd0eb5060b5')
        self.vs[14]["mm__"] = """hasArgs"""
        self.vs[14]["GUID__"] = UUID('2239827d-f1a5-4473-849a-b4f56d05b63f')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('b2b131cf-c664-430e-aeba-b3244487c6c6')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('ebfc487e-7ce3-4082-a681-0e3286e1f510')
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = UUID('5e990411-f302-49df-8fe5-75288db1b610')
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = UUID('ec4a28de-d190-459d-880c-11beb6c065ef')
        self.vs[19]["associationType"] = """def"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('31be52e4-1e6b-4e6a-a6f4-3ad733964d61')
        self.vs[20]["associationType"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('ffd917f1-fe1d-468a-943e-ce9387c3e1c0')
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('03963299-5560-4bba-ba71-081bf57a4827')
        self.vs[22]["associationType"] = """p"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = UUID('b2aeb2dc-c426-4960-bbe0-7733c3cfbe35')
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = UUID('a337b9bc-a0ba-441b-9840-fe3d533efe8c')
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = UUID('b051b6e2-5c03-4e55-a2ea-5586f02e1a82')
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = UUID('a450989d-4506-4941-a766-40d6f3ba545a')
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = UUID('3db00686-02d1-4a98-9118-b001a4ca675c')
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = UUID('f13560bf-9883-4948-90b5-f2b523df45d8')
        self.vs[28]["mm__"] = """apply_contains"""
        self.vs[28]["GUID__"] = UUID('ef05773b-b7b4-4ce5-afca-db96d714bb8f')
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = UUID('b57f9f2b-cee5-4fdc-90b2-5b023a640193')
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = UUID('99f4fb18-36c3-4db1-9468-37bbb3760ffe')
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = UUID('1792e38e-5733-4b39-98df-45fa76cdce52')
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = UUID('996425ec-e4bc-4752-8239-8e71ed0bb9b2')
        self.vs[33]["mm__"] = """rightExpr"""
        self.vs[33]["GUID__"] = UUID('4c95e20c-f99d-498c-a3dc-123e9a0aea94')
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = UUID('d343cc6b-e2cc-44ee-a255-c900511d2b26')
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = UUID('bc182aba-3f3a-475c-ac92-1fc8fdb8a353')
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = UUID('7999fbdc-21ad-4d87-9f39-cd330444c3af')
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = UUID('a9f0f38f-6c94-41fb-a9bc-e9b8c5f69e4b')
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = UUID('0cc20b97-a476-4c03-b160-71df2b56c054')
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = UUID('7819f088-2be0-4123-a985-35617370f148')
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = UUID('40ee8765-0f88-4036-8708-232ff8b2c8cd')
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = UUID('796b5027-ee2a-4543-919b-8dc77cb083dc')
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = UUID('318989a8-4191-483c-a3ab-d47925923a35')
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = UUID('a76f034a-7a66-48ab-96cf-e679592051fc')
        self.vs[44]["name"] = """eq6"""
        self.vs[44]["mm__"] = """Equation"""
        self.vs[44]["GUID__"] = UUID('b6e459b6-de34-44ec-94d1-78c3b82b9b55')
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = UUID('ec133653-a79d-419e-9c58-248e8ae585ee')
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = UUID('1c85c190-6222-4b5e-8176-7fda4ad13a48')
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = UUID('c6505416-ee64-4b82-8a87-8b269d1197f9')
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = UUID('eb3e7aaf-fa26-48cf-9306-002b449fb58c')
        self.vs[49]["mm__"] = """leftExpr"""
        self.vs[49]["GUID__"] = UUID('e80f429c-ff6f-41fb-8171-dbad28d4a1c0')
        self.vs[50]["mm__"] = """leftExpr"""
        self.vs[50]["GUID__"] = UUID('ba9401c5-0e80-4417-90c1-5b4152573f1f')
        self.vs[51]["name"] = """true"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'Bool'"""
        self.vs[51]["GUID__"] = UUID('513d8641-37e8-40af-b9f8-5e006b5ec6b4')
        self.vs[52]["name"] = """B"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = UUID('c357e0cc-de98-4910-9079-5860ffb86bd9')
        self.vs[53]["name"] = """sh_in"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = UUID('72293817-40bf-408a-b81b-5e7ed1dc822a')
        self.vs[54]["name"] = """sh_in"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = UUID('02afb59c-a14c-4d40-82c1-341542977da5')
        self.vs[55]["name"] = """localdefcompstate"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = UUID('e5bc6e7f-62ea-408e-a9d9-a146c6bbb1e9')
        self.vs[56]["name"] = """parexitpoint"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = UUID('7d2d52cb-6943-44f3-9df2-72ad7ae0606e')
        self.vs[57]["name"] = """isComposite"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'Bool'"""
        self.vs[57]["GUID__"] = UUID('71815e93-4b43-4684-a380-04e99d660131')
        self.vs[58]["name"] = """name"""
        self.vs[58]["mm__"] = """Attribute"""
        self.vs[58]["Type"] = """'String'"""
        self.vs[58]["GUID__"] = UUID('01572dbf-4922-4286-9f1c-5bf0e1337f61')
        self.vs[59]["name"] = """name"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        self.vs[59]["GUID__"] = UUID('39c6321c-da19-414e-93fe-6816d2d1f87e')
        self.vs[60]["name"] = """literal"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        self.vs[60]["GUID__"] = UUID('5bd92f89-3d9d-40b1-9c89-48ea732f9808')
        self.vs[61]["name"] = """channel"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        self.vs[61]["GUID__"] = UUID('6baf6d61-c721-48de-9b49-62a2c238c1e0')
        self.vs[62]["name"] = """pivotin"""
        self.vs[62]["mm__"] = """Attribute"""
        self.vs[62]["Type"] = """'String'"""
        self.vs[62]["GUID__"] = UUID('3528042d-05fb-4a35-99ef-d1d0cd689d4f')
        self.vs[63]["name"] = """pivotout"""
        self.vs[63]["mm__"] = """Attribute"""
        self.vs[63]["Type"] = """'String'"""
        self.vs[63]["GUID__"] = UUID('88f528da-6c52-4086-8a8e-d1974eebbec5')

