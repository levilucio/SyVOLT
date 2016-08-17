

from core.himesis import Himesis

class HeclasslefteOperationsSolveRefEClassEOperationEClassEOperation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclasslefteOperationsSolveRefEClassEOperationEClassEOperation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclasslefteOperationsSolveRefEClassEOperationEClassEOperation, self).__init__(name='HeclasslefteOperationsSolveRefEClassEOperationEClassEOperation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclasslefteOperationsSolveRefEClassEOperationEClassEOperation"""
        self["GUID__"] = 462954409801849393
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6954027704260084537
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 532483440262095149
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8376329556651738805
        self.vs[3]["associationType"] = """eOperations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2332780939052661589
        self.vs[4]["associationType"] = """eOperations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 7371630957236949189
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EClass"""
        self.vs[5]["mm__"] = """EClass"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2347665438325433326
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4685435128987263563
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EOperation"""
        self.vs[7]["mm__"] = """EOperation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5651903018524761781
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6929436415206612381
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EClass"""
        self.vs[9]["mm__"] = """EClass"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8556749978378026648
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1281113383570764084
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EOperation"""
        self.vs[11]["mm__"] = """EOperation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2668596919474249295
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4965845654513090691
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6662413568797736049
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6947749854822258121
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 397253454953559567
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 7310782928622430971
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2201342219425827406
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2897212445066683158
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8353751640685595367
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 9079747118239079879
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4065992746093258734
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 4094131165274511970
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6805337444540015879
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3995131250724452817
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7857222495059779213
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 100280768079233326

