

from core.himesis import Himesis

class HegenerictypeOUTeClassifierSolveRefEGenericTypeEClassifierEGenericTypeEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HegenerictypeOUTeClassifierSolveRefEGenericTypeEClassifierEGenericTypeEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HegenerictypeOUTeClassifierSolveRefEGenericTypeEClassifierEGenericTypeEClassifier, self).__init__(name='HegenerictypeOUTeClassifierSolveRefEGenericTypeEClassifierEGenericTypeEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """egenerictypeOUTeClassifierSolveRefEGenericTypeEClassifierEGenericTypeEClassifier"""
        self["GUID__"] = 117709274106564881
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6676519710133644423
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1176221967511856068
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 9135943619821959559
        self.vs[3]["associationType"] = """eClassifier"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5832126431420901203
        self.vs[4]["associationType"] = """eClassifier"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 5408450337190564529
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EGenericType"""
        self.vs[5]["mm__"] = """EGenericType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 4627021825613318353
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4496076248191087905
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7793031743928288286
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7205826747144287124
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EGenericType"""
        self.vs[9]["mm__"] = """EGenericType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6858219720100566225
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 660563138846763612
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 4800381982972114669
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4764059174156966593
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 4941893639295468772
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 304508590503778783
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 5328501513961630595
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 7797542830758559365
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3338463729105059783
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1252359373377200073
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 7857722132946092792
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 9196550031619788925
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 1366981353923170199
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2110830228316811138
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3781343904156739718
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 7275478954960589019
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 5689023347330052374
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 7387033078860307837

