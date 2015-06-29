

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
        self.vs[0]["GUID__"] = 2349741084656002296
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1698200933654799582
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1279504677246170552
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 8403306242030835434
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 182985560560777127
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 2272403042598444574
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EOperation"""
        self.vs[6]["mm__"] = """EOperation"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 3510254610971977054
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EOperation"""
        self.vs[7]["mm__"] = """EOperation"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 7230396022660084720
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 7354774646149057451
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 9030678926305662310
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 1668191866697394228
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 2727205682400516366
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 7038471773927484739
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 7716471996337662985
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 14633557779776965
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 6821702741326234981
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 5691903449550541426
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 3760575299484167483
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 3516209773573194437
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 8182667084193462978
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 4557444671438980705
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5855460836042468719
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 2111225842379693338
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 6411478630717596226
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 8418202449478014638
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 6834750771330396440
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        self.vs[26]["GUID__"] = 1702484783028014866
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 3700196298452459538
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 2799635856191533654
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 7652256510150391268
        self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 6747491396810411609
        self.vs[31]["mm__"] = """leftExpr"""
        self.vs[31]["GUID__"] = 5529125698324934703
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = 6873405646020638791
        self.vs[33]["mm__"] = """hasAttribute_T"""
        self.vs[33]["GUID__"] = 2410736583885622679
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 2114381928451914275
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 5970032384135495781
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 5331602328928154248
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 6165387995052735803
        self.vs[38]["name"] = """ordered"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 6362164819486616144
        self.vs[39]["name"] = """unique"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 6563484413584312951
        self.vs[40]["name"] = """lowerBound"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 2921736144407152895
        self.vs[41]["name"] = """upperBound"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 547956903115148763
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 176960579472552476
        self.vs[43]["name"] = """ordered"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 3596916216257454569
        self.vs[44]["name"] = """unique"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 1606269498719635526
        self.vs[45]["name"] = """lowerBound"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 6355824469280334375
        self.vs[46]["name"] = """upperBound"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 4646585716293145040
        self.vs[47]["name"] = """ApplyAttribute"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 7892050384737894044

