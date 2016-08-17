

from core.himesis import Himesis

class HepackageOUTeFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HepackageOUTeFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HepackageOUTeFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory, self).__init__(name='HepackageOUTeFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """epackageOUTeFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory"""
        self["GUID__"] = 4709174051022166187
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4231580133452891083
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8631377411555995428
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4237852361844278249
        self.vs[3]["associationType"] = """eFactoryInstance"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5218313243529445137
        self.vs[4]["associationType"] = """eFactoryInstance"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6836889693106884853
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EPackage"""
        self.vs[5]["mm__"] = """EPackage"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2514770223916284325
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5349404699201334775
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EFactory"""
        self.vs[7]["mm__"] = """EFactory"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5048402173467301935
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 536283503097499105
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EPackage"""
        self.vs[9]["mm__"] = """EPackage"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8470835144066371415
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6875894762205235978
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EFactory"""
        self.vs[11]["mm__"] = """EFactory"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8069813301381615213
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5797562316180377653
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 521590616679632308
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 743327577253593610
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8475936060619617328
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 2541931610233514074
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6708348967188956303
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1675741724473110817
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 186368678036501396
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 3341488270157212101
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5317975929562910499
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 9130525873714163321
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3570720800914918025
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8166534211753768185
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 686081286119546133
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 4665868472507240272

