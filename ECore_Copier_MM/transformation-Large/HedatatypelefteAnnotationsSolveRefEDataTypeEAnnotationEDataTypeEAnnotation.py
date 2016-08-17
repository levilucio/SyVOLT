

from core.himesis import Himesis

class HedatatypelefteAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HedatatypelefteAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HedatatypelefteAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation, self).__init__(name='HedatatypelefteAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """edatatypelefteAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation"""
        self["GUID__"] = 1243887299510101410
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 452596858350289194
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5678199606385288144
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4259561105607281531
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 6940100112008540272
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3626362631382221251
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EDataType"""
        self.vs[5]["mm__"] = """EDataType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 4880950124778275037
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 1844604349198765216
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2450830074723836560
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7660157175863132521
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EDataType"""
        self.vs[9]["mm__"] = """EDataType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 1056134911012817433
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6113382267961050054
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 206312796897776760
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3702307767148166506
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 3925020822589414663
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2061286100120302970
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2831797684364586805
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 5198731961797399558
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3039411046705591830
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 245533408478309528
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2241301550955796232
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 187351634523932468
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3952632101429380393
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 7871673988256564814
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6813184790004859873
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6419272907154405665
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 118889672033736517
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8922887118443887236

