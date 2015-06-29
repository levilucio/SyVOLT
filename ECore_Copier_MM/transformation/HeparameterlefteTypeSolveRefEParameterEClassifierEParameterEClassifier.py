

from core.himesis import Himesis

class HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier, self).__init__(name='HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier"""
        self["GUID__"] = 8947834518386860899
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2586301352691820822
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7851509353061373582
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 9124761058207307012
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 7567889593289521995
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2798508867299703427
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EParameter"""
        self.vs[5]["mm__"] = """EParameter"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 4337549127798293920
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 9101679639648590274
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6545756247357778469
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7074702917940757451
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EParameter"""
        self.vs[9]["mm__"] = """EParameter"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 1315446653191548654
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 4077879401224231147
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2655518862741374986
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 9172513471228645511
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6168809680272526266
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 1812953428593598497
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 5552071457525344210
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4127873800974145644
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6725851505873163644
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 3394155783154710807
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2529625495517638084
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 6472268932712957583
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 220406439806186895
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 6627615356136868891
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 1902716974322132696
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 5954560624072599080
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 5172517672119474232
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 447368218909241437

