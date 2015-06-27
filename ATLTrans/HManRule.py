

from core.himesis import Himesis

class HManRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HManRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HManRule, self).__init__(name='HManRule', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 6], [6, 5], [3, 7], [7, 4], [3, 12], [12, 24], [4, 13], [13, 25], [5, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 8], [5, 18], [18, 27], [19, 20], [20, 27], [19, 21], [9, 22], [22, 25], [9, 23], [23, 24], [21, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ManRule"""
        self["GUID__"] = 1518737727439020560
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4665626218708646587
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3426597900953428626
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7893119959234729278
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8649144747482177161
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 9024485515169962067
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Man"""
        self.vs[5]["mm__"] = """Man"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 6239816436654288907
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 2118956497773014940
        self.vs[7]["associationType"] = """father"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 382519105464057084
        self.vs[8]["name"] = """famMemberMan"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 2446622892667027954
        self.vs[9]["name"] = """Concat25"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 8054805059857317129
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 8216763959335065929
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 7029143308538900043
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 2198529069597928647
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 1415556121533609124
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 3719552517063582867
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 4766823180487793159
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 7952876096835225435
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 6717780342835172473
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 7881961352980688349
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 148962736808281359
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 7135478253470514847
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 6452395482149373614
        self.vs[22]["mm__"] = """hasArgs"""
        self.vs[22]["GUID__"] = 5048866479673836652
        self.vs[23]["mm__"] = """hasArgs"""
        self.vs[23]["GUID__"] = 811581169213819816
        self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 8978506466111092627
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 4055777145146873305
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 8586252860598058128
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 262767465669255140

