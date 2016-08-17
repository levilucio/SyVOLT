

from core.himesis import Himesis

class HeoperationOUTeGenericExceptionsSolveRefEOperationEGenericTypeEOperationEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationOUTeGenericExceptionsSolveRefEOperationEGenericTypeEOperationEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationOUTeGenericExceptionsSolveRefEOperationEGenericTypeEOperationEGenericType, self).__init__(name='HeoperationOUTeGenericExceptionsSolveRefEOperationEGenericTypeEOperationEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationOUTeGenericExceptionsSolveRefEOperationEGenericTypeEOperationEGenericType"""
        self["GUID__"] = 4788171618960519764
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4917697116120841654
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3813922077039655948
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3056453059615493951
        self.vs[3]["associationType"] = """eGenericExceptions"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2635692178382393299
        self.vs[4]["associationType"] = """eGenericExceptions"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 792211599389703829
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3868882221831967968
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7211375981526869061
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EGenericType"""
        self.vs[7]["mm__"] = """EGenericType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7967060527257026856
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 742345841861061736
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2012641825903755244
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1327423584911954806
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EGenericType"""
        self.vs[11]["mm__"] = """EGenericType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 6178531506374243554
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3664327602673942462
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 3223981959800890321
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6785632751355334596
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 5176215223894660039
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3895044296209003308
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4024059398633811673
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1127786744824811149
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2524981587675868556
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2776982927727920798
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4328516979856297897
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 45905022657588848
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3744063013678058400
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1276106479724447533
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 2496702223131163166
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6067110705978862478

