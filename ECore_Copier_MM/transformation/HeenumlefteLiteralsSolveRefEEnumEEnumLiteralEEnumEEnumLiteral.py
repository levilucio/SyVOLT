

from core.himesis import Himesis

class HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral, self).__init__(name='HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral"""
        self["GUID__"] = 5485823344221208828
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6850472287012574347
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8922580743663690970
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 9112781513832893444
        self.vs[3]["associationType"] = """eLiterals"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2055986137017493144
        self.vs[4]["associationType"] = """eLiterals"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 5323490873118151284
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EEnum"""
        self.vs[5]["mm__"] = """EEnum"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5037507503445089957
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5078215745713800016
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EEnumLiteral"""
        self.vs[7]["mm__"] = """EEnumLiteral"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4423868817006334339
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 1610031893697241136
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EEnum"""
        self.vs[9]["mm__"] = """EEnum"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6103592759612918198
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 8223023841356876962
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EEnumLiteral"""
        self.vs[11]["mm__"] = """EEnumLiteral"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8310119395647516060
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 7506515484568732986
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8126544916030499879
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 979325526670265930
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 9215450630382736053
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8946667691330259774
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 7053513620425751299
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1559416485291026117
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6522390968376860582
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5505683868740165717
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6412677525279532537
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 7561882659592668475
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4928191820073307639
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6369210366134918789
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7629018128502024115
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 2504927941738604252

