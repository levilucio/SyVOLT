

from core.himesis import Himesis

class HeenumliteralOUTeAnnotationsSolveRefEEnumLiteralEAnnotationEEnumLiteralEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeenumliteralOUTeAnnotationsSolveRefEEnumLiteralEAnnotationEEnumLiteralEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeenumliteralOUTeAnnotationsSolveRefEEnumLiteralEAnnotationEEnumLiteralEAnnotation, self).__init__(name='HeenumliteralOUTeAnnotationsSolveRefEEnumLiteralEAnnotationEEnumLiteralEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eenumliteralOUTeAnnotationsSolveRefEEnumLiteralEAnnotationEEnumLiteralEAnnotation"""
        self["GUID__"] = 1316979693516342952
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1593015404505172269
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2842595596334402712
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2784916252514360580
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 362586408815241077
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2794540704824389104
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EEnumLiteral"""
        self.vs[5]["mm__"] = """EEnumLiteral"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 9147740471573260288
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3836781123396929437
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1739617741798531354
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 192835347876015105
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EEnumLiteral"""
        self.vs[9]["mm__"] = """EEnumLiteral"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 5203477516651800122
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2980663816019969980
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 7978485837877825266
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 1242845286087331861
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6718493436482242599
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 8964708864525574284
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 5851388870439148712
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 429542388938316045
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 7729157785896268977
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4349808484587281238
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8450250736284441697
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5369389095578096318
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7974086640312895099
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 521935072128092954
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 9116852418007175681
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8804872282360614527
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 5941126387258410644
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 7121133936065230739

