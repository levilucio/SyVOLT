

from core.himesis import Himesis

class HMotherRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMotherRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMotherRule, self).__init__(name='HMotherRule', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 6], [6, 5], [3, 7], [7, 4], [3, 12], [12, 24], [4, 13], [13, 25], [5, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 8], [5, 18], [18, 27], [19, 20], [20, 27], [19, 21], [9, 22], [22, 25], [9, 23], [23, 24], [21, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """MotherRule"""
        self["GUID__"] = 4730744551579486757
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1015963421896407843
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8282172216519396368
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6194870155548178116
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 305003275633303473
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4138277694835655474
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Woman"""
        self.vs[5]["mm__"] = """Woman"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5422469374931066975
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 2142672395269086641
        self.vs[7]["associationType"] = """mother"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 875673741042183092
        self.vs[8]["name"] = """famMemberMother"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 1627586778927396000
        self.vs[9]["name"] = """Concat25"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 1264653663269209784
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 9157906074030743660
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 8497742158846110986
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 3569655681832529896
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 2716813269152775616
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 4898394296837767794
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 1816621347152661201
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 8453835729267098996
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 1584521443797795889
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 3915398271343584138
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4554567644635950407
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 54865672022491640
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 6201199321262275895
        self.vs[22]["mm__"] = """hasArgs"""
        self.vs[22]["GUID__"] = 8450281554808356535
        self.vs[23]["mm__"] = """hasArgs"""
        self.vs[23]["GUID__"] = 770528175706543359
        self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 3162051575458428136
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 4725497937161195254
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 9217751372490761334
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 5582443067348719344

