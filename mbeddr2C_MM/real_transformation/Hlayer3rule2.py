

from core.himesis import Himesis

class Hlayer3rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer3rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule2, self).__init__(name='Hlayer3rule2', num_nodes=49, edges=[])
        
        # Add the edges
        self.add_edges([[0, 18], [18, 12], [0, 19], [19, 3], [0, 20], [20, 4], [1, 21], [21, 13], [1, 22], [22, 5], [1, 23], [23, 6], [12, 14], [14, 3], [3, 15], [15, 4], [13, 16], [16, 5], [5, 17], [17, 6], [13, 7], [7, 12], [12, 24], [24, 30], [3, 25], [25, 31], [4, 26], [26, 32], [5, 8], [8, 33], [9, 10], [10, 33], [9, 11], [38, 47], [47, 32], [38, 48], [48, 29], [37, 45], [45, 28], [37, 46], [46, 38], [36, 43], [43, 31], [36, 44], [44, 37], [35, 41], [41, 27], [35, 42], [42, 36], [34, 39], [39, 30], [34, 40], [40, 35], [11, 34], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer3rule2"""
        self["GUID__"] = 2722114226721529004
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1690545755978910091
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4801240412585750723
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8375188997339392799
        self.vs[3]["name"] = """layer3rule2class1"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 5155372350888156861
        self.vs[4]["name"] = """layer3rule2class2"""
        self.vs[4]["classtype"] = """ComponentInstance"""
        self.vs[4]["mm__"] = """ComponentInstance"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 148113175994770160
        self.vs[5]["name"] = """layer3rule2class4"""
        self.vs[5]["classtype"] = """FunctionPrototype"""
        self.vs[5]["mm__"] = """FunctionPrototype"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 7968615809443145482
        self.vs[6]["name"] = """layer3rule2class5"""
        self.vs[6]["classtype"] = """VoidType"""
        self.vs[6]["mm__"] = """VoidType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 1007770323848821010
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 6053793745013368229
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 7458423502009632560
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 228942911969198042
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 3857402667608002975
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 6542114345896610882
        self.vs[12]["name"] = """layer3rule2class0"""
        self.vs[12]["classtype"] = """ImplementationModule"""
        self.vs[12]["mm__"] = """ImplementationModule"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = 818759343365418992
        self.vs[13]["name"] = """layer3rule2class3"""
        self.vs[13]["classtype"] = """ImplementationModule"""
        self.vs[13]["mm__"] = """ImplementationModule"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = 2788307415469877675
        self.vs[14]["associationType"] = """contents"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = 3170357892079804232
        self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = 4044779163689984307
        self.vs[16]["associationType"] = """contents"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 7036021720226932325
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 87406569571176564
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = 1053315995272885739
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = 4671619690714897012
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = 6044448561202542755
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 4301163100372642769
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 5368996989042809564
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 631675874862975730
        self.vs[24]["mm__"] = """hasAttribute_S"""
        self.vs[24]["GUID__"] = 3688816968567438595
        self.vs[25]["mm__"] = """hasAttribute_S"""
        self.vs[25]["GUID__"] = 8222259919875635423
        self.vs[26]["mm__"] = """hasAttribute_S"""
        self.vs[26]["GUID__"] = 7168754156189176526
        self.vs[27]["name"] = """_"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 6266091612577270905
        self.vs[28]["name"] = """_"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["GUID__"] = 3617917985382773477
        self.vs[29]["name"] = """__wire"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["GUID__"] = 8621331941013453956
        self.vs[30]["name"] = """name"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["GUID__"] = 6013162020089488254
        self.vs[31]["name"] = """name"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["GUID__"] = 6731126897205280848
        self.vs[32]["name"] = """name"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["GUID__"] = 7184342152679883169
        self.vs[33]["name"] = """name"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["GUID__"] = 1983309508826899502
        self.vs[34]["name"] = """Concatlayer3rule2class4attribute031"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["mm__"] = """Concat"""
        self.vs[34]["GUID__"] = 8015617781832624507
        self.vs[35]["name"] = """Concatlayer3rule2class4attribute034"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["mm__"] = """Concat"""
        self.vs[35]["GUID__"] = 3132478396576999624
        self.vs[36]["name"] = """Concatlayer3rule2class4attribute038"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["mm__"] = """Concat"""
        self.vs[36]["GUID__"] = 1420550251009311607
        self.vs[37]["name"] = """Concatlayer3rule2class4attribute041"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["mm__"] = """Concat"""
        self.vs[37]["GUID__"] = 953614434570897002
        self.vs[38]["name"] = """Concatlayer3rule2class4attribute045"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["mm__"] = """Concat"""
        self.vs[38]["GUID__"] = 1814954481816995908
        self.vs[39]["mm__"] = """hasArgs"""
        self.vs[39]["GUID__"] = 4008869787432069432
        self.vs[40]["mm__"] = """hasArgs"""
        self.vs[40]["GUID__"] = 7537905501413491536
        self.vs[41]["mm__"] = """hasArgs"""
        self.vs[41]["GUID__"] = 2119889914311232418
        self.vs[42]["mm__"] = """hasArgs"""
        self.vs[42]["GUID__"] = 8772355720924153596
        self.vs[43]["mm__"] = """hasArgs"""
        self.vs[43]["GUID__"] = 5137942043644380648
        self.vs[44]["mm__"] = """hasArgs"""
        self.vs[44]["GUID__"] = 2063390190060859068
        self.vs[45]["mm__"] = """hasArgs"""
        self.vs[45]["GUID__"] = 8314145746611953294
        self.vs[46]["mm__"] = """hasArgs"""
        self.vs[46]["GUID__"] = 4816330533300926019
        self.vs[47]["mm__"] = """hasArgs"""
        self.vs[47]["GUID__"] = 400972084160078270
        self.vs[48]["mm__"] = """hasArgs"""
        self.vs[48]["GUID__"] = 5028385589556675815

