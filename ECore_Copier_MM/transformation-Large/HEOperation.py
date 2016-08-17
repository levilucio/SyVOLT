

from core.himesis import Himesis

class HEOperation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEOperation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEOperation, self).__init__(name='HEOperation', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 37], [6, 9], [9, 38], [6, 10], [10, 39], [6, 11], [11, 40], [6, 12], [12, 41], [7, 13], [13, 42], [14, 15], [15, 42], [14, 16], [16, 37], [7, 17], [17, 43], [18, 19], [19, 43], [18, 20], [20, 38], [7, 21], [21, 44], [22, 23], [23, 44], [22, 24], [24, 39], [7, 25], [25, 45], [26, 27], [27, 45], [26, 28], [28, 40], [7, 29], [29, 46], [30, 31], [31, 46], [30, 32], [32, 41], [7, 33], [33, 47], [34, 35], [35, 47], [34, 36], [36, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EOperation"""
        self["GUID__"] = 5655672644192994165
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7660167473522130430
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7013968127810372500
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4045402376054543100
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 2172176497330642339
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 6209129734844524575
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 5344118111702294352
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EOperation"""
        self.vs[6]["mm__"] = """EOperation"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 1686780261536799063
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EOperation"""
        self.vs[7]["mm__"] = """EOperation"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 7626481590968188248
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 3536166385162117727
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 1464597587616384151
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 1350809393502574576
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 965155818467026446
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 7310554859125840039
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 5744438435478525730
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 8337220745246610547
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 2563598895621004273
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 5288498327781001122
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 5238300264103967076
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 9170606126778369557
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 8223625806063009863
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 3617166988237835997
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6147198171902242869
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 396053287289583777
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 5111740585639067173
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 1096386367514403908
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 634194051408272210
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        self.vs[26]["GUID__"] = 6306715130714294480
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 4380838281989136760
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 5855632012024954166
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 22779994074243194
        self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 5065029525151965250
        self.vs[31]["mm__"] = """leftExpr"""
        self.vs[31]["GUID__"] = 1536436329247519890
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = 9024372505114061664
        self.vs[33]["mm__"] = """hasAttribute_T"""
        self.vs[33]["GUID__"] = 9060043959546923575
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 7475245586963462076
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 1786863342008372497
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 7841707050695274475
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 616305899089290799
        self.vs[38]["name"] = """ordered"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 106576842962946350
        self.vs[39]["name"] = """unique"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 4812027357528808734
        self.vs[40]["name"] = """lowerBound"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 6858921450571077173
        self.vs[41]["name"] = """upperBound"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 3595279696945346583
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 7911215376889123242
        self.vs[43]["name"] = """ordered"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 3183619382689423504
        self.vs[44]["name"] = """unique"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 6083106354023772124
        self.vs[45]["name"] = """lowerBound"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 3740563471252359756
        self.vs[46]["name"] = """upperBound"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 4969944714622754204
        self.vs[47]["name"] = """ApplyAttribute"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 1455372024716410919

