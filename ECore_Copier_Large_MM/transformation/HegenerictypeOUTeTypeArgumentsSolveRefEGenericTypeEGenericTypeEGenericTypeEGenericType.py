

from core.himesis import Himesis

class HegenerictypeOUTeTypeArgumentsSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HegenerictypeOUTeTypeArgumentsSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HegenerictypeOUTeTypeArgumentsSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType, self).__init__(name='HegenerictypeOUTeTypeArgumentsSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """egenerictypeOUTeTypeArgumentsSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType"""
        self["GUID__"] = 1163969356209401305
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4263021132154131796
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5619287812245906582
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8420125055152812126
        self.vs[3]["associationType"] = """eTypeArguments"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3224463837021539350
        self.vs[4]["associationType"] = """eTypeArguments"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6659254865219541633
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 9124198635123170308
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6053289240507681181
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 4756544661523032137
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 2074544952341431160
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 4395877569753897891
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 5755352215703555148
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 1379025442644676028
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 6961227487732529866
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 5111756796927249086
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 188683875786463223
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 2680405351181085385
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 1221252493769467845
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 4390020033630803312
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 2838696940734216097
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4874175365016707056
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 9013291510455054357
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 2147594448672403304
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 7035658593419061562
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EGenericType"""
        self.vs[23]["mm__"] = """EGenericType"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 3943489011835763053
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EGenericType"""
        self.vs[24]["mm__"] = """EGenericType"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 6527184657356461016
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EGenericType"""
        self.vs[25]["mm__"] = """EGenericType"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 3013009137772184559
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EGenericType"""
        self.vs[26]["mm__"] = """EGenericType"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 3045567106934400514

