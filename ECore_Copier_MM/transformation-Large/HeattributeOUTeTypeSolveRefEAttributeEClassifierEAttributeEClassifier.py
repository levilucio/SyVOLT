

from core.himesis import Himesis

class HeattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier, self).__init__(name='HeattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier"""
        self["GUID__"] = 3742844623519195810
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9121184809675232806
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1612396965234750349
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 757368196000983860
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 6973608622513064424
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3712687355741701215
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAttribute"""
        self.vs[5]["mm__"] = """EAttribute"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 6642503275034388891
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5609296520118283978
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7930254848063447971
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7206306843059185902
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAttribute"""
        self.vs[9]["mm__"] = """EAttribute"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 209490495226888738
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1145468736183007676
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2803943428873137815
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4717964771043476762
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 1637765777982604118
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 1467178596937847991
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 1944276835699359309
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 2574073570656851072
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3678277356007623714
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2294398262332599662
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 538092855384078242
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4767275185275030371
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6302794502347180887
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 8708000758327525875
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 8357976920041755405
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8108832280067151098
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 1035939230522006041
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 1416065531247900148

