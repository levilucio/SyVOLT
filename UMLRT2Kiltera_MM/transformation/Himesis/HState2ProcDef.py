

from core.himesis import Himesis

class HState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2ProcDef, self).__init__(name='HState2ProcDef', num_nodes=51, edges=[])
        
        # Add the edges
        self.add_edges([[6, 10], [10, 13], [6, 11], [11, 14], [6, 12], [12, 15], [30, 20], [20, 7], [31, 21], [21, 41], [32, 22], [22, 42], [33, 23], [23, 43], [34, 24], [24, 44], [6, 25], [25, 46], [13, 26], [26, 47], [14, 27], [27, 48], [15, 28], [28, 49], [6, 29], [29, 50], [4, 0], [0, 16], [0, 17], [0, 18], [0, 19], [7, 8], [8, 40], [7, 9], [9, 45], [5, 1], [1, 3], [3, 2], [2, 45], [5, 4], [30, 35], [31, 36], [32, 37], [33, 38], [34, 39], [16, 6], [17, 13], [18, 14], [19, 15], [35, 46], [36, 47], [37, 48], [38, 49], [39, 50]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """State2ProcDef"""
        self["GUID__"] = 5868154402058820660
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = 6023735636777289509
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = 8249591039908396085
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = 2248556881169590401
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 5753169759945980110
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = 1776044080255211063
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = 8480124852550724146
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8658492048813039277
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = 5237970348482896147
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = 2000006070180197766
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = 5261022733864461102
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 5384803648272409178
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 1899304831058892044
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 6071979344604623639
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = 8691475669695461642
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = 4271267063983213581
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = 2006372584879936667
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = 6884994521218670441
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 2790615513193465114
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 1995529773240575337
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 8970793545929849146
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 4520931377827821516
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 8359981838105396676
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 2639583176318113407
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 1071929417013884259
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 2043100431761228224
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 3091295137094457672
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = 2841188093962773166
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = 1458859885407251894
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = 1371618169950527677
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 881401249667185146
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 5354834592482843134
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = 4978433724172629925
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = 2360051415754966850
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = 4477895697036208526
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 6336243887300545169
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 7266875998136793308
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = 3567123816839899785
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = 843578483414704084
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = 2076757302587087147
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = 983848495269315121
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 8102546740561233250
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 7647877458866108495
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 5186084713309088805
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 7882385690562791281
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 8087043863430461793
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 7647347847094829842
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 3897461793064659294
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 2884341870650841214
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = 7452482164085726276
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = 648994299097011304
        self.vs[50]["name"] = """pivot"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = 6835665445598761227

