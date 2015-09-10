

from core.himesis import Himesis

class HeclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation, self).__init__(name='HeclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation"""
        self["GUID__"] = 3359169346285675343
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7887258420814325909
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4876210931247030698
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3828508891451029712
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2279121756029123257
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 8220687171121145140
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EClass"""
        self.vs[5]["mm__"] = """EClass"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 6722921119834000387
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6153591746993615678
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5140187824407477268
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 14462926987790403
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EClass"""
        self.vs[9]["mm__"] = """EClass"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8412127038050386242
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1308188530631913943
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 819139986920812810
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6940200293281621228
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 5132026138373793822
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 1625378267323985052
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2484125233189919059
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8841972117525129100
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4099804589635285883
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4077417574605430779
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 3326965727069273580
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 1794592588659178158
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 1100339077608453243
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 7898186002199725379
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4786459792079337838
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 7374890872715653893
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 5363247889309388489
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 2666800595952132634

