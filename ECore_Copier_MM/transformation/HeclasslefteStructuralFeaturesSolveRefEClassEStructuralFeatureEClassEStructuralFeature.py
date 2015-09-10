

from core.himesis import Himesis

class HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature, self).__init__(name='HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature"""
        self["GUID__"] = 3525224390595480610
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 86804466480986934
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5453138388616074141
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 412338183357154381
        self.vs[3]["associationType"] = """eStructuralFeatures"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 6354873013594355563
        self.vs[4]["associationType"] = """eStructuralFeatures"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2111829456660231639
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EClass"""
        self.vs[5]["mm__"] = """EClass"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2470420311131639695
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4388861957379745426
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EStructuralFeature"""
        self.vs[7]["mm__"] = """EStructuralFeature"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3197533483808587095
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 2119333953814487966
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EClass"""
        self.vs[9]["mm__"] = """EClass"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7135338949370076026
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 677337769598247591
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EStructuralFeature"""
        self.vs[11]["mm__"] = """EStructuralFeature"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 6966255711564945251
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3018026550382442829
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 1667095267598676173
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5840466644563941974
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 3699166007061873683
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3431407202996650043
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4325699780447816233
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1209872705358570660
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 4162003231748975172
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 7135012806010825053
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 2223948072679937551
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 8171615330487646812
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 450859732800340905
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 9025088107045434807
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 5813659879599233615
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 7258322450005554572

