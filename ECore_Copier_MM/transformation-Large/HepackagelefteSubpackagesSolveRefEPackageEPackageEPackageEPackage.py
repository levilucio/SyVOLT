

from core.himesis import Himesis

class HepackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HepackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HepackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage, self).__init__(name='HepackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """epackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage"""
        self["GUID__"] = 2311505325353184135
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9218594852063356421
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2723361463517309507
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6468986532278061184
        self.vs[3]["associationType"] = """eSubpackages"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3420789399063013406
        self.vs[4]["associationType"] = """eSubpackages"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 7760167553714392005
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 7752797620786643366
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 605088784807819283
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 8277699380189979451
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 2387656822212210684
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 7192273161277740721
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 4756074584341926437
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 7955278127779601435
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 2761761553466551289
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 4335056454677632924
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 564811729926088465
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 4794966508074080349
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 7460558413670437736
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 453587633504200471
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 4598855338674897536
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 474556201196635572
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 1485880888628172305
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 440919681392127711
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 7954806676931685271
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EPackage"""
        self.vs[23]["mm__"] = """EPackage"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 1945876686386197807
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EPackage"""
        self.vs[24]["mm__"] = """EPackage"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 6182079020572468366
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EPackage"""
        self.vs[25]["mm__"] = """EPackage"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 135677758284154560
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EPackage"""
        self.vs[26]["mm__"] = """EPackage"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 5701029814982654204

