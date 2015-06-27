

from core.himesis import Himesis

class HBasicState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef, self).__init__(name='HBasicState2ProcDef', num_nodes=53, edges=[])
        
        # Add the edges
        self.add_edges([[8, 12], [12, 4], [4, 13], [13, 7], [7, 14], [14, 5], [29, 23], [23, 47], [30, 24], [24, 48], [31, 25], [25, 49], [32, 26], [26, 50], [33, 27], [27, 51], [34, 28], [28, 52], [7, 15], [15, 37], [5, 16], [16, 38], [8, 17], [17, 39], [4, 18], [18, 40], [3, 0], [0, 19], [0, 20], [0, 21], [0, 22], [6, 1], [1, 2], [2, 10], [10, 35], [2, 11], [11, 36], [9, 2], [6, 3], [20, 4], [22, 5], [29, 41], [30, 42], [31, 43], [32, 44], [33, 45], [34, 46], [19, 8], [21, 7], [8, 9], [41, 35], [42, 36], [43, 37], [44, 38], [45, 39], [46, 40]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = 8525836681255955941
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = 4165776204580979531
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = 761675179070702009
        self.vs[2]["name"] = """state1"""
        self.vs[2]["classtype"] = """State"""
        self.vs[2]["mm__"] = """State"""
        self.vs[2]["cardinality"] = """+"""
        self.vs[2]["GUID__"] = 8088169172056618593
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = 204235031184039220
        self.vs[4]["name"] = """listen1"""
        self.vs[4]["classtype"] = """Listen"""
        self.vs[4]["mm__"] = """Listen"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 6109874148419968718
        self.vs[5]["name"] = """triggerT1"""
        self.vs[5]["classtype"] = """Trigger_T"""
        self.vs[5]["mm__"] = """Trigger_T"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8537663124982216460
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = 3624612151048761973
        self.vs[7]["name"] = """listenbranch1"""
        self.vs[7]["classtype"] = """ListenBranch"""
        self.vs[7]["mm__"] = """ListenBranch"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 8134050433771539095
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5616958820576264020
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["GUID__"] = 7825935618795872861
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 1210863139480522005
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 6722137952565447414
        self.vs[12]["associationType"] = """p"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 7486476771521029684
        self.vs[13]["associationType"] = """branches"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = 1637799321920411080
        self.vs[14]["associationType"] = """p"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = 4073698587131039331
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8619365000023766722
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 3571463021479962905
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 504279484655809875
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 6859326992699408385
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 4614108943600654051
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 7229693712047415162
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 1611198130436134687
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 8622969388822719460
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 3535626402179004615
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 2761826174276947416
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 4415701548185711299
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = 3086136540291320049
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = 3995393775820911543
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 4124526192260432474
        self.vs[29]["name"] = """eq1"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = 5170141126968319744
        self.vs[30]["name"] = """eq2"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 450994506263513499
        self.vs[31]["name"] = """eq3"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = 9102076439848772466
        self.vs[32]["name"] = """eq4"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = 5322118659465219930
        self.vs[33]["name"] = """eq5"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = 6979930072231281578
        self.vs[34]["name"] = """eq6"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 7882404140603194677
        self.vs[35]["name"] = """isComposite"""
        self.vs[35]["Type"] = """'Bool'"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["GUID__"] = 1881848727588848346
        self.vs[36]["name"] = """hasOutgoingTransitions"""
        self.vs[36]["Type"] = """'Bool'"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["GUID__"] = 5227568023042720112
        self.vs[37]["name"] = """channel"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["GUID__"] = 1204013898487930896
        self.vs[38]["name"] = """channel"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["GUID__"] = 2168292903985405079
        self.vs[39]["name"] = """pivot"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["GUID__"] = 5554538517249505431
        self.vs[40]["name"] = """pivot"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["GUID__"] = 2714301674149879993
        self.vs[41]["mm__"] = """leftExpr"""
        self.vs[41]["GUID__"] = 738420713652842594
        self.vs[42]["mm__"] = """leftExpr"""
        self.vs[42]["GUID__"] = 5080129685971985518
        self.vs[43]["mm__"] = """leftExpr"""
        self.vs[43]["GUID__"] = 2493551741163191478
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = 6778484884671154853
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = 8945984260293129596
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = 9216555088932102827
        self.vs[47]["name"] = """false"""
        self.vs[47]["Type"] = """'Bool'"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["GUID__"] = 4285635979393714227
        self.vs[48]["name"] = """true"""
        self.vs[48]["Type"] = """'Bool'"""
        self.vs[48]["mm__"] = """Constant"""
        self.vs[48]["GUID__"] = 3596345801233172722
        self.vs[49]["name"] = """exit"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["GUID__"] = 851869635112614524
        self.vs[50]["name"] = """exack"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["mm__"] = """Constant"""
        self.vs[50]["GUID__"] = 663606201488962254
        self.vs[51]["name"] = """procdef"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["GUID__"] = 4665539004629923200
        self.vs[52]["name"] = """listensimplestate"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["GUID__"] = 6350657064421388151

