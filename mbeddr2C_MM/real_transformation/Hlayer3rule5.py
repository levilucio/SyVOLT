

from core.himesis import Himesis

class Hlayer3rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer3rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule5, self).__init__(name='Hlayer3rule5', num_nodes=33, edges=[])
        
        # Add the edges
        self.add_edges([[0, 14], [14, 13], [0, 15], [15, 3], [1, 23], [23, 16], [1, 24], [24, 4], [1, 25], [25, 5], [13, 6], [6, 3], [16, 17], [17, 4], [4, 18], [18, 5], [16, 7], [7, 13], [13, 19], [19, 26], [3, 20], [20, 27], [4, 8], [8, 28], [9, 10], [10, 28], [9, 11], [22, 31], [31, 12], [22, 32], [32, 27], [21, 29], [29, 26], [21, 30], [30, 22], [11, 21], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer3rule5"""
        self["GUID__"] = 4303714822784739265
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7094597229188919725
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9002247540469939512
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 519541451605398707
        self.vs[3]["name"] = """layer3rule5class1"""
        self.vs[3]["classtype"] = """TestCase"""
        self.vs[3]["mm__"] = """TestCase"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 3919620588585908882
        self.vs[4]["name"] = """layer3rule5class3"""
        self.vs[4]["classtype"] = """FunctionPrototype"""
        self.vs[4]["mm__"] = """FunctionPrototype"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 2819199474376925258
        self.vs[5]["name"] = """layer3rule5class4"""
        self.vs[5]["classtype"] = """VoidType"""
        self.vs[5]["mm__"] = """VoidType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5791685160057797672
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_S"""
        self.vs[6]["GUID__"] = 5149197745929836506
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 4499837968626885383
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 3767378573382432743
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 2853437606445799134
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 3394929353282027624
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 4851603274455934586
        self.vs[12]["name"] = """_"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["mm__"] = """Constant"""
        self.vs[12]["GUID__"] = 1496751475580267605
        self.vs[13]["name"] = """layer3rule5class0"""
        self.vs[13]["classtype"] = """ImplementationModule"""
        self.vs[13]["mm__"] = """ImplementationModule"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = 3138799743003332872
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 7538938848646825845
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 4348853679234533789
        self.vs[16]["name"] = """layer3rule5class2"""
        self.vs[16]["classtype"] = """ImplementationModule"""
        self.vs[16]["mm__"] = """ImplementationModule"""
        self.vs[16]["cardinality"] = """1"""
        self.vs[16]["GUID__"] = 8473591807027325715
        self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 4679650173462021934
        self.vs[18]["associationType"] = """type"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = 3211326572899297902
        self.vs[19]["mm__"] = """hasAttribute_S"""
        self.vs[19]["GUID__"] = 6138458738813941621
        self.vs[20]["mm__"] = """hasAttribute_S"""
        self.vs[20]["GUID__"] = 7563007725499157237
        self.vs[21]["name"] = """Concatlayer3rule5class3attribute026"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["mm__"] = """Concat"""
        self.vs[21]["GUID__"] = 1829610763563507772
        self.vs[22]["name"] = """Concatlayer3rule5class3attribute029"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Concat"""
        self.vs[22]["GUID__"] = 2306200848832710537
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 5399054749567138694
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 4181899886279519426
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = 6553054580352442733
        self.vs[26]["name"] = """name"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = 4731356539597097985
        self.vs[27]["name"] = """name"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["GUID__"] = 6409802135123494261
        self.vs[28]["name"] = """name"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["GUID__"] = 3918876666188006471
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = 2463400461719384869
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = 2974099109696682495
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = 7217247852610009266
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 6896295022055211094

