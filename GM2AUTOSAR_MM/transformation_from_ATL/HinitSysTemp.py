

from core.himesis import Himesis

class HinitSysTemp(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HinitSysTemp.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HinitSysTemp, self).__init__(name='HinitSysTemp', num_nodes=101, edges=[])
        
        # Add the edges
        self.add_edges([[0, 14], [14, 3], [0, 15], [15, 4], [0, 16], [16, 5], [1, 20], [20, 6], [1, 21], [21, 7], [1, 22], [22, 8], [1, 23], [23, 9], [1, 24], [24, 10], [3, 12], [12, 4], [4, 13], [13, 5], [7, 17], [17, 6], [7, 18], [18, 8], [8, 19], [19, 9], [3, 11], [11, 90], [6, 30], [30, 91], [31, 32], [32, 91], [31, 33], [25, 34], [34, 36], [25, 35], [35, 90], [33, 25], [6, 37], [37, 92], [38, 39], [39, 92], [38, 40], [40, 41], [7, 42], [42, 93], [43, 44], [44, 93], [43, 45], [26, 46], [46, 48], [26, 47], [47, 90], [45, 26], [7, 49], [49, 94], [50, 51], [51, 94], [50, 52], [52, 53], [8, 54], [54, 95], [55, 56], [56, 95], [55, 57], [27, 58], [58, 60], [27, 59], [59, 90], [57, 27], [8, 61], [61, 96], [62, 63], [63, 96], [62, 64], [64, 65], [9, 66], [66, 97], [67, 68], [68, 97], [67, 69], [28, 70], [70, 72], [28, 71], [71, 90], [69, 28], [9, 73], [73, 98], [74, 75], [75, 98], [74, 76], [76, 77], [10, 78], [78, 99], [79, 80], [80, 99], [79, 81], [29, 82], [82, 84], [29, 83], [83, 90], [81, 29], [10, 85], [85, 100], [86, 87], [87, 100], [86, 88], [88, 89], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """initSysTemp"""
        self["GUID__"] = 6017098026413879491
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5650140504996248247
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6319616156922497193
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6436844163736149590
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4539150919730083327
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 3285011214173514571
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Module"""
        self.vs[5]["mm__"] = """Module"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8058824351991930052
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """SystemMapping"""
        self.vs[6]["mm__"] = """SystemMapping"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 1651692768430182583
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """System"""
        self.vs[7]["mm__"] = """System"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 6763094272528514700
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """SoftwareComposition"""
        self.vs[8]["mm__"] = """SoftwareComposition"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 4971264708343128002
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """CompositionType"""
        self.vs[9]["mm__"] = """CompositionType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 3141445283108653213
        self.vs[10]["name"] = """"""
        self.vs[10]["classtype"] = """EcuInstance"""
        self.vs[10]["mm__"] = """EcuInstance"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 9032961083522853916
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 4556735073833906759
        self.vs[12]["associationType"] = """partition"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 285325655646467050
        self.vs[13]["associationType"] = """module"""
        self.vs[13]["mm__"] = """directLink_S"""
        self.vs[13]["GUID__"] = 8242059632463443207
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 2883953680507117715
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 1898819519167736847
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 5151251121226757147
        self.vs[17]["associationType"] = """mapping"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 8786334663894993169
        self.vs[18]["associationType"] = """softwareComposition"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = 683365307796392972
        self.vs[19]["associationType"] = """softwareComposition"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = 1501734342982717467
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 6279552700075184270
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 7153356092981058842
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 7471902788304705786
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 1702621935874906404
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 2068031773938435883
        self.vs[25]["name"] = """Concat31"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 7422005489354383643
        self.vs[26]["name"] = """Concat46"""
        self.vs[26]["mm__"] = """Concat"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 3041606968040175266
        self.vs[27]["name"] = """Concat61"""
        self.vs[27]["mm__"] = """Concat"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 4834165754815195778
        self.vs[28]["name"] = """Concat76"""
        self.vs[28]["mm__"] = """Concat"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 602895499441875279
        self.vs[29]["name"] = """Concat91"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 2681739341457190995
        self.vs[30]["mm__"] = """hasAttribute_T"""
        self.vs[30]["GUID__"] = 8844763700840808765
        self.vs[31]["name"] = """eq_"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = 3581155918458220013
        self.vs[32]["mm__"] = """leftExpr"""
        self.vs[32]["GUID__"] = 5192314239478346402
        self.vs[33]["mm__"] = """rightExpr"""
        self.vs[33]["GUID__"] = 8062259701961983348
        self.vs[34]["mm__"] = """hasArgs"""
        self.vs[34]["GUID__"] = 8150473652551950104
        self.vs[35]["mm__"] = """hasArgs"""
        self.vs[35]["GUID__"] = 6890597444347843891
        self.vs[36]["name"] = """SysMapping_"""
        self.vs[36]["mm__"] = """Constant"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 4432630855151475468
        self.vs[37]["mm__"] = """hasAttribute_T"""
        self.vs[37]["GUID__"] = 1474993919379046780
        self.vs[38]["name"] = """eq_"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = 1143680355983720575
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = 2533927322873409743
        self.vs[40]["mm__"] = """rightExpr"""
        self.vs[40]["GUID__"] = 6086652361182616424
        self.vs[41]["name"] = """solveRef"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 4950205285682009875
        self.vs[42]["mm__"] = """hasAttribute_T"""
        self.vs[42]["GUID__"] = 7714348979341382739
        self.vs[43]["name"] = """eq_"""
        self.vs[43]["mm__"] = """Equation"""
        self.vs[43]["GUID__"] = 7885532965444518626
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = 6980198823676586131
        self.vs[45]["mm__"] = """rightExpr"""
        self.vs[45]["GUID__"] = 7204702170851850573
        self.vs[46]["mm__"] = """hasArgs"""
        self.vs[46]["GUID__"] = 581892285309489347
        self.vs[47]["mm__"] = """hasArgs"""
        self.vs[47]["GUID__"] = 5059707442800016053
        self.vs[48]["name"] = """SysTemplate_"""
        self.vs[48]["mm__"] = """Constant"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = 8798431616108992241
        self.vs[49]["mm__"] = """hasAttribute_T"""
        self.vs[49]["GUID__"] = 447053881184379639
        self.vs[50]["name"] = """eq_"""
        self.vs[50]["mm__"] = """Equation"""
        self.vs[50]["GUID__"] = 4060287384689853908
        self.vs[51]["mm__"] = """leftExpr"""
        self.vs[51]["GUID__"] = 2372427856051427316
        self.vs[52]["mm__"] = """rightExpr"""
        self.vs[52]["GUID__"] = 8683973512563876895
        self.vs[53]["name"] = """solveRef"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'String'"""
        self.vs[53]["GUID__"] = 4698708002130038450
        self.vs[54]["mm__"] = """hasAttribute_T"""
        self.vs[54]["GUID__"] = 4025784187931126411
        self.vs[55]["name"] = """eq_"""
        self.vs[55]["mm__"] = """Equation"""
        self.vs[55]["GUID__"] = 3123582668223909498
        self.vs[56]["mm__"] = """leftExpr"""
        self.vs[56]["GUID__"] = 715232399660732637
        self.vs[57]["mm__"] = """rightExpr"""
        self.vs[57]["GUID__"] = 3422883875264583136
        self.vs[58]["mm__"] = """hasArgs"""
        self.vs[58]["GUID__"] = 2869673311565420874
        self.vs[59]["mm__"] = """hasArgs"""
        self.vs[59]["GUID__"] = 1205250633025800294
        self.vs[60]["name"] = """SoftwareComposition_"""
        self.vs[60]["mm__"] = """Constant"""
        self.vs[60]["Type"] = """'String'"""
        self.vs[60]["GUID__"] = 7721340737643978758
        self.vs[61]["mm__"] = """hasAttribute_T"""
        self.vs[61]["GUID__"] = 3092084270105677598
        self.vs[62]["name"] = """eq_"""
        self.vs[62]["mm__"] = """Equation"""
        self.vs[62]["GUID__"] = 1389434681041456321
        self.vs[63]["mm__"] = """leftExpr"""
        self.vs[63]["GUID__"] = 6957961422126400496
        self.vs[64]["mm__"] = """rightExpr"""
        self.vs[64]["GUID__"] = 8739409107926613916
        self.vs[65]["name"] = """solveRef"""
        self.vs[65]["mm__"] = """Constant"""
        self.vs[65]["Type"] = """'String'"""
        self.vs[65]["GUID__"] = 1380796134599664911
        self.vs[66]["mm__"] = """hasAttribute_T"""
        self.vs[66]["GUID__"] = 4088879545079336901
        self.vs[67]["name"] = """eq_"""
        self.vs[67]["mm__"] = """Equation"""
        self.vs[67]["GUID__"] = 6811636263654341538
        self.vs[68]["mm__"] = """leftExpr"""
        self.vs[68]["GUID__"] = 5005944643527364951
        self.vs[69]["mm__"] = """rightExpr"""
        self.vs[69]["GUID__"] = 6656152057917534578
        self.vs[70]["mm__"] = """hasArgs"""
        self.vs[70]["GUID__"] = 7191484230383398100
        self.vs[71]["mm__"] = """hasArgs"""
        self.vs[71]["GUID__"] = 7300807129991640267
        self.vs[72]["name"] = """CompositionType_"""
        self.vs[72]["mm__"] = """Constant"""
        self.vs[72]["Type"] = """'String'"""
        self.vs[72]["GUID__"] = 5720036211723014019
        self.vs[73]["mm__"] = """hasAttribute_T"""
        self.vs[73]["GUID__"] = 3740879867921427517
        self.vs[74]["name"] = """eq_"""
        self.vs[74]["mm__"] = """Equation"""
        self.vs[74]["GUID__"] = 7670303422450087703
        self.vs[75]["mm__"] = """leftExpr"""
        self.vs[75]["GUID__"] = 6460474629531978584
        self.vs[76]["mm__"] = """rightExpr"""
        self.vs[76]["GUID__"] = 6737701532103619383
        self.vs[77]["name"] = """solveRef"""
        self.vs[77]["mm__"] = """Constant"""
        self.vs[77]["Type"] = """'String'"""
        self.vs[77]["GUID__"] = 2025121386127475781
        self.vs[78]["mm__"] = """hasAttribute_T"""
        self.vs[78]["GUID__"] = 1567406153526413846
        self.vs[79]["name"] = """eq_"""
        self.vs[79]["mm__"] = """Equation"""
        self.vs[79]["GUID__"] = 2448194491867054766
        self.vs[80]["mm__"] = """leftExpr"""
        self.vs[80]["GUID__"] = 1778648587606633829
        self.vs[81]["mm__"] = """rightExpr"""
        self.vs[81]["GUID__"] = 1645608438091411007
        self.vs[82]["mm__"] = """hasArgs"""
        self.vs[82]["GUID__"] = 8880739884109494820
        self.vs[83]["mm__"] = """hasArgs"""
        self.vs[83]["GUID__"] = 614166154483862329
        self.vs[84]["name"] = """EcuInstance_"""
        self.vs[84]["mm__"] = """Constant"""
        self.vs[84]["Type"] = """'String'"""
        self.vs[84]["GUID__"] = 8500807068209599045
        self.vs[85]["mm__"] = """hasAttribute_T"""
        self.vs[85]["GUID__"] = 8892888145723215923
        self.vs[86]["name"] = """eq_"""
        self.vs[86]["mm__"] = """Equation"""
        self.vs[86]["GUID__"] = 9046272851244580639
        self.vs[87]["mm__"] = """leftExpr"""
        self.vs[87]["GUID__"] = 6384856933779487782
        self.vs[88]["mm__"] = """rightExpr"""
        self.vs[88]["GUID__"] = 7538916061652866840
        self.vs[89]["name"] = """solveRef"""
        self.vs[89]["mm__"] = """Constant"""
        self.vs[89]["Type"] = """'String'"""
        self.vs[89]["GUID__"] = 5815820522440220424
        self.vs[90]["name"] = """name"""
        self.vs[90]["mm__"] = """Attribute"""
        self.vs[90]["Type"] = """'String'"""
        self.vs[90]["GUID__"] = 551898534832851338
        self.vs[91]["name"] = """shortName"""
        self.vs[91]["mm__"] = """Attribute"""
        self.vs[91]["Type"] = """'String'"""
        self.vs[91]["GUID__"] = 4957064639318291773
        self.vs[92]["name"] = """ApplyAttribute"""
        self.vs[92]["mm__"] = """Attribute"""
        self.vs[92]["Type"] = """'String'"""
        self.vs[92]["GUID__"] = 2196572298710769910
        self.vs[93]["name"] = """shortName"""
        self.vs[93]["mm__"] = """Attribute"""
        self.vs[93]["Type"] = """'String'"""
        self.vs[93]["GUID__"] = 7093211276994620749
        self.vs[94]["name"] = """ApplyAttribute"""
        self.vs[94]["mm__"] = """Attribute"""
        self.vs[94]["Type"] = """'String'"""
        self.vs[94]["GUID__"] = 1121374351051483462
        self.vs[95]["name"] = """shortName"""
        self.vs[95]["mm__"] = """Attribute"""
        self.vs[95]["Type"] = """'String'"""
        self.vs[95]["GUID__"] = 3777831018012230179
        self.vs[96]["name"] = """ApplyAttribute"""
        self.vs[96]["mm__"] = """Attribute"""
        self.vs[96]["Type"] = """'String'"""
        self.vs[96]["GUID__"] = 2109256916075447320
        self.vs[97]["name"] = """shortName"""
        self.vs[97]["mm__"] = """Attribute"""
        self.vs[97]["Type"] = """'String'"""
        self.vs[97]["GUID__"] = 4224318856397822124
        self.vs[98]["name"] = """ApplyAttribute"""
        self.vs[98]["mm__"] = """Attribute"""
        self.vs[98]["Type"] = """'String'"""
        self.vs[98]["GUID__"] = 4469975850831694097
        self.vs[99]["name"] = """shortName"""
        self.vs[99]["mm__"] = """Attribute"""
        self.vs[99]["Type"] = """'String'"""
        self.vs[99]["GUID__"] = 2832100905731223166
        self.vs[100]["name"] = """ApplyAttribute"""
        self.vs[100]["mm__"] = """Attribute"""
        self.vs[100]["Type"] = """'String'"""
        self.vs[100]["GUID__"] = 295148868490434377

