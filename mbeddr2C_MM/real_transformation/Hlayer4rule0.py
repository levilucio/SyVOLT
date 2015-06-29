

from core.himesis import Himesis

class Hlayer4rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer4rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule0, self).__init__(name='Hlayer4rule0', num_nodes=52, edges=[])
        
        # Add the edges
        self.add_edges([[0, 17], [17, 13], [0, 18], [18, 3], [0, 19], [19, 4], [1, 29], [29, 14], [1, 30], [30, 5], [1, 31], [31, 6], [1, 32], [32, 7], [13, 15], [15, 3], [3, 16], [16, 4], [14, 20], [20, 5], [5, 21], [21, 6], [5, 22], [22, 7], [14, 8], [8, 13], [13, 23], [23, 33], [3, 24], [24, 34], [4, 25], [25, 35], [5, 9], [9, 36], [10, 11], [11, 36], [10, 12], [41, 50], [50, 35], [41, 51], [51, 28], [40, 48], [48, 27], [40, 49], [49, 41], [39, 46], [46, 34], [39, 47], [47, 40], [38, 44], [44, 26], [38, 45], [45, 39], [37, 42], [42, 33], [37, 43], [43, 38], [12, 37], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer4rule0"""
        self["GUID__"] = 3303658752271827800
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4205754168243793061
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7438470220973857653
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1723811367447053140
        self.vs[3]["name"] = """layer4rule0class1"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4836970014377240306
        self.vs[4]["name"] = """layer4rule0class2"""
        self.vs[4]["classtype"] = """ComponentInstance"""
        self.vs[4]["mm__"] = """ComponentInstance"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4062909205005884483
        self.vs[5]["name"] = """layer4rule0class4"""
        self.vs[5]["classtype"] = """Function"""
        self.vs[5]["mm__"] = """Function"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3485137225544125092
        self.vs[6]["name"] = """layer4rule0class5"""
        self.vs[6]["classtype"] = """VoidType"""
        self.vs[6]["mm__"] = """VoidType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 2547057548168388441
        self.vs[7]["name"] = """layer4rule0class6"""
        self.vs[7]["classtype"] = """StatementList"""
        self.vs[7]["mm__"] = """StatementList"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1439828700040650157
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["type"] = """ruleDef"""
        self.vs[8]["GUID__"] = 7973863358521227642
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 6676356641279038930
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 6319871805543569169
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 6197006303695238763
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 7378398354384033717
        self.vs[13]["name"] = """layer4rule0class0"""
        self.vs[13]["classtype"] = """ImplementationModule"""
        self.vs[13]["mm__"] = """ImplementationModule"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = 7056684760981377241
        self.vs[14]["name"] = """layer4rule0class3"""
        self.vs[14]["classtype"] = """ImplementationModule"""
        self.vs[14]["mm__"] = """ImplementationModule"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = 9124898660936707700
        self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = 5223338284713142533
        self.vs[16]["associationType"] = """contents"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = 8178576485349992543
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = 6050399826910750525
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = 598890860850370732
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = 1502964557004290990
        self.vs[20]["associationType"] = """contents"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = 2370986965577892660
        self.vs[21]["associationType"] = """type"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = 7795245098235225114
        self.vs[22]["associationType"] = """body"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = 92443489655344879
        self.vs[23]["mm__"] = """hasAttribute_S"""
        self.vs[23]["GUID__"] = 1449305795537209527
        self.vs[24]["mm__"] = """hasAttribute_S"""
        self.vs[24]["GUID__"] = 8231560110052509997
        self.vs[25]["mm__"] = """hasAttribute_S"""
        self.vs[25]["GUID__"] = 7853967178341340164
        self.vs[26]["name"] = """_"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 4316935311400845973
        self.vs[27]["name"] = """_"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 3230094559300689434
        self.vs[28]["name"] = """__wire"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["GUID__"] = 6560014084059723646
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = 4064831884562266643
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = 3760403733873121814
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = 4361301146516030100
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = 2811983000467165057
        self.vs[33]["name"] = """name"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["GUID__"] = 7845507500159077359
        self.vs[34]["name"] = """name"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["GUID__"] = 7445205270852535962
        self.vs[35]["name"] = """name"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["GUID__"] = 1750436019175273729
        self.vs[36]["name"] = """name"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["GUID__"] = 5321000915069404268
        self.vs[37]["name"] = """Concatlayer4rule0class4attribute034"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["mm__"] = """Concat"""
        self.vs[37]["GUID__"] = 7436570382637272673
        self.vs[38]["name"] = """Concatlayer4rule0class4attribute037"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["mm__"] = """Concat"""
        self.vs[38]["GUID__"] = 6514944513211711372
        self.vs[39]["name"] = """Concatlayer4rule0class4attribute041"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["mm__"] = """Concat"""
        self.vs[39]["GUID__"] = 8777768184587764677
        self.vs[40]["name"] = """Concatlayer4rule0class4attribute044"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["mm__"] = """Concat"""
        self.vs[40]["GUID__"] = 672686645718109767
        self.vs[41]["name"] = """Concatlayer4rule0class4attribute048"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["mm__"] = """Concat"""
        self.vs[41]["GUID__"] = 9003331103557202452
        self.vs[42]["mm__"] = """hasArgs"""
        self.vs[42]["GUID__"] = 3094918218345454266
        self.vs[43]["mm__"] = """hasArgs"""
        self.vs[43]["GUID__"] = 1059889413125048071
        self.vs[44]["mm__"] = """hasArgs"""
        self.vs[44]["GUID__"] = 4262886666218264282
        self.vs[45]["mm__"] = """hasArgs"""
        self.vs[45]["GUID__"] = 8260867084775197337
        self.vs[46]["mm__"] = """hasArgs"""
        self.vs[46]["GUID__"] = 2566820529196821454
        self.vs[47]["mm__"] = """hasArgs"""
        self.vs[47]["GUID__"] = 5403112819721005339
        self.vs[48]["mm__"] = """hasArgs"""
        self.vs[48]["GUID__"] = 2336805450534967734
        self.vs[49]["mm__"] = """hasArgs"""
        self.vs[49]["GUID__"] = 5793390006367941931
        self.vs[50]["mm__"] = """hasArgs"""
        self.vs[50]["GUID__"] = 3815596986537381535
        self.vs[51]["mm__"] = """hasArgs"""
        self.vs[51]["GUID__"] = 6054720891362211207

