

from core.himesis import Himesis

class HeattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType, self).__init__(name='HeattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType"""
        self["GUID__"] = 7500290523339363630
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3345355481358239434
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2661112097501954342
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2884002363878182308
        self.vs[3]["associationType"] = """eGenericType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3237503427209923934
        self.vs[4]["associationType"] = """eGenericType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3487447824061178971
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAttribute"""
        self.vs[5]["mm__"] = """EAttribute"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 180383522542507929
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 9029141784669719181
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EGenericType"""
        self.vs[7]["mm__"] = """EGenericType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 705924063494009604
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 5107917165971943200
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAttribute"""
        self.vs[9]["mm__"] = """EAttribute"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8056650007601953622
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 8334363595364440411
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EGenericType"""
        self.vs[11]["mm__"] = """EGenericType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 638205883689070586
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5247899703763388228
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 9152985125860709070
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 8939660675905724386
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 4724550716111922994
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 6342963225845912724
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 8425545405611867446
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2510594769584959828
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2091737926535973939
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 8569331947771768572
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 684785101581142767
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 9082076936603064885
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4941466305534700405
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 2426201971054401358
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 4495076672642341780
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 7828040183483422309

