

from core.himesis import Himesis

class HTransition2ListenBranch(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2ListenBranch.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2ListenBranch, self).__init__(name='HTransition2ListenBranch', num_nodes=55, edges=[])
        
        # Add the edges
        self.add_edges([[1, 14], [14, 8], [8, 15], [15, 4], [4, 16], [16, 9], [3, 10], [10, 6], [6, 11], [11, 7], [39, 34], [34, 30], [40, 35], [35, 31], [41, 36], [36, 51], [42, 37], [37, 32], [43, 38], [38, 33], [6, 17], [17, 52], [3, 18], [18, 53], [7, 19], [19, 54], [2, 0], [0, 23], [0, 24], [0, 25], [5, 26], [26, 1], [5, 27], [27, 8], [5, 28], [28, 9], [5, 29], [29, 4], [1, 20], [20, 49], [1, 21], [21, 50], [9, 22], [22, 51], [12, 1], [5, 2], [23, 3], [3, 12], [39, 44], [40, 45], [41, 46], [42, 47], [43, 48], [24, 6], [25, 7], [7, 13], [13, 8], [44, 49], [45, 50], [46, 52], [47, 53], [48, 54]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """Transition2ListenBranch"""
        self["GUID__"] = 5184987474563896728
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = 8149157110998739746
        self.vs[1]["name"] = """state1"""
        self.vs[1]["classtype"] = """State"""
        self.vs[1]["mm__"] = """State"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = 2196956704740365435
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4763186052526997229
        self.vs[3]["name"] = """listen1"""
        self.vs[3]["classtype"] = """Listen"""
        self.vs[3]["mm__"] = """Listen"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = 8944126039869618053
        self.vs[4]["name"] = """triggerS1"""
        self.vs[4]["classtype"] = """Trigger_S"""
        self.vs[4]["mm__"] = """Trigger_S"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 2927110859401985286
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = 1953951274571045254
        self.vs[6]["name"] = """listenBranch1"""
        self.vs[6]["classtype"] = """ListenBranch"""
        self.vs[6]["mm__"] = """ListenBranch"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8600339433141114875
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 8664856963478135098
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 4063092222345058752
        self.vs[9]["name"] = """signal1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7606441555155088962
        self.vs[10]["associationType"] = """branches"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 8744369292442153775
        self.vs[11]["associationType"] = """p"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 5367628784474211673
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = 2989537639080527786
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 4955191583932356097
        self.vs[14]["associationType"] = """outgoingTransitions"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = 2973019561932070733
        self.vs[15]["associationType"] = """triggers"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = 1530834202362252193
        self.vs[16]["associationType"] = """signal"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = 7333670852340135554
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 8960985163420563424
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 6508274637764687600
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 8458379788347878336
        self.vs[20]["mm__"] = """hasAttribute_S"""
        self.vs[20]["GUID__"] = 9220980264981177499
        self.vs[21]["mm__"] = """hasAttribute_S"""
        self.vs[21]["GUID__"] = 3604107907230036655
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = 7082079116332420588
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 5748563221380947690
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 6729098958346500583
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = 7849656981176756629
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 843209316348666190
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 6474919487301416062
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = 6119015526641431442
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = 4652366366110212173
        self.vs[30]["name"] = """false"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["GUID__"] = 4793745639114816231
        self.vs[31]["name"] = """true"""
        self.vs[31]["Type"] = """'Bool'"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["GUID__"] = 4015240516077430451
        self.vs[32]["name"] = """listensimplestate"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["GUID__"] = 2682142900797424581
        self.vs[33]["name"] = """instfortrans"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["GUID__"] = 1094679293021634783
        self.vs[34]["mm__"] = """rightExpr"""
        self.vs[34]["GUID__"] = 6408778812646695961
        self.vs[35]["mm__"] = """rightExpr"""
        self.vs[35]["GUID__"] = 1999132886648318812
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 4476882783670291046
        self.vs[37]["mm__"] = """rightExpr"""
        self.vs[37]["GUID__"] = 4074628782730772891
        self.vs[38]["mm__"] = """rightExpr"""
        self.vs[38]["GUID__"] = 7659714681327009747
        self.vs[39]["name"] = """eq1"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = 4884596254001935957
        self.vs[40]["name"] = """eq2"""
        self.vs[40]["mm__"] = """Equation"""
        self.vs[40]["GUID__"] = 3951415378151178480
        self.vs[41]["name"] = """eq3"""
        self.vs[41]["mm__"] = """Equation"""
        self.vs[41]["GUID__"] = 1902675590121246250
        self.vs[42]["name"] = """eq4"""
        self.vs[42]["mm__"] = """Equation"""
        self.vs[42]["GUID__"] = 7292223287641522681
        self.vs[43]["name"] = """eq5"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = 3239913063680988705
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = 3847142822360118286
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = 6803270872720096089
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = 1063736190311085706
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = 6410745223723560938
        self.vs[48]["mm__"] = """leftExpr"""
        self.vs[48]["GUID__"] = 6660040496842162484
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["GUID__"] = 4489177083772561844
        self.vs[50]["name"] = """hasOutgoingTransitions"""
        self.vs[50]["Type"] = """'Bool'"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["GUID__"] = 6300003509120619113
        self.vs[51]["name"] = """name"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["GUID__"] = 4112942812727010568
        self.vs[52]["name"] = """channel"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["GUID__"] = 4676131714463281385
        self.vs[53]["name"] = """pivot"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["mm__"] = """Attribute"""
        self.vs[53]["GUID__"] = 6003773386319958172
        self.vs[54]["name"] = """pivot"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["GUID__"] = 5858949537207068815

