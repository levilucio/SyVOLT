

from core.himesis import Himesis

class HUnionDaughterRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HUnionDaughterRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionDaughterRule, self).__init__(name='HUnionDaughterRule', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([[0, 25], [25, 3], [0, 26], [26, 4], [0, 27], [27, 5], [1, 9], [9, 6], [1, 10], [10, 7], [3, 11], [11, 5], [5, 12], [12, 4], [6, 8], [8, 7], [6, 28], [28, 3], [7, 29], [29, 5], [7, 30], [30, 4], [6, 13], [13, 14], [15, 16], [16, 14], [15, 17], [17, 18], [7, 19], [19, 20], [21, 22], [22, 20], [21, 23], [23, 24], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """UnionDaughterRule"""
        self["GUID__"] = 6975863611577739308
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1954856707224904883
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5470210171089411687
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1934529909393599777
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 2261100835801457357
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 3144493727101206352
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Family"""
        self.vs[5]["mm__"] = """Family"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2887970237931435858
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """CommunityRoot"""
        self.vs[6]["mm__"] = """CommunityRoot"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8921735792390608552
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Woman"""
        self.vs[7]["mm__"] = """Woman"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 3782499470327087198
        self.vs[8]["associationType"] = """has"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 152469756416494944
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 1818184243157966113
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6671194050430602597
        self.vs[11]["associationType"] = """have"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 5565252990392562815
        self.vs[12]["associationType"] = """daughter"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 1409411876280895112
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 3660100141943919667
        self.vs[14]["name"] = """ApplyAttribute"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 1719992494388817869
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 1404371981771765290
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 6634011369581322676
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 5823530588687211208
        self.vs[18]["name"] = """root"""
        self.vs[18]["mm__"] = """Constant"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 5809769287614389197
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 2857702259279873692
        self.vs[20]["name"] = """ApplyAttribute"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 9138795181435641187
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 5905722737414828562
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 1216040211617894576
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 8176521394970944485
        self.vs[24]["name"] = """famMemberDaughter"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 1704821530847703578
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 3296319934895103119
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 4485860162779480492
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 5663037300753336932
        self.vs[28]["type"] = """ruleDef"""
        self.vs[28]["mm__"] = """backward_link"""
        self.vs[28]["GUID__"] = 1026847426422096483
        self.vs[29]["type"] = """ruleDef"""
        self.vs[29]["mm__"] = """backward_link"""
        self.vs[29]["GUID__"] = 190905747642901998
        self.vs[30]["type"] = """ruleDef"""
        self.vs[30]["mm__"] = """backward_link"""
        self.vs[30]["GUID__"] = 1485390749326646595

