

from core.himesis import Himesis

class HereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference, self).__init__(name='HereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference"""
        self["GUID__"] = 1680653252241126549
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8599027892599234228
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 525421361186797492
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8064502004876203458
        self.vs[3]["associationType"] = """eOpposite"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 8507671434255518083
        self.vs[4]["associationType"] = """eOpposite"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2937507821378036231
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 7098910161870395804
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 1115639604261024188
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 1192276399721910200
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 652368921971560198
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["GUID__"] = 790607413162888032
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["GUID__"] = 2019744839375441271
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 9082804814346474715
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = 3090686168143481215
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 11660772144309822
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 486686853913791151
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 1430716435473135847
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["GUID__"] = 8906447456909286230
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 9133874984160960651
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["GUID__"] = 5888246358658042416
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4741570653026729683
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 5142953401628514825
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 2703894519605350290
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["GUID__"] = 4200701000064636781
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EReference"""
        self.vs[23]["mm__"] = """EReference"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 7463717208226075088
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EReference"""
        self.vs[24]["mm__"] = """EReference"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 5428599403721263012
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EReference"""
        self.vs[25]["mm__"] = """EReference"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 7888164588756226514
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EReference"""
        self.vs[26]["mm__"] = """EReference"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 8124450405700971127

