

from core.himesis import Himesis

class HWomanRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HWomanRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HWomanRule, self).__init__(name='HWomanRule', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 6], [6, 5], [3, 7], [7, 4], [3, 12], [12, 24], [4, 13], [13, 25], [5, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 8], [5, 18], [18, 27], [19, 20], [20, 27], [19, 21], [9, 22], [22, 25], [9, 23], [23, 24], [21, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """WomanRule"""
        self["GUID__"] = 8457742264251002894
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8009611726976446951
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 372794396720608293
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1327508891871377136
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 548707802918241195
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 1265182788181975267
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Woman"""
        self.vs[5]["mm__"] = """Woman"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2638110463662318278
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 2675147792078631318
        self.vs[7]["associationType"] = """mother"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 7028283342595829829
        self.vs[8]["name"] = """famMemberWoman"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 3888633219847485796
        self.vs[9]["name"] = """Concat25"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 4827450290373532125
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 2357147018267540791
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 4920382659406994684
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 2816163604048487751
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 2388982236619412180
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 8901117338204396981
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 6321408140296887898
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 2775049156363972732
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 7938925202965103280
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 2012130181368514873
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 5916101407977386735
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 866871253719943208
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 6079610504767178158
        self.vs[22]["mm__"] = """hasArgs"""
        self.vs[22]["GUID__"] = 6667908846669371930
        self.vs[23]["mm__"] = """hasArgs"""
        self.vs[23]["GUID__"] = 146736375655734441
        self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 852493860284510409
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 4378519500225498470
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 8605263999469323806
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 3910658592158815459

