

from core.himesis import Himesis

class HepackageOUTeSubpackagesSolveRefEPackageEPackageEPackageEPackage(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HepackageOUTeSubpackagesSolveRefEPackageEPackageEPackageEPackage.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HepackageOUTeSubpackagesSolveRefEPackageEPackageEPackageEPackage, self).__init__(name='HepackageOUTeSubpackagesSolveRefEPackageEPackageEPackageEPackage', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """epackageOUTeSubpackagesSolveRefEPackageEPackageEPackageEPackage"""
        self["GUID__"] = 1581342654108745616
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 290992640484679191
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 672100292046221234
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6377429414622976717
        self.vs[3]["associationType"] = """eSubpackages"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 6566430165682136576
        self.vs[4]["associationType"] = """eSubpackages"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 98618361033713296
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 3001762155184743657
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3667479716978987836
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 7225139742180289730
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 7835999257857258444
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 8306035710734088912
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 8724681125610634958
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 7074221729166972243
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 3969684362550886650
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 4245989091516644437
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 6610931304275467954
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 8516799144973711986
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 7690598942770243219
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 3930262704084063244
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 6283378703191028377
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4201508073434092205
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 2116542749602851289
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 4613343998931197358
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 1570563951474468032
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EPackage"""
        self.vs[23]["mm__"] = """EPackage"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 6110896378602777011
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EPackage"""
        self.vs[24]["mm__"] = """EPackage"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 7697114445801458346
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EPackage"""
        self.vs[25]["mm__"] = """EPackage"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 4611533363297466222
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EPackage"""
        self.vs[26]["mm__"] = """EPackage"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 5577902695125458360

