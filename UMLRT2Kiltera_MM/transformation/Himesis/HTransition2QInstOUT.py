

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HTransition2QInstOUT(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2QInstOUT.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstOUT, self).__init__(name='HTransition2QInstOUT', num_nodes=43, edges=[])
        
        # Add the edges
        self.add_edges([(9, 31), (31, 3), (9, 32), (32, 7), (7, 33), (33, 1), (9, 34), (34, 1), (8, 0), (0, 11), (22, 16), (16, 28), (23, 17), (17, 10), (24, 18), (18, 30), (11, 19), (19, 40), (8, 20), (20, 41), (8, 21), (21, 42), (38, 1), (1, 4), (5, 2), (2, 14), (2, 15), (10, 12), (12, 29), (10, 13), (13, 39), (6, 35), (35, 9), (6, 36), (36, 3), (6, 37), (37, 7), (6, 38), (4, 39), (6, 5), (22, 25), (23, 26), (24, 27), (14, 8), (15, 11), (25, 40), (26, 41), (27, 42)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """Transition2QInstOUT"""
        self["GUID__"] = UUID('04f0d992-4641-4944-b3ec-762cfa923c6a')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """channelNames"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('e338ea0b-bfad-4c26-80a5-50f22def76e9')
        self.vs[1]["name"] = """vertex1"""
        self.vs[1]["classtype"] = """Vertex"""
        self.vs[1]["mm__"] = """Vertex"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('6318e2a5-562f-42c0-86fc-ca502fd0d49d')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('c4c41a88-2ffc-4d96-b3df-22e8573cbba4')
        self.vs[3]["name"] = """out2_1"""
        self.vs[3]["classtype"] = """OUT2"""
        self.vs[3]["mm__"] = """OUT2"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('d9df40d5-9203-4e77-8ed9-d29f54efa222')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('70146bb4-0354-455e-87a2-d514ff4fe635')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('21450353-9ad0-4a35-b075-93dc7f16f180')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('d2855303-e491-4b1a-abc7-9af6a990f734')
        self.vs[7]["name"] = """statemachine1"""
        self.vs[7]["classtype"] = """StateMachine"""
        self.vs[7]["mm__"] = """StateMachine"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('626eebbc-6c91-4d37-89ba-05c7247533b5')
        self.vs[8]["name"] = """inst1"""
        self.vs[8]["classtype"] = """Inst"""
        self.vs[8]["mm__"] = """Inst"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('bacd666c-9fe9-4b9a-a09c-00b38435eca0')
        self.vs[9]["name"] = """transition1"""
        self.vs[9]["classtype"] = """Transition"""
        self.vs[9]["mm__"] = """Transition"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = UUID('675c11a9-78ae-40eb-bfaf-520be67f4717')
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('ef58a50e-15e7-444a-9de9-a2d84ffcea53')
        self.vs[11]["name"] = """name1"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('7025b17f-bbaa-4a32-80c1-7b723156e04b')
        self.vs[12]["mm__"] = """hasArgs"""
        self.vs[12]["GUID__"] = UUID('d6fa6f4c-0cad-42c0-a83d-c8b4809bb773')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('e2220143-5377-4508-bfd3-eac21023a031')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('d411a1a3-5d4a-42aa-960c-bbe211521e1d')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('42306890-9a06-4b3e-92f2-676c2ba58b8e')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('3ec1b392-8e5f-4126-bceb-9a76b886e793')
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = UUID('8bac9c10-40e6-4dd1-a6d2-7384dcff0f2f')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('d138e43d-a8db-46fc-afe1-d4aaff768cbd')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('5de5705b-a064-4076-aa4b-2f4a8fd04b5c')
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = UUID('dbfb5f48-6a4b-4cad-8a6e-0b58e7bace23')
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = UUID('b079b575-b672-43b6-bd5d-49b11f1231f8')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('186d54d1-6f16-42ac-adec-42bfdc9a6e09')
        self.vs[23]["name"] = """eq1"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('26d230b5-121a-4b53-9049-c6bf1745cf25')
        self.vs[24]["name"] = """eq3"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = UUID('90a8251a-396b-49d8-86ce-a29ea06d4ef6')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('24119f1b-acfc-48b2-85fe-e7d150d09f95')
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = UUID('2a0562c7-6874-40ab-bf89-5f7523b97a90')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('7f90280e-b460-4841-83be-4357c3343586')
        self.vs[28]["name"] = """sh"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('323c8547-ce5d-4ed3-b774-885c7f9c14ad')
        self.vs[29]["name"] = """B"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = UUID('45901d2b-f2d5-4930-95fc-e0657dddfd38')
        self.vs[30]["name"] = """instfortrans"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = UUID('5b928879-26dc-41e8-9ffb-ba762fd04d5b')
        self.vs[31]["associationType"] = """type"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = UUID('f0ed83c8-fc1f-4ff7-8346-f20f6b1b1966')
        self.vs[32]["associationType"] = """owningStateMachine"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = UUID('ab35b044-1ea7-43c5-819c-ad2fbc878476')
        self.vs[33]["associationType"] = """exitPoints"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = UUID('9b1c67b7-d640-4c85-808c-f5e8b4b2a6e1')
        self.vs[34]["associationType"] = """dest"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = UUID('ac8267d8-a570-4a48-ae96-cf15b90d95c6')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('4a66b867-4350-4f80-925f-8165957a47b4')
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = UUID('aa27839d-7a6f-47d7-a892-f16a3802a1f2')
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = UUID('88a260e5-1a90-4bf5-b3f0-058bb52c4cde')
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = UUID('93cae252-c60d-4daa-bf8b-e0684c99e22f')
        self.vs[39]["name"] = """name"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('86971ce8-6ecf-4802-89ef-669de1540ec0')
        self.vs[40]["name"] = """literal"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('d81be5e3-8827-49ad-9d72-ff7a8180186e')
        self.vs[41]["name"] = """name"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('61a4e298-2b6b-4acc-8ab5-e050ad67a716')
        self.vs[42]["name"] = """pivot"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('9a04c305-7f59-4e0e-998f-8b30bd93c38b')

