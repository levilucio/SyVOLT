

from core.himesis import Himesis

class HegenerictypeOUTeUpperBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HegenerictypeOUTeUpperBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HegenerictypeOUTeUpperBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType, self).__init__(name='HegenerictypeOUTeUpperBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """egenerictypeOUTeUpperBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType"""
        self["GUID__"] = 3734714033570221592
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6635136322183342904
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2114557495085775112
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7368303190660175551
        self.vs[3]["associationType"] = """eUpperBound"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3063830049347856781
        self.vs[4]["associationType"] = """eUpperBound"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 8761592588881449642
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 7450947819977480279
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 8171720685469802437
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 4974367327146903535
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 6461287043466238280
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 630111066073442268
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 8204709517030428164
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 3529712902707625811
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 7381502734311539589
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 8119863107018886222
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 1709228727870683218
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 8771270902062297412
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 4040428509349643510
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 2653488582886686258
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 2805979440282939390
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 5454141605510275668
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 4559195293024617085
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 6512038889700924215
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 5806388713828211937
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EGenericType"""
        self.vs[23]["mm__"] = """EGenericType"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 6845659052015235326
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EGenericType"""
        self.vs[24]["mm__"] = """EGenericType"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 2116621941944756607
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EGenericType"""
        self.vs[25]["mm__"] = """EGenericType"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 8726101737871191315
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EGenericType"""
        self.vs[26]["mm__"] = """EGenericType"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 6757717084710083514

