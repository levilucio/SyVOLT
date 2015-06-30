

from core.himesis import Himesis

class HeannotationOUTeAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeannotationOUTeAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeannotationOUTeAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation, self).__init__(name='HeannotationOUTeAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eannotationOUTeAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation"""
        self["GUID__"] = 1419369890555458424
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4429715011281915959
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3242832673176857420
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3991246536544072476
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 6844567943126491089
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6208309255253200553
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 3450426451060586864
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 9025674610293987964
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 25897838045837848
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 6999968820446588537
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 595531717867263483
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 6866601825201050099
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 428619601718670114
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 3862059349729904650
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 4801542214695522518
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 4058055593815996237
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 7997050246001470165
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 2137004201682818843
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 1580629152919450194
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 1069827965430031842
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4236915078158938461
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 8936526415227042097
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 6960910467965559835
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 3954007698329942275
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EAnnotation"""
        self.vs[23]["mm__"] = """EAnnotation"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 7438356280624737130
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EAnnotation"""
        self.vs[24]["mm__"] = """EAnnotation"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 5608536765215063105
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EAnnotation"""
        self.vs[25]["mm__"] = """EAnnotation"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 8872833850057496378
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EAnnotation"""
        self.vs[26]["mm__"] = """EAnnotation"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 1763871728954838422

