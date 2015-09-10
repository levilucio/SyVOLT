

from core.himesis import Himesis

class HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier, self).__init__(name='HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier"""
        self["GUID__"] = 8388354868321727385
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4084694337272062892
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1430615135669444893
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7159358634142268211
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2606764010143288323
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2895883632797189536
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3129765175514033367
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 49167859930294970
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 8317975326449997667
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4157192163222768866
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6329546408351021242
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2821755111926358432
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 5145350553131565616
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2405311321128566724
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 823768535968311442
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5384328948113793969
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 3634820346672540033
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3556352336277837672
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 8388226191747536855
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4859481446745279322
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6024246869927291767
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2865375052003054693
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6454419334758396129
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 7559951973797049719
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 5510352597968353772
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3403792641369743298
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 8340035213366462221
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6487045433152311448

