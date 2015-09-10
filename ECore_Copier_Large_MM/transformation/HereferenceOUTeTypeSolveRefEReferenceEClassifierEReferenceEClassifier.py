

from core.himesis import Himesis

class HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier, self).__init__(name='HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier"""
        self["GUID__"] = 7384547820026194404
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4272322158019531650
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7152692080517083330
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8562434998297218990
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3581907394171172151
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6877728499490855938
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 104623451246837376
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3606811084380408803
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4414550636340212865
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6852194026466895187
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4375092161575132562
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2766176047324396630
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8726566990403406363
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5020680833199755442
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 3736525257041567966
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2929987396798340693
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2087401244582663070
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4829005596049772133
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 718358423727880053
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 5832194158748181801
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 4895556508895146771
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 1281690433410431972
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6493269687449489446
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2448025679146951847
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 1073296510818810236
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 5640927105030127825
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 8052091284044342389
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6483842809814649856

