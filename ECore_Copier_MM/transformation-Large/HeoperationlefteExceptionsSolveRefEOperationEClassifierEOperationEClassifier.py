

from core.himesis import Himesis

class HeoperationlefteExceptionsSolveRefEOperationEClassifierEOperationEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationlefteExceptionsSolveRefEOperationEClassifierEOperationEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationlefteExceptionsSolveRefEOperationEClassifierEOperationEClassifier, self).__init__(name='HeoperationlefteExceptionsSolveRefEOperationEClassifierEOperationEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationlefteExceptionsSolveRefEOperationEClassifierEOperationEClassifier"""
        self["GUID__"] = 4830147818018407783
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2187180104923138849
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7211573392333489616
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1690667555044947518
        self.vs[3]["associationType"] = """eExceptions"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 8434451750005213083
        self.vs[4]["associationType"] = """eExceptions"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3843671353443443523
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2499928002132475280
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6408314901404139020
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1260532649913434009
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6451471377751860498
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8703800390030557624
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6867239410027957690
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8257351761402933341
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6048678060054628361
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 5544871544834684362
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4585560325894986481
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 1674329981885127561
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4692077207853581787
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5587387088069615693
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 9024230351933483998
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 3438604917843656538
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4489705022928648532
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 1964041197305096659
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 1043235335942522149
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 7656461216162834842
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6144645840695779735
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 3339556439652055201
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 4423552965207264147

