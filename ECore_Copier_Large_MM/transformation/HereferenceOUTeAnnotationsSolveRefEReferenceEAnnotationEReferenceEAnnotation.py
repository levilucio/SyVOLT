

from core.himesis import Himesis

class HereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation, self).__init__(name='HereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation"""
        self["GUID__"] = 7460278131433738635
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4500961836254032784
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2066584626337015386
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2417711440559883145
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 641214243724413977
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2843361018908865980
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 8129393471477956071
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5587982218998391734
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4053223727306208923
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4938438607362154035
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4062559614697743149
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 5031928256469329240
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 528919349358282982
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3269206415893237683
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 3219134995710642288
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5826934488828178322
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 7599044613790909289
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 351858288972620787
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5324066289154334917
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 7836022325359525655
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8202199358083553367
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 7984462856600950343
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 837668182209400387
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 848375837428375045
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 5378070342143814506
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3539749039361463750
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7026598639553010168
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 2958696594442584324

