

from core.himesis import Himesis

class HeoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter, self).__init__(name='HeoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter"""
        self["GUID__"] = 4996462937418951956
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4835940878548779618
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3821481946137937030
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6733203573050651647
        self.vs[3]["associationType"] = """eParameters"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5415770231607207730
        self.vs[4]["associationType"] = """eParameters"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6387857876437389622
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5779474568683368155
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7372663741506684419
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EParameter"""
        self.vs[7]["mm__"] = """EParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4141153908853641257
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 2916057956725805572
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 5748671792784341513
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 604271002314869306
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EParameter"""
        self.vs[11]["mm__"] = """EParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 7188739353087150915
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 8649287468393655511
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 1957512640843314683
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 8972012841969148035
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2422993504054084811
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 2097220440925128456
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5136034511718424013
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6650180939269945721
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 4534986109565133489
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 276413947143916503
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5971109757015921547
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 4181477818678350085
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6473711901848666778
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6370965259852542841
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 4688243561529406417
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 626580702204497035

