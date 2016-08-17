

from core.himesis import Himesis

class HeattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation, self).__init__(name='HeattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation"""
        self["GUID__"] = 7550486544553541240
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7626014172030242045
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3727004838746124882
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3940912710484206409
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 7542728076422993015
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 7478456262460425328
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAttribute"""
        self.vs[5]["mm__"] = """EAttribute"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3185294255855098617
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6681142183469548485
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6258557237535921024
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7747189759517425990
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAttribute"""
        self.vs[9]["mm__"] = """EAttribute"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7252733596803385156
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 706710278862596708
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 7047231288824683224
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5106424627917802341
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7271101115311340832
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6536932245824915451
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 6337906921224669249
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8538113880597338322
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2071483856593159591
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 579416891797961628
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 314011744246255416
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4215134239440822882
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6950311117796173519
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 3327240772969449251
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 8319129256141374218
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6618500388056299370
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 1977123364517822703
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8886010151994762398

