

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HTransition2Inst(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2Inst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2Inst, self).__init__(name='HTransition2Inst', num_nodes=85, edges=[])
        
        # Add the edges
        self.add_edges([(2, 14), (14, 7), (7, 15), (15, 8), (7, 16), (16, 1), (8, 17), (17, 5), (6, 18), (18, 22), (6, 19), (19, 23), (6, 20), (20, 24), (6, 21), (21, 25), (54, 47), (47, 68), (55, 48), (48, 69), (56, 49), (49, 70), (57, 50), (50, 9), (58, 51), (51, 73), (59, 52), (52, 10), (60, 53), (53, 75), (22, 41), (41, 79), (23, 42), (42, 80), (24, 43), (43, 81), (25, 44), (44, 82), (6, 45), (45, 83), (6, 46), (46, 84), (3, 0), (0, 36), (0, 37), (0, 38), (0, 39), (0, 40), (9, 26), (26, 72), (9, 27), (27, 76), (9, 28), (28, 71), (10, 29), (29, 74), (10, 30), (30, 77), (4, 31), (31, 2), (4, 32), (32, 7), (4, 33), (33, 8), (4, 34), (34, 5), (4, 35), (35, 1), (5, 11), (11, 77), (8, 12), (12, 76), (2, 13), (13, 78), (4, 3), (54, 61), (55, 62), (56, 63), (57, 64), (58, 65), (59, 66), (60, 67), (36, 6), (37, 25), (38, 24), (39, 23), (40, 22), (61, 78), (62, 79), (63, 80), (64, 81), (65, 82), (66, 83), (67, 84)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """Transition2Inst"""
        self["GUID__"] = UUID('e3b6d80f-8580-44fa-a5a9-988923857d7c')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('eec7fdf1-4bc3-46e5-951d-da35c3e426af')
        self.vs[1]["name"] = """in1_1"""
        self.vs[1]["classtype"] = """IN1"""
        self.vs[1]["mm__"] = """IN1"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('6649f3f6-dcb7-4d1a-9bcc-6043400bb894')
        self.vs[2]["name"] = """state1"""
        self.vs[2]["classtype"] = """State"""
        self.vs[2]["mm__"] = """State"""
        self.vs[2]["cardinality"] = """+"""
        self.vs[2]["GUID__"] = UUID('f7d67208-9464-4be4-8692-881e27338bd9')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('6817a62c-7fe2-4483-8aa0-98205ab0330d')
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = UUID('523faec2-d939-46b0-afa1-7cb355c48a55')
        self.vs[5]["name"] = """statemachine1"""
        self.vs[5]["classtype"] = """StateMachine"""
        self.vs[5]["mm__"] = """StateMachine"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('1adf74c3-6591-4624-9f2b-ab86ca1de045')
        self.vs[6]["name"] = """inst1"""
        self.vs[6]["classtype"] = """Inst"""
        self.vs[6]["mm__"] = """Inst"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('61ff7129-a5c3-42fb-86ea-f0a33a06162d')
        self.vs[7]["name"] = """transition1"""
        self.vs[7]["classtype"] = """Transition"""
        self.vs[7]["mm__"] = """Transition"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('d05cb1c3-3e10-4c3d-a1ac-30afa1124dc4')
        self.vs[8]["name"] = """entrypoint1"""
        self.vs[8]["classtype"] = """EntryPoint"""
        self.vs[8]["mm__"] = """EntryPoint"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('cdb0d5c1-1b57-431f-ae91-d8e30342bafe')
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = UUID('30d59d4b-709d-4d2e-a90e-5704e2036a4f')
        self.vs[10]["name"] = """concat2"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('1da7f13b-cd1d-441b-9171-e914bb67062d')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('88ccc698-8b3f-4c08-ae37-57973c37006b')
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = UUID('4af8d7e2-558a-4751-a2ab-79a84dc2a790')
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = UUID('7eda4143-a98d-4b4a-abad-7344d1ac7dcb')
        self.vs[14]["associationType"] = """transitions"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('9ae31b08-3dd6-4933-aa4b-96781ce7de7c')
        self.vs[15]["associationType"] = """dest"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('0f4dda0f-0a0a-41fd-b9f6-00d4525c57c5')
        self.vs[16]["associationType"] = """type"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('4a3d5388-91d3-4941-88a6-ecdf29d0f743')
        self.vs[17]["associationType"] = """owningStateMachine"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('9929c00f-66e5-4f89-9b22-1abe8e4c4573')
        self.vs[18]["associationType"] = """channelNames"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = UUID('117448ae-8dd9-4bc1-a7be-52f0d61b3f33')
        self.vs[19]["associationType"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = UUID('94204bdc-66ab-4a86-b7bf-13168ab45aa0')
        self.vs[20]["associationType"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = UUID('eaa30af6-8b04-43a9-b2f6-d7dfced6c526')
        self.vs[21]["associationType"] = """channelNames"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = UUID('db01d575-224c-407e-840e-7d16e10ca759')
        self.vs[22]["name"] = """name1"""
        self.vs[22]["classtype"] = """Name"""
        self.vs[22]["mm__"] = """Name"""
        self.vs[22]["cardinality"] = """1"""
        self.vs[22]["GUID__"] = UUID('7db3d0ec-8a05-4a43-aa75-304244d4caa1')
        self.vs[23]["name"] = """name2"""
        self.vs[23]["classtype"] = """Name"""
        self.vs[23]["mm__"] = """Name"""
        self.vs[23]["cardinality"] = """1"""
        self.vs[23]["GUID__"] = UUID('a150928e-d986-4697-b70e-ab86d2c8f33c')
        self.vs[24]["name"] = """name3"""
        self.vs[24]["classtype"] = """Name"""
        self.vs[24]["mm__"] = """Name"""
        self.vs[24]["cardinality"] = """1"""
        self.vs[24]["GUID__"] = UUID('b597cb7e-d133-4b43-aa06-daa83500b7c7')
        self.vs[25]["name"] = """name4"""
        self.vs[25]["classtype"] = """Name"""
        self.vs[25]["mm__"] = """Name"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = UUID('87fc9f68-ba42-42d1-9a87-74c760d6dd0a')
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = UUID('cf359b58-d394-4b53-8284-674ae45aac3c')
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = UUID('3afe0335-7ced-490d-aae2-799b618737b4')
        self.vs[28]["mm__"] = """hasArgs"""
        self.vs[28]["GUID__"] = UUID('93476d6b-1604-4564-8e48-fc27af82bb68')
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = UUID('df18105d-1c9a-41a3-bdab-b0cdd5efc41a')
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = UUID('d22848d4-6c52-4313-9cc2-0548c30e0fed')
        self.vs[31]["mm__"] = """match_contains"""
        self.vs[31]["GUID__"] = UUID('bfb1bac3-1253-4c74-89b1-6e3c3497edae')
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = UUID('0a53b67a-a796-412b-8b7f-97cd7887eb8b')
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = UUID('ade1037a-c51d-41fa-bc09-3ef4ac902ac1')
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = UUID('a1fb9e20-fa79-4776-981b-869f5eb375ac')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('ea6e7fcf-5d27-48e1-a605-90523452ad4f')
        self.vs[36]["mm__"] = """apply_contains"""
        self.vs[36]["GUID__"] = UUID('024a5c83-54b1-4bc1-8688-f732d3b4872f')
        self.vs[37]["mm__"] = """apply_contains"""
        self.vs[37]["GUID__"] = UUID('3b61a2b2-6362-48fb-9117-f59c0f0376bf')
        self.vs[38]["mm__"] = """apply_contains"""
        self.vs[38]["GUID__"] = UUID('cfbb3119-0d6b-4f93-8058-543b2df1008d')
        self.vs[39]["mm__"] = """apply_contains"""
        self.vs[39]["GUID__"] = UUID('d5972f2c-1f9d-416d-a35e-e49451ba78a9')
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = UUID('f77221c3-b620-40cc-aa7f-902ffd9501bc')
        self.vs[41]["mm__"] = """hasAttribute_T"""
        self.vs[41]["GUID__"] = UUID('68c85db6-bec0-4501-ab66-6ead3c60e1a3')
        self.vs[42]["mm__"] = """hasAttribute_T"""
        self.vs[42]["GUID__"] = UUID('68a6d7ea-e76b-439d-bc7b-568a9b35dd62')
        self.vs[43]["mm__"] = """hasAttribute_T"""
        self.vs[43]["GUID__"] = UUID('bf7e664a-f616-4656-9cab-8e40ac0647d8')
        self.vs[44]["mm__"] = """hasAttribute_T"""
        self.vs[44]["GUID__"] = UUID('2e1485b7-ef95-404b-952c-8f7cdb812ea0')
        self.vs[45]["mm__"] = """hasAttribute_T"""
        self.vs[45]["GUID__"] = UUID('2f1f7746-38a8-41a1-ab36-aa361dc64fde')
        self.vs[46]["mm__"] = """hasAttribute_T"""
        self.vs[46]["GUID__"] = UUID('d8c289fc-749f-459c-af64-72565b4f918a')
        self.vs[47]["mm__"] = """rightExpr"""
        self.vs[47]["GUID__"] = UUID('1c2c6e65-5228-4a11-9f0d-0042eb1921e3')
        self.vs[48]["mm__"] = """rightExpr"""
        self.vs[48]["GUID__"] = UUID('3f46a6d0-114f-42fa-b70f-0e0830006a40')
        self.vs[49]["mm__"] = """rightExpr"""
        self.vs[49]["GUID__"] = UUID('6e6d46b4-1921-4531-9a49-4f5d8e81bc57')
        self.vs[50]["mm__"] = """rightExpr"""
        self.vs[50]["GUID__"] = UUID('0ec61165-68dc-4bc5-803f-2d8894b94869')
        self.vs[51]["mm__"] = """rightExpr"""
        self.vs[51]["GUID__"] = UUID('bc8f171a-5894-480f-bf2b-32cb63171bf1')
        self.vs[52]["mm__"] = """rightExpr"""
        self.vs[52]["GUID__"] = UUID('c11d3140-7cca-4d43-b8f7-948e28dfd9dd')
        self.vs[53]["mm__"] = """rightExpr"""
        self.vs[53]["GUID__"] = UUID('f6826c19-5df1-4e9d-bcc9-026ba6eff297')
        self.vs[54]["name"] = """eq1"""
        self.vs[54]["mm__"] = """Equation"""
        self.vs[54]["GUID__"] = UUID('1654f3f4-72d7-4205-abe1-dd6b4c5b7479')
        self.vs[55]["name"] = """eq2"""
        self.vs[55]["mm__"] = """Equation"""
        self.vs[55]["GUID__"] = UUID('992ef8ce-9b0e-4f14-a9a3-b40e87c8ef86')
        self.vs[56]["name"] = """eq3"""
        self.vs[56]["mm__"] = """Equation"""
        self.vs[56]["GUID__"] = UUID('ff7c7c0f-50e6-45ce-a450-2e24d9222d5f')
        self.vs[57]["name"] = """eq4"""
        self.vs[57]["mm__"] = """Equation"""
        self.vs[57]["GUID__"] = UUID('0b6fff13-1282-420c-9e7c-bea06015bb84')
        self.vs[58]["name"] = """eq5"""
        self.vs[58]["mm__"] = """Equation"""
        self.vs[58]["GUID__"] = UUID('9bf1a1d3-d2bc-41da-b90d-7adce34f3302')
        self.vs[59]["name"] = """eq6"""
        self.vs[59]["mm__"] = """Equation"""
        self.vs[59]["GUID__"] = UUID('ba2fde17-ca50-42c5-8317-24930ea20d4e')
        self.vs[60]["name"] = """eq7"""
        self.vs[60]["mm__"] = """Equation"""
        self.vs[60]["GUID__"] = UUID('c7d53714-bae5-46ff-9748-3db74924ab51')
        self.vs[61]["mm__"] = """leftExpr"""
        self.vs[61]["GUID__"] = UUID('20ee3dae-732f-467c-b005-d7592c9a3449')
        self.vs[62]["mm__"] = """leftExpr"""
        self.vs[62]["GUID__"] = UUID('ece69ba0-49c0-4d06-9433-798ad8b2d0c0')
        self.vs[63]["mm__"] = """leftExpr"""
        self.vs[63]["GUID__"] = UUID('e89b7e6b-5211-415b-8020-3789562e1a34')
        self.vs[64]["mm__"] = """leftExpr"""
        self.vs[64]["GUID__"] = UUID('ba3881ad-d4ec-437b-81b5-39f8c59b1c42')
        self.vs[65]["mm__"] = """leftExpr"""
        self.vs[65]["GUID__"] = UUID('5be4e840-4fd7-42e4-856b-8004a3fcc0f3')
        self.vs[66]["mm__"] = """leftExpr"""
        self.vs[66]["GUID__"] = UUID('4c667d1a-e770-491b-a626-04ff915cf25b')
        self.vs[67]["mm__"] = """leftExpr"""
        self.vs[67]["GUID__"] = UUID('f3058580-7720-4f9f-877c-d64ec4a7e141')
        self.vs[68]["name"] = """true"""
        self.vs[68]["mm__"] = """Constant"""
        self.vs[68]["Type"] = """'Bool'"""
        self.vs[68]["GUID__"] = UUID('c5229ae0-7b2b-43d8-910f-29bd04deec65')
        self.vs[69]["name"] = """exit_in"""
        self.vs[69]["mm__"] = """Constant"""
        self.vs[69]["Type"] = """'String'"""
        self.vs[69]["GUID__"] = UUID('eb2cd9b8-eee1-48d3-a6c0-9deb9b9aff74')
        self.vs[70]["name"] = """exack_in"""
        self.vs[70]["mm__"] = """Constant"""
        self.vs[70]["Type"] = """'String'"""
        self.vs[70]["GUID__"] = UUID('7b219c70-50c5-4642-9b5f-9e245ed62229')
        self.vs[71]["name"] = """xox"""
        self.vs[71]["mm__"] = """Constant"""
        self.vs[71]["Type"] = """'String'"""
        self.vs[71]["GUID__"] = UUID('e262a896-2337-4e41-bae0-1ef8578ad6e4')
        self.vs[72]["name"] = """xox"""
        self.vs[72]["mm__"] = """Constant"""
        self.vs[72]["Type"] = """'String'"""
        self.vs[72]["GUID__"] = UUID('7630e466-0536-4f9f-b426-458db90290df')
        self.vs[73]["name"] = """sh_in"""
        self.vs[73]["mm__"] = """Constant"""
        self.vs[73]["Type"] = """'String'"""
        self.vs[73]["GUID__"] = UUID('0e4462a4-7dbe-4bec-8227-12232ef5f828')
        self.vs[74]["name"] = """S"""
        self.vs[74]["mm__"] = """Constant"""
        self.vs[74]["Type"] = """'String'"""
        self.vs[74]["GUID__"] = UUID('295fd11a-30a0-43be-9a41-a8b70d909447')
        self.vs[75]["name"] = """instForInTrans"""
        self.vs[75]["mm__"] = """Constant"""
        self.vs[75]["Type"] = """'String'"""
        self.vs[75]["GUID__"] = UUID('fe4d9c44-c587-47d6-b9de-f0a893bf4fd3')
        self.vs[76]["name"] = """name"""
        self.vs[76]["mm__"] = """Attribute"""
        self.vs[76]["Type"] = """'String'"""
        self.vs[76]["GUID__"] = UUID('94a5e0a7-61c2-44a8-95f5-64c47cd01af9')
        self.vs[77]["name"] = """name"""
        self.vs[77]["mm__"] = """Attribute"""
        self.vs[77]["Type"] = """'String'"""
        self.vs[77]["GUID__"] = UUID('75d077e6-3930-4489-9f8d-b96cdaa1a422')
        self.vs[78]["name"] = """isComposite"""
        self.vs[78]["mm__"] = """Attribute"""
        self.vs[78]["Type"] = """'Bool'"""
        self.vs[78]["GUID__"] = UUID('09d2edab-c1d9-442f-a4b2-c5ac716af08b')
        self.vs[79]["name"] = """literal"""
        self.vs[79]["mm__"] = """Attribute"""
        self.vs[79]["Type"] = """'String'"""
        self.vs[79]["GUID__"] = UUID('5b9c61dc-189d-440a-9650-2dde2a2d175f')
        self.vs[80]["name"] = """literal"""
        self.vs[80]["mm__"] = """Attribute"""
        self.vs[80]["Type"] = """'String'"""
        self.vs[80]["GUID__"] = UUID('13132858-c135-4bfa-a635-c5d284c1f074')
        self.vs[81]["name"] = """literal"""
        self.vs[81]["mm__"] = """Attribute"""
        self.vs[81]["Type"] = """'String'"""
        self.vs[81]["GUID__"] = UUID('2ef9cf61-f3cf-4707-8ed3-3e24ba367533')
        self.vs[82]["name"] = """literal"""
        self.vs[82]["mm__"] = """Attribute"""
        self.vs[82]["Type"] = """'String'"""
        self.vs[82]["GUID__"] = UUID('adc8eb1e-f6e5-4a26-8f74-c7380b4080c5')
        self.vs[83]["name"] = """name"""
        self.vs[83]["mm__"] = """Attribute"""
        self.vs[83]["Type"] = """'String'"""
        self.vs[83]["GUID__"] = UUID('9388c69b-4f6e-471c-8242-508ece64bbeb')
        self.vs[84]["name"] = """pivot"""
        self.vs[84]["mm__"] = """Attribute"""
        self.vs[84]["Type"] = """'String'"""
        self.vs[84]["GUID__"] = UUID('b8f5976f-0365-4a3c-aa50-31cf415492d3')
