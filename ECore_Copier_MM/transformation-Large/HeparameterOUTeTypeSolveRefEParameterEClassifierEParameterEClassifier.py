

from core.himesis import Himesis

class HeparameterOUTeTypeSolveRefEParameterEClassifierEParameterEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeparameterOUTeTypeSolveRefEParameterEClassifierEParameterEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeparameterOUTeTypeSolveRefEParameterEClassifierEParameterEClassifier, self).__init__(name='HeparameterOUTeTypeSolveRefEParameterEClassifierEParameterEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eparameterOUTeTypeSolveRefEParameterEClassifierEParameterEClassifier"""
        self["GUID__"] = 4109714719636350362
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5196833136443227844
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5335636835502066202
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4690101007742171832
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2238959356200816461
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2782049712604787816
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EParameter"""
        self.vs[5]["mm__"] = """EParameter"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1027039694583409823
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5579978830065751312
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3737905671808833092
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 5294580772967439108
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EParameter"""
        self.vs[9]["mm__"] = """EParameter"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8539626378867922084
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7762327410800803744
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 4351793663753078334
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5360037725451503293
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7963899392918269250
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2643782155055160290
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8664154206246741290
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4348000290046174004
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6181512690932340532
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1738928666903825222
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1632645191410624537
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5928498627999664323
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3126418976032920603
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 3886930940215909828
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4537638174846410588
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3691775069722029343
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 9018541899650748417
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 5779595723905149266

