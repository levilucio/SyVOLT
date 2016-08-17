

from core.himesis import Himesis

class HegenerictypeOUTeLowerBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HegenerictypeOUTeLowerBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HegenerictypeOUTeLowerBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType, self).__init__(name='HegenerictypeOUTeLowerBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """egenerictypeOUTeLowerBoundSolveRefEGenericTypeEGenericTypeEGenericTypeEGenericType"""
        self["GUID__"] = 7380862600974936012
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7485154533695625334
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1969531844659707924
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6008991890636758527
        self.vs[3]["associationType"] = """eLowerBound"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 540719805138281823
        self.vs[4]["associationType"] = """eLowerBound"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 8747503829556084465
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 3126181679237888399
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7023177719915721801
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 4801020647148677979
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 4275198470508125547
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 3955152868201076993
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 5372151841218836581
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 1197592777994160574
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 8005915504008783100
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 5423474303117667078
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 8663017697007024534
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 8442099846539107638
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 9133490392693075572
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 8282192555691844218
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 5050364985904732742
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 622989881821734037
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 4763656428700918925
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 2746910975607366727
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 5228819618744150492
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EGenericType"""
        self.vs[23]["mm__"] = """EGenericType"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 27505543290748781
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EGenericType"""
        self.vs[24]["mm__"] = """EGenericType"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 3046227073477110587
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EGenericType"""
        self.vs[25]["mm__"] = """EGenericType"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 271579848256792015
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EGenericType"""
        self.vs[26]["mm__"] = """EGenericType"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 6521945753432813082

