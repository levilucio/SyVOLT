

from core.himesis import Himesis

class HeannotationOUTeModelElementSolveRefEAnnotationEModelElementEAnnotationEModelElement(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeannotationOUTeModelElementSolveRefEAnnotationEModelElementEAnnotationEModelElement.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeannotationOUTeModelElementSolveRefEAnnotationEModelElementEAnnotationEModelElement, self).__init__(name='HeannotationOUTeModelElementSolveRefEAnnotationEModelElementEAnnotationEModelElement', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eannotationOUTeModelElementSolveRefEAnnotationEModelElementEAnnotationEModelElement"""
        self["GUID__"] = 2855660611818197509
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 607676573314735679
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 592725244774539553
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4920166639626068788
        self.vs[3]["associationType"] = """eModelElement"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 831096199314199592
        self.vs[4]["associationType"] = """eModelElement"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 8435470170930949071
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAnnotation"""
        self.vs[5]["mm__"] = """EAnnotation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 4004107775108259324
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4198482030454514553
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EModelElement"""
        self.vs[7]["mm__"] = """EModelElement"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 9181186673601218491
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 737454621671213959
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EAnnotation"""
        self.vs[9]["mm__"] = """EAnnotation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4595151994442179981
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2804698173079114560
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EModelElement"""
        self.vs[11]["mm__"] = """EModelElement"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 549177142027610602
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 8697402874447184893
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6032497319711719885
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4683399963960258013
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 9169305039988847154
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 9113707655982182824
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6100508646676596116
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 8006862576742284418
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 3165988237496271368
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2721208758214515214
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5712907939807110736
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 6569307275291640379
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3783276916536859912
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1754334493694591762
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 6974247349017668387
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 5884354215135176500

