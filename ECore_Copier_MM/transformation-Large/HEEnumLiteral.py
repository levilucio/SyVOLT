

from core.himesis import Himesis

class HEEnumLiteral(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEEnumLiteral.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEEnumLiteral, self).__init__(name='HEEnumLiteral', num_nodes=41, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 32], [6, 9], [9, 33], [6, 10], [10, 34], [6, 11], [11, 35], [7, 12], [12, 36], [13, 14], [14, 36], [13, 15], [15, 32], [7, 16], [16, 37], [17, 18], [18, 37], [17, 19], [19, 33], [7, 20], [20, 38], [21, 22], [22, 38], [21, 23], [23, 34], [7, 24], [24, 39], [25, 26], [26, 39], [25, 27], [27, 35], [7, 28], [28, 40], [29, 30], [30, 40], [29, 31], [31, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EEnumLiteral"""
        self["GUID__"] = 4558136981394933924
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8101889034385461966
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1442388161125307722
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8645673757689307601
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 8739923037735507106
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 3336667162408061991
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 8547036357036538361
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EEnumLiteral"""
        self.vs[6]["mm__"] = """EEnumLiteral"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 5099637847705449182
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EEnumLiteral"""
        self.vs[7]["mm__"] = """EEnumLiteral"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 2187790684093147517
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 215828077114473740
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 7837857838657339598
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 8272327147694414003
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 3178388044972738503
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = 8198002675663758747
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 1096914896769884454
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 609456725398937898
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 6458552033092392922
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 8615941297134690132
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 8032316592740897135
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6404389690332166926
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 416095492830756471
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = 3921191445445872942
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 2656040434553206528
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 6745839880893916146
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 147952023357446018
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = 7244107268603249602
        self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        self.vs[25]["GUID__"] = 4290007487669934071
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = 5489988626905157977
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = 4117125160840642472
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = 1185723138392162651
        self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = 6038158924035385783
        self.vs[30]["mm__"] = """leftExpr"""
        self.vs[30]["GUID__"] = 3115404126435040789
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = 2427842587256421048
        self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 8513988969729325821
        self.vs[33]["name"] = """value"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 7775167660342505810
        self.vs[34]["name"] = """instance"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 6429384321488924066
        self.vs[35]["name"] = """literal"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["GUID__"] = 4161215510177905992
        self.vs[36]["name"] = """name"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 6621693705500303987
        self.vs[37]["name"] = """value"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 1410670431357855190
        self.vs[38]["name"] = """instance"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 5200203948556067592
        self.vs[39]["name"] = """literal"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 5154938578810256501
        self.vs[40]["name"] = """ApplyAttribute"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 516865020118147674

