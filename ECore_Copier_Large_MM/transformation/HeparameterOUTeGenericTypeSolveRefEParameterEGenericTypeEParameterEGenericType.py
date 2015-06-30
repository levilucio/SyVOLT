

from core.himesis import Himesis

class HeparameterOUTeGenericTypeSolveRefEParameterEGenericTypeEParameterEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeparameterOUTeGenericTypeSolveRefEParameterEGenericTypeEParameterEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeparameterOUTeGenericTypeSolveRefEParameterEGenericTypeEParameterEGenericType, self).__init__(name='HeparameterOUTeGenericTypeSolveRefEParameterEGenericTypeEParameterEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eparameterOUTeGenericTypeSolveRefEParameterEGenericTypeEParameterEGenericType"""
        self["GUID__"] = 6699309772541566019
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7797916025078712187
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4632374264890659388
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5181650114519713613
        self.vs[3]["associationType"] = """eGenericType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 4699311558597537133
        self.vs[4]["associationType"] = """eGenericType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2763557195883674650
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EParameter"""
        self.vs[5]["mm__"] = """EParameter"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2359728984087608413
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 541501703309738921
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EGenericType"""
        self.vs[7]["mm__"] = """EGenericType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5751706889238175354
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7408437507025746121
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EParameter"""
        self.vs[9]["mm__"] = """EParameter"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7700773634606521349
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 4926777893558757941
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EGenericType"""
        self.vs[11]["mm__"] = """EGenericType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8125258216804491866
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4783707159961982771
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8301644529340859946
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4940722633125469759
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 648325783003479938
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4708970177002588869
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6805676789110400649
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 3318388048551559553
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 7318244023344006145
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 543105047331211401
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7349328738455272923
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 4031397444402386861
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 5286744168256527019
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 5944602992072900844
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 2665921729122478640
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8432313864781556758

