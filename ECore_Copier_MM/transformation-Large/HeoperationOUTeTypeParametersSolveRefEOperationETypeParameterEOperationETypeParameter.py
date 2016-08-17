

from core.himesis import Himesis

class HeoperationOUTeTypeParametersSolveRefEOperationETypeParameterEOperationETypeParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationOUTeTypeParametersSolveRefEOperationETypeParameterEOperationETypeParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationOUTeTypeParametersSolveRefEOperationETypeParameterEOperationETypeParameter, self).__init__(name='HeoperationOUTeTypeParametersSolveRefEOperationETypeParameterEOperationETypeParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationOUTeTypeParametersSolveRefEOperationETypeParameterEOperationETypeParameter"""
        self["GUID__"] = 4435630720948241196
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3808294906631425948
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6704461277805051339
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4403356183883373190
        self.vs[3]["associationType"] = """eTypeParameters"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3037171043381526273
        self.vs[4]["associationType"] = """eTypeParameters"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 8138622826390697562
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5233388312893727119
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 1766078854901397058
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ETypeParameter"""
        self.vs[7]["mm__"] = """ETypeParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7196452878662075224
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6819777654543679943
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 1303350185906834109
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6008334052828947535
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ETypeParameter"""
        self.vs[11]["mm__"] = """ETypeParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 546291824691763151
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3954865000512043587
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6727990482212958418
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5452511052961302633
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8313577342005231322
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 5363292105420746295
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4246790457107269204
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1695960364970878750
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2073932141582630439
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 8892926405829538072
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 1786341143801025908
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2567326669929784651
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3054768956023821173
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1640620513030002789
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7092782651256167786
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8913375256392572887

