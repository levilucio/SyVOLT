

from core.himesis import Himesis

class HeattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier, self).__init__(name='HeattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier"""
        self["GUID__"] = 4765147938407728873
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8535993327210313330
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7555134151556594261
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7633045357617543135
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 536543925273797877
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 1532049739852249159
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAttribute"""
        self.vs[5]["mm__"] = """EAttribute"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2801626087785056034
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5680065940465064391
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3091048174211359728
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 2133496569626869196
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAttribute"""
        self.vs[9]["mm__"] = """EAttribute"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 5665400088949056115
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 401678743675738549
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 1473818062833040246
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 1845769691357108892
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 150267654570739990
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6510976342661573689
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8095425635966561760
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 7114117534563049418
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2103969746537014078
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 7783026411972863457
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2225385317818312360
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5887028608244628289
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 2741541200170154631
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 1749996128998111192
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 2386532640524706727
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8605059509997477018
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 3907951089951151044
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 7454503879490098361

