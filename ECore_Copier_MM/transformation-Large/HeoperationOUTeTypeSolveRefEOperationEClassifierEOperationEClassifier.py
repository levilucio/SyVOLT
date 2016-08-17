

from core.himesis import Himesis

class HeoperationOUTeTypeSolveRefEOperationEClassifierEOperationEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationOUTeTypeSolveRefEOperationEClassifierEOperationEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationOUTeTypeSolveRefEOperationEClassifierEOperationEClassifier, self).__init__(name='HeoperationOUTeTypeSolveRefEOperationEClassifierEOperationEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationOUTeTypeSolveRefEOperationEClassifierEOperationEClassifier"""
        self["GUID__"] = 424446018023750853
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9192177577901060796
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7178308152118892884
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7593940650527012097
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 1325918869866211929
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6389656013786428490
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2308031356070592143
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3079852545320159404
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6041075333942441510
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6345817282536398188
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2182213367937335180
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 9160529496469068837
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8821001511612472449
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4931589341008871727
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8530064806362189876
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 8637927025533268026
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2310875166481492213
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8851384254674386548
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 8211698718914351398
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 8556184534004332741
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6367796968262173754
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4796966060506734327
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4936761161212732835
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 802891841990721287
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 665568347204246876
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 785097822406446557
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7341113776985595133
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 743072801165315752

