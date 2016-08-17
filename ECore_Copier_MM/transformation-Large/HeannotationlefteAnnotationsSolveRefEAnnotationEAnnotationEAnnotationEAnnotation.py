

from core.himesis import Himesis

class HeannotationlefteAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeannotationlefteAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeannotationlefteAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation, self).__init__(name='HeannotationlefteAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eannotationlefteAnnotationsSolveRefEAnnotationEAnnotationEAnnotationEAnnotation"""
        self["GUID__"] = 3778088013148362547
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2050475436945545404
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 111195935818549784
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3272894018156083157
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5578794074389394646
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 4672318323672063422
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 6272154298932608922
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 2010410563344941881
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 941203075791444923
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 6837523999441027625
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 328715322606086348
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 6149014608014252254
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 5841123160613974429
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 3458257375737646999
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 1752179935830964190
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 4889743664253718023
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 6419959474297311071
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 3923751652790568856
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 8293315245178951571
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 3199190349986213475
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 8819802271848690640
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 1632047668435590737
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 8448968828361545921
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 186702864469354800
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EAnnotation"""
        self.vs[23]["mm__"] = """EAnnotation"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 3555574934668659990
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EAnnotation"""
        self.vs[24]["mm__"] = """EAnnotation"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 1766445983752503823
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EAnnotation"""
        self.vs[25]["mm__"] = """EAnnotation"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 6006682320783437402
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EAnnotation"""
        self.vs[26]["mm__"] = """EAnnotation"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 801705180801751180

