

from core.himesis import Himesis

class HEEnumLiteral(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEEnumLiteral.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEEnumLiteral, self).__init__(name='HEEnumLiteral', num_nodes=34, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 27], [6, 9], [9, 28], [6, 10], [10, 29], [7, 11], [11, 30], [12, 13], [13, 30], [12, 14], [14, 27], [7, 15], [15, 31], [16, 17], [17, 31], [16, 18], [18, 28], [7, 19], [19, 32], [20, 21], [21, 32], [20, 22], [22, 29], [7, 23], [23, 33], [24, 25], [25, 33], [24, 26], [26, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EEnumLiteral"""
        self["GUID__"] = 4558136981394933924
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 310162465802877310
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6343483957675861186
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3467513448555658471
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 1613711446593694645
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 6313369066027177018
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 9206185180348173058
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EEnumLiteral"""
        self.vs[6]["mm__"] = """EEnumLiteral"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 5604346888782148423
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EEnumLiteral"""
        self.vs[7]["mm__"] = """EEnumLiteral"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 7287926594333753070
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 8908890576303988165
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 3144827787733102834
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 4375129227184307981
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 50966187032179347
        self.vs[12]["name"] = """eq_"""
        self.vs[12]["mm__"] = """Equation"""
        self.vs[12]["GUID__"] = 6248134636434646881
        self.vs[13]["mm__"] = """leftExpr"""
        self.vs[13]["GUID__"] = 4604017049030590360
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 476755277108383371
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 5009467508760700754
        self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = 9033540789096792579
        self.vs[17]["mm__"] = """leftExpr"""
        self.vs[17]["GUID__"] = 6209865852961303194
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = 485010101910837647
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 717209630604038206
        self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        self.vs[20]["GUID__"] = 4865593291975254903
        self.vs[21]["mm__"] = """leftExpr"""
        self.vs[21]["GUID__"] = 7254639492188645850
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 1957288682621511040
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = 1038960452427696712
        self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = 8593722164037616005
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 7463155533999835571
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = 5437079881025655692
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 8332195325301366962
        self.vs[28]["name"] = """value"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 3813786989955698381
        self.vs[29]["name"] = """instance"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 8743550639718594643
        self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = 3423966285988088193
        self.vs[31]["name"] = """value"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = 5924027152655063277
        self.vs[32]["name"] = """instance"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 3136461620418565313
        self.vs[33]["name"] = """ApplyAttribute"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 5175023318042544174

