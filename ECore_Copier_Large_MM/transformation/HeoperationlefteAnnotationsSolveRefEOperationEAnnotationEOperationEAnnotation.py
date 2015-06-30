

from core.himesis import Himesis

class HeoperationlefteAnnotationsSolveRefEOperationEAnnotationEOperationEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationlefteAnnotationsSolveRefEOperationEAnnotationEOperationEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationlefteAnnotationsSolveRefEOperationEAnnotationEOperationEAnnotation, self).__init__(name='HeoperationlefteAnnotationsSolveRefEOperationEAnnotationEOperationEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationlefteAnnotationsSolveRefEOperationEAnnotationEOperationEAnnotation"""
        self["GUID__"] = 5816395996192583717
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8044970359314201378
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1048396254969054700
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4558494274367220420
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2115966609539548178
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 1458168688512188010
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3498868833057656827
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 1307123802579665829
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5438034355437875093
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 347179529733664915
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2062346932891848348
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7369516320927345833
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8754100728367131831
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 7003937250653372044
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 1875949330034786489
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5523630539087955496
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2583131276534883053
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 1181219036459105099
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 1530653583095677969
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 40237161015443598
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 7359435342082954621
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 6720296362885197874
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7435363414672850123
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 206401628991295002
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3235173079800635441
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 7728551407519580789
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 98859355129756548
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6740085100061687672

