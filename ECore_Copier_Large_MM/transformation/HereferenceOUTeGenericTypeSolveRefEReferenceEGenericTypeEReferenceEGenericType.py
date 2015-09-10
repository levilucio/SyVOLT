

from core.himesis import Himesis

class HereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType, self).__init__(name='HereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType"""
        self["GUID__"] = 4155983781036593475
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3880085856439821049
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9081712227334382903
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3307931872126582102
        self.vs[3]["associationType"] = """eGenericType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 8063115179620184848
        self.vs[4]["associationType"] = """eGenericType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 1007036473195030496
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5278343529961602348
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7356432744091521881
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EGenericType"""
        self.vs[7]["mm__"] = """EGenericType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7257389347221334491
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4834665025365411083
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7170051592656914476
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6919182284072259447
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EGenericType"""
        self.vs[11]["mm__"] = """EGenericType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 5873993621362459345
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2903536962750585145
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7069848863240515581
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 7372017637490797662
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 1433993274315091521
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 735591487972836552
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 417880400820924351
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4176342339252035166
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1767634180366919004
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4707884472661482752
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 9035274664863575638
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 1138363122502836866
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 5229208194972737604
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1699528761846105690
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7774096428454943707
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 1919098360369949554

