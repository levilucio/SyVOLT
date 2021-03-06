

from core.himesis import Himesis

class HepackagelefteClassifiersSolveRefEPackageEClassifierEPackageEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HepackagelefteClassifiersSolveRefEPackageEClassifierEPackageEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HepackagelefteClassifiersSolveRefEPackageEClassifierEPackageEClassifier, self).__init__(name='HepackagelefteClassifiersSolveRefEPackageEClassifierEPackageEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """epackagelefteClassifiersSolveRefEPackageEClassifierEPackageEClassifier"""
        self["GUID__"] = 1637569243490002813
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8172937490155739430
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 835179154965955717
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3200681570207913185
        self.vs[3]["associationType"] = """eClassifiers"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2987931577010535784
        self.vs[4]["associationType"] = """eClassifiers"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2526615103121616315
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EPackage"""
        self.vs[5]["mm__"] = """EPackage"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 162577832098114504
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 138184002025605592
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2288899628806279379
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3084594632682682457
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EPackage"""
        self.vs[9]["mm__"] = """EPackage"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 450161203772578476
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2917955487002358059
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 4512228908359498529
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2634584285091346424
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8571929317004878751
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4620270213572713756
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 9071899922691776293
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4692446295416608001
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4998500585952983340
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6012882971373510672
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2680872810924081575
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 3174587760863713661
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 8144662928460111577
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 8305075292692690669
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6371636209819726880
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1841299939334753040
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 6249495404791531500
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 5527938434520648689

