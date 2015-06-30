

from core.himesis import Himesis

class HetypeparameterOUTeAnnotationsSolveRefETypeParameterEAnnotationETypeParameterEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HetypeparameterOUTeAnnotationsSolveRefETypeParameterEAnnotationETypeParameterEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HetypeparameterOUTeAnnotationsSolveRefETypeParameterEAnnotationETypeParameterEAnnotation, self).__init__(name='HetypeparameterOUTeAnnotationsSolveRefETypeParameterEAnnotationETypeParameterEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """etypeparameterOUTeAnnotationsSolveRefETypeParameterEAnnotationETypeParameterEAnnotation"""
        self["GUID__"] = 8719953264800390205
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4781894380701366369
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2436340639919981731
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7961903346498701025
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 1474427485867568633
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3898678985499802093
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ETypeParameter"""
        self.vs[5]["mm__"] = """ETypeParameter"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5680476667632226861
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5836632077703442891
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 419371687796964408
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 1630072987784785577
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ETypeParameter"""
        self.vs[9]["mm__"] = """ETypeParameter"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2752909184066623309
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6454295331177435782
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 1955568675135568297
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3487370564642592310
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 1269449602713302106
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2742190514587501761
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 4141375045405810566
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 751817918621507283
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5167620817878417421
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 109624947079681912
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8045607711106924959
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 3546978683772519194
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 9015754691574810337
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 5601514986625259341
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 1889122431213372689
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6197721983447186369
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 634157197573220751
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8315601313784272579

