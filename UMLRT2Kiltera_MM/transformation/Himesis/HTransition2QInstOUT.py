

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
        self["GUID__"] = UUID('000bfa90-d5ef-4d77-b3d8-d2db02506e06')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """channelNames"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('478bd655-aa0f-493b-9b2e-fc7b54e6f94b')
        self.vs[1]["name"] = """vertex1"""
        self.vs[1]["classtype"] = """Vertex"""
        self.vs[1]["mm__"] = """Vertex"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('f841bd05-1e93-4860-aa80-409e570b7d36')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('96414446-6f9d-4ad1-81f5-b4168e30f954')
        self.vs[3]["name"] = """out2_1"""
        self.vs[3]["classtype"] = """OUT2"""
        self.vs[3]["mm__"] = """OUT2"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = UUID('8368a8dc-b3f0-4e68-8012-97ee9d3ca7cc')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('20050eae-665f-42d3-a4f8-5236b78d26e4')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('c377974e-e3c1-48e8-8961-3b15d7b8fc9a')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('c493245e-b4b6-4115-9b57-4b3622f58c7a')
        self.vs[7]["name"] = """statemachine1"""
        self.vs[7]["classtype"] = """StateMachine"""
        self.vs[7]["mm__"] = """StateMachine"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('ca035b19-0b92-4564-9e9c-89cf7d27ac74')
        self.vs[8]["name"] = """inst1"""
        self.vs[8]["classtype"] = """Inst"""
        self.vs[8]["mm__"] = """Inst"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('37232d24-cc2b-4b83-a286-d981a4a89103')
        self.vs[9]["name"] = """transition1"""
        self.vs[9]["classtype"] = """Transition"""
        self.vs[9]["mm__"] = """Transition"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = UUID('3bc1b2a7-eba7-4c40-9ffe-993b0ef00705')
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = UUID('3eacf01a-9f26-43dc-bd2c-80299189a326')
        self.vs[11]["name"] = """name1"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('81a7dad1-c198-4132-9b90-64041dd89809')
        self.vs[12]["mm__"] = """hasArgs"""
        self.vs[12]["GUID__"] = UUID('818e7c5b-e836-468f-82a0-adcae0573941')
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = UUID('84e08698-e29d-427b-bef9-098be833d369')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('4ad43da8-d4fd-4cd9-b494-f2fcaf00309a')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('ae7b8a65-23cd-483d-b7c1-72d8d37a147f')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('9e76cf22-cb98-45fe-80e9-e90069acc0b8')
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = UUID('73a22411-8461-499c-8463-00b8698a7e4e')
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = UUID('f434ed62-14f2-462f-87be-c638b50ac1e2')
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = UUID('04ba9a12-f98f-4367-90f2-27f1d89e38f9')
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = UUID('864af444-2138-468f-9515-f5111729b538')
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = UUID('9c404698-8d9a-4011-aa78-ca27cc2f84ee')
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = UUID('619395d1-e277-40bc-bfd5-9151c907adc2')
        self.vs[23]["name"] = """eq1"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = UUID('1fb3a4ca-d27a-4c38-9c0e-249810574a01')
        self.vs[24]["name"] = """eq3"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = UUID('7832336d-d730-4f5d-b81a-e0e42e121229')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('98ee9a79-d276-425b-b2c4-44c25985a4ec')
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = UUID('ab3b7c73-a1da-4ec8-ac15-9bb255f514bc')
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = UUID('75ec880c-d4f1-4c67-a99c-b5d95fe58733')
        self.vs[28]["name"] = """sh"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('0d3ba04e-541a-437b-a49b-04f53af350db')
        self.vs[29]["name"] = """B"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = UUID('9d9e593f-4a6b-487c-aa36-6f86ff6f5902')
        self.vs[30]["name"] = """instfortrans"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = UUID('53f80ace-792a-45c2-aa04-09a75dde2151')
        self.vs[31]["associationType"] = """type"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = UUID('32adb3e1-6afd-46a0-b3fe-c48eb02a9e4c')
        self.vs[32]["associationType"] = """owningStateMachine"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = UUID('2f7c0909-41e8-4d98-b42f-6367bff2e185')
        self.vs[33]["associationType"] = """exitPoints"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = UUID('5ed999f0-07f1-4a7b-9a2f-c7176f748999')
        self.vs[34]["associationType"] = """dest"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = UUID('b5ff77e1-683a-47ec-a231-63d74466acc0')
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = UUID('e32e7df1-624b-466a-86d5-9b0e32f2093f')
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = UUID('ca6e1432-3cd4-43f2-8c26-b9e7f07868aa')
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = UUID('20bf4f66-d794-4690-beca-018cdf779807')
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = UUID('593fc0a7-0433-4599-9c7c-02d3dc45af69')
        self.vs[39]["name"] = """name"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = UUID('0e461f91-f8d3-4113-9220-0bc484dfba3a')
        self.vs[40]["name"] = """literal"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = UUID('25d120c2-46e4-4ee3-906b-7b4a057def7a')
        self.vs[41]["name"] = """name"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = UUID('d8fa60d9-d2c9-45fc-8482-ffd651b9c1a5')
        self.vs[42]["name"] = """pivot"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = UUID('e654d083-9551-4f7f-bd9b-51042704c3d7')

