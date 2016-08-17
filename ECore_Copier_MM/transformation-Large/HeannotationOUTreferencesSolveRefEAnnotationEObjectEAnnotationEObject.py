

from core.himesis import Himesis

class HeannotationOUTreferencesSolveRefEAnnotationEObjectEAnnotationEObject(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeannotationOUTreferencesSolveRefEAnnotationEObjectEAnnotationEObject.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeannotationOUTreferencesSolveRefEAnnotationEObjectEAnnotationEObject, self).__init__(name='HeannotationOUTreferencesSolveRefEAnnotationEObjectEAnnotationEObject', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eannotationOUTreferencesSolveRefEAnnotationEObjectEAnnotationEObject"""
        self["GUID__"] = 4106694662363054783
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7671712569517465753
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 150773625110346287
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7923383215505333528
        self.vs[3]["associationType"] = """references"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3395548786810933937
        self.vs[4]["associationType"] = """references"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2209428587144155752
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAnnotation"""
        self.vs[5]["mm__"] = """EAnnotation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5428621690944073542
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3683169434083065128
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EObject"""
        self.vs[7]["mm__"] = """EObject"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4455588895164780573
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3851266971843901910
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAnnotation"""
        self.vs[9]["mm__"] = """EAnnotation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6216892109226634956
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6823589513915680990
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EObject"""
        self.vs[11]["mm__"] = """EObject"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2204283541128779065
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6449327567515899387
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6095980137268263065
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6934740231615852705
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 3551444831029645500
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4221911134843097156
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 7028818947932950355
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 7109474444630748473
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 7983329174235714149
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 7901325331246282505
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5778927389151304066
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 7518750454318956054
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4881614548926067284
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1895532608346897857
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 6033870116359672458
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6118984482074658311

