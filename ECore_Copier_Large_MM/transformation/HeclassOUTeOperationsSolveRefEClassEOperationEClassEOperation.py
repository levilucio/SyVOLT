

from core.himesis import Himesis

class HeclassOUTeOperationsSolveRefEClassEOperationEClassEOperation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclassOUTeOperationsSolveRefEClassEOperationEClassEOperation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclassOUTeOperationsSolveRefEClassEOperationEClassEOperation, self).__init__(name='HeclassOUTeOperationsSolveRefEClassEOperationEClassEOperation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclassOUTeOperationsSolveRefEClassEOperationEClassEOperation"""
        self["GUID__"] = 1978634013385514902
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2517532533648662885
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1376281682252862235
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6597778609308859427
        self.vs[3]["associationType"] = """eOperations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 951748661951976089
        self.vs[4]["associationType"] = """eOperations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 4991072133922880865
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EClass"""
        self.vs[5]["mm__"] = """EClass"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 6120985007253492729
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7251367458087575278
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EOperation"""
        self.vs[7]["mm__"] = """EOperation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7154449097454651421
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 2041339595589821480
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EClass"""
        self.vs[9]["mm__"] = """EClass"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 5987017436268474592
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 8797509015852127828
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EOperation"""
        self.vs[11]["mm__"] = """EOperation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 1204046274037994408
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2310104955353223654
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6376438141223773572
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2522384603297663574
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8539777213793394590
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 510717554956897733
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3417960432796638183
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6889083972618139998
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 755211839417180077
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5388846640980110718
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 8146402503070924045
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2585667424221604689
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 8423814483472754989
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1480124650021406173
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 53308935682951260
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 684516318178810309

