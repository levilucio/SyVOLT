

from core.himesis import Himesis

class HefactoryOUTePackageSolveRefEFactoryEPackageEFactoryEPackage(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HefactoryOUTePackageSolveRefEFactoryEPackageEFactoryEPackage.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HefactoryOUTePackageSolveRefEFactoryEPackageEFactoryEPackage, self).__init__(name='HefactoryOUTePackageSolveRefEFactoryEPackageEFactoryEPackage', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """efactoryOUTePackageSolveRefEFactoryEPackageEFactoryEPackage"""
        self["GUID__"] = 3717429310681033793
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4993505578531848852
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 641118400718646217
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3013382963369961364
        self.vs[3]["associationType"] = """ePackage"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 4205420215888253255
        self.vs[4]["associationType"] = """ePackage"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 4552145397151403403
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EFactory"""
        self.vs[5]["mm__"] = """EFactory"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 8160873012583365614
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4950919886052945288
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EPackage"""
        self.vs[7]["mm__"] = """EPackage"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7782164468330729641
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 1475092258545241046
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EFactory"""
        self.vs[9]["mm__"] = """EFactory"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 111848876990288534
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2156646667581448299
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EPackage"""
        self.vs[11]["mm__"] = """EPackage"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8495697497500912009
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 7764741560807901711
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7319753417328787838
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5375655492637912269
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2348614815311596633
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8654721226966675585
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4177899911257930411
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2625403877406551997
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 355646058349337534
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 6339328845287662122
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 8130085914009820639
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 4538201449256482928
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6331758233922162775
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 7665126590232307398
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 573854148080077150
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 2320144929494642788

