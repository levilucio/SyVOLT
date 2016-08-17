

from core.himesis import Himesis

class HeattributelefteAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeattributelefteAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeattributelefteAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation, self).__init__(name='HeattributelefteAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eattributelefteAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation"""
        self["GUID__"] = 3278098437533437088
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3339471094173398571
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2621678561196524974
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2645714254491546873
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2507757732832146707
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 4747946609322870606
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAttribute"""
        self.vs[5]["mm__"] = """EAttribute"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1088235891408015371
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7784093840446634972
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5423992361002373772
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6037534563815099286
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAttribute"""
        self.vs[9]["mm__"] = """EAttribute"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 3637230438431112063
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1111894234524683493
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8997901468576828296
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 8683062091009577251
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7173489911769387838
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6987951316168233343
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 6604245890079757503
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 6409562530396104514
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4558419661807481669
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 261903470056327783
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8225033802259546054
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2963673742725924206
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 879816634802765785
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 3197373689472796460
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 2529401861463259796
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 2107858840182794516
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7444477850823502820
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 5468455959818152391

