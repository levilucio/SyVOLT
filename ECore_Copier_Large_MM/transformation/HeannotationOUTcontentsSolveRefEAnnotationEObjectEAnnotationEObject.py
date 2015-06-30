

from core.himesis import Himesis

class HeannotationOUTcontentsSolveRefEAnnotationEObjectEAnnotationEObject(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeannotationOUTcontentsSolveRefEAnnotationEObjectEAnnotationEObject.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeannotationOUTcontentsSolveRefEAnnotationEObjectEAnnotationEObject, self).__init__(name='HeannotationOUTcontentsSolveRefEAnnotationEObjectEAnnotationEObject', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eannotationOUTcontentsSolveRefEAnnotationEObjectEAnnotationEObject"""
        self["GUID__"] = 8459852196827768809
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4513496662321916150
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8991578811319614758
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4569242313268715698
        self.vs[3]["associationType"] = """contents"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 1112441495339477987
        self.vs[4]["associationType"] = """contents"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 8638934958474597384
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAnnotation"""
        self.vs[5]["mm__"] = """EAnnotation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1263976938731960894
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4781134258347536384
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EObject"""
        self.vs[7]["mm__"] = """EObject"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3735792381478555737
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3763653197241778197
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAnnotation"""
        self.vs[9]["mm__"] = """EAnnotation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 3804282192511151928
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7321870568255341971
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EObject"""
        self.vs[11]["mm__"] = """EObject"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 5592110068218064100
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4026738340067507728
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7655527916891971692
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 3135637848291177388
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8636277663374249648
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4272289879689551518
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2275902440946493890
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 3261483613197208392
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8931855392501998726
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4491206980974696542
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4227806712091619904
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 5391291747819769391
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 5428072360408319782
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 4777535914057568354
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 9113896831603788135
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 1443199061138367963

