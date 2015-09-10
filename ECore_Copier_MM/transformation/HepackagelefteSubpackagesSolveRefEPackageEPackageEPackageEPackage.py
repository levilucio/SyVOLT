

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
        self.vs[0]["GUID__"] = 7677506752797922491
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2106704214998908376
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1600137721138981516
        self.vs[3]["associationType"] = """eSubpackages"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 8423558233614059220
        self.vs[4]["associationType"] = """eSubpackages"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 371305503591138304
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 8166737395252824113
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 8337038070528842345
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 8900390451387851622
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 7291946324904642636
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["GUID__"] = 4362921370697843437
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["GUID__"] = 7561384909334318899
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 4579870555401082648
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = 2783018483080520813
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 2860299789555354485
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 3872519859621231165
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 2631105914355509768
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["GUID__"] = 8894612232734408751
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 7023230429255755368
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["GUID__"] = 3175989419592596515
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 7560402338740417722
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 1661717578710846453
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 8852089132526946210
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["GUID__"] = 6356862967791070510
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EPackage"""
        self.vs[23]["mm__"] = """EPackage"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 327087108804353286
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EPackage"""
        self.vs[24]["mm__"] = """EPackage"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 314830980110560905
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EPackage"""
        self.vs[25]["mm__"] = """EPackage"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 8377362257397708981
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EPackage"""
        self.vs[26]["mm__"] = """EPackage"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 6716433728426337837

