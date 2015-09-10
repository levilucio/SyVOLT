

from core.himesis import Himesis

class HeclasslefteAnnotationsSolveRefEClassEAnnotationEClassEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclasslefteAnnotationsSolveRefEClassEAnnotationEClassEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclasslefteAnnotationsSolveRefEClassEAnnotationEClassEAnnotation, self).__init__(name='HeclasslefteAnnotationsSolveRefEClassEAnnotationEClassEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclasslefteAnnotationsSolveRefEClassEAnnotationEClassEAnnotation"""
        self["GUID__"] = 1967168956248356356
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1945143228266002373
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7880802285291825121
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8111603748207664931
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 7718970627554007399
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6420629268660536686
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EClass"""
        self.vs[5]["mm__"] = """EClass"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 6782111062471684374
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5137505662326072115
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4607561817419454905
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4966390251983289474
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EClass"""
        self.vs[9]["mm__"] = """EClass"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4204653762234326148
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7458588879935249666
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2446395381437947956
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 907391584439606211
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6917808394810915060
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 7329891363515446038
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 9152773140815291121
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 6187731196635368671
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3411008749780932811
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1451481599114899161
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 5760127974134855428
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 8735633893684210584
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 869487963134911809
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 6736716652714801760
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 413138640854042380
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6296606593921398578
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 2879725726020050119
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8539285759769689663

