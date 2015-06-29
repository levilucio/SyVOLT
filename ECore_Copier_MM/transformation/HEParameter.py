

from core.himesis import Himesis

class HEParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEParameter, self).__init__(name='HEParameter', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 37], [6, 9], [9, 38], [6, 10], [10, 39], [6, 11], [11, 40], [6, 12], [12, 41], [7, 13], [13, 42], [14, 15], [15, 42], [14, 16], [16, 37], [7, 17], [17, 43], [18, 19], [19, 43], [18, 20], [20, 38], [7, 21], [21, 44], [22, 23], [23, 44], [22, 24], [24, 39], [7, 25], [25, 45], [26, 27], [27, 45], [26, 28], [28, 40], [7, 29], [29, 46], [30, 31], [31, 46], [30, 32], [32, 41], [7, 33], [33, 47], [34, 35], [35, 47], [34, 36], [36, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EParameter"""
        self["GUID__"] = 6749339449011532152
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5066493726140259593
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1908786364551201335
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5028260838094772894
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 3169400082512507432
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 2632876681448156773
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 6486012414161783605
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EParameter"""
        self.vs[6]["mm__"] = """EParameter"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 6881549812873145573
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EParameter"""
        self.vs[7]["mm__"] = """EParameter"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1374841096582332606
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 6166835910555773068
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 5285090702680380818
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 3410391578316306121
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 8392174574851789981
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 1683555276503570350
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 4178649255826797861
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 3218521483481710976
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 513967555323393814
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 7694217592896266493
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 3938162461835846897
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 8242842033594615206
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 6084469532909539007
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 5708145222009623893
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7333130023844624237
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 7802685651846350843
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 2613473770656827096
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 7920621136354795701
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 2017881888437281160
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        self.vs[26]["GUID__"] = 6869055516404508506
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 6942896353284561786
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 8051803556628296849
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 7579565893053618768
        self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 3294339521285944565
        self.vs[31]["mm__"] = """leftExpr"""
        self.vs[31]["GUID__"] = 4780137751860573113
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = 5274868830233725502
        self.vs[33]["mm__"] = """hasAttribute_T"""
        self.vs[33]["GUID__"] = 1780505478519492102
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 5148601493768470115
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 3179735280525836967
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 197018344942197946
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 8624527481982154983
        self.vs[38]["name"] = """ordered"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 7041827744980570228
        self.vs[39]["name"] = """unique"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 6720486629244464940
        self.vs[40]["name"] = """lowerBound"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 4692748426544002121
        self.vs[41]["name"] = """upperBound"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 6604354944828621312
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 1722851899342158711
        self.vs[43]["name"] = """ordered"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 9027578460472773257
        self.vs[44]["name"] = """unique"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 5888080645134518665
        self.vs[45]["name"] = """lowerBound"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 7005335248644790718
        self.vs[46]["name"] = """upperBound"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 3669375322603962123
        self.vs[47]["name"] = """ApplyAttribute"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 8632882251326510590

