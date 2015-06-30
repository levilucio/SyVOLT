

from core.himesis import Himesis

class HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter, self).__init__(name='HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter"""
        self["GUID__"] = 4629300704248250363
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6535403694973183705
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 734441392837783268
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2854530901101042958
        self.vs[3]["associationType"] = """eParameters"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 4715348912612923025
        self.vs[4]["associationType"] = """eParameters"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 650593392692477023
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EOperation"""
        self.vs[5]["mm__"] = """EOperation"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5382801748129539798
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 8449818931772187001
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EParameter"""
        self.vs[7]["mm__"] = """EParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1969180631687423378
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4111988676987472015
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EOperation"""
        self.vs[9]["mm__"] = """EOperation"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4309530224598352215
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2315046708658562405
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EParameter"""
        self.vs[11]["mm__"] = """EParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 432964688674994357
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 62405196789205197
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6142732580537168672
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2217517468120260905
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 1296501878371837600
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 77393555926575159
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5635382720612409784
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6618246301604674962
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1302514106757690703
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 6603226318631964911
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4043955891759020975
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 8337869973333530215
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3305498590197872270
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8722464311790405343
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 1032874868394122435
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6252886210167658643

