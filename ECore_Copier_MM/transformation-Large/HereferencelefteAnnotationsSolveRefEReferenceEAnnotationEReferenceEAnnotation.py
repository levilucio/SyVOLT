

from core.himesis import Himesis

class HereferencelefteAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferencelefteAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferencelefteAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation, self).__init__(name='HereferencelefteAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferencelefteAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation"""
        self["GUID__"] = 945651455592695730
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3461444016222556918
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 591266871495432564
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6428663618161820362
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 7204839478505758470
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 7248690594362623999
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2525147047570684448
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4772201853530768545
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 8239332070027134445
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 1781916284026865746
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6342166957570240184
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7038186003534017465
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 1429599319350449261
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 8904331269806508265
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 2841555729777372190
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 619949822745332614
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2345669654314626473
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 2912771905006154331
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 7721029253510731899
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6958092181398942321
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6119055628067488720
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 961084947980471983
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3052505215910782303
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 5220945689969560218
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 562798116828923943
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6205911910109049247
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 3532302778268842330
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6510131383530369278

