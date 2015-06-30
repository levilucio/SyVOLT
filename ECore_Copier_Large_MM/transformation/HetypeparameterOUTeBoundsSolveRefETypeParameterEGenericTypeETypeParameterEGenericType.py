

from core.himesis import Himesis

class HetypeparameterOUTeBoundsSolveRefETypeParameterEGenericTypeETypeParameterEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HetypeparameterOUTeBoundsSolveRefETypeParameterEGenericTypeETypeParameterEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HetypeparameterOUTeBoundsSolveRefETypeParameterEGenericTypeETypeParameterEGenericType, self).__init__(name='HetypeparameterOUTeBoundsSolveRefETypeParameterEGenericTypeETypeParameterEGenericType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """etypeparameterOUTeBoundsSolveRefETypeParameterEGenericTypeETypeParameterEGenericType"""
        self["GUID__"] = 2043522540655997447
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5063742788303125985
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7538597220994146738
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1590528347517351420
        self.vs[3]["associationType"] = """eBounds"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 6837444956415320473
        self.vs[4]["associationType"] = """eBounds"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 5927939017554171348
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ETypeParameter"""
        self.vs[5]["mm__"] = """ETypeParameter"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3298587294958358675
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 227095453960209701
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EGenericType"""
        self.vs[7]["mm__"] = """EGenericType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4526671740311637763
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 1316641905058113764
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ETypeParameter"""
        self.vs[9]["mm__"] = """ETypeParameter"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 433948251282233016
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 8358214632634444368
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EGenericType"""
        self.vs[11]["mm__"] = """EGenericType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 1859229315964526790
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2271716477997746552
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 2085675732734689735
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 765268170256626965
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 4808870445740077391
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3699344733359546311
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5602522182082190583
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 8926113895294579176
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 9122097380799770615
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2432784644524003740
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6797373833401308961
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 4711770853746913385
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4104682702192222430
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3737794163354539837
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 6240736416142282914
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8048845989643242856

