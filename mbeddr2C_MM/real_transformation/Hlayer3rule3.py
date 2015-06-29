

from core.himesis import Himesis

class Hlayer3rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer3rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule3, self).__init__(name='Hlayer3rule3', num_nodes=62, edges=[])
        
        # Add the edges
        self.add_edges([[0, 46], [46, 15], [0, 47], [47, 3], [0, 48], [48, 4], [0, 49], [49, 5], [0, 50], [50, 6], [0, 51], [51, 7], [1, 28], [28, 16], [1, 29], [29, 8], [1, 30], [30, 9], [1, 31], [31, 10], [15, 36], [36, 3], [3, 37], [37, 4], [4, 38], [38, 5], [5, 39], [39, 6], [6, 40], [40, 7], [16, 19], [19, 8], [8, 20], [20, 10], [10, 21], [21, 9], [16, 17], [17, 15], [9, 18], [18, 7], [15, 22], [22, 32], [4, 23], [23, 33], [7, 24], [24, 34], [8, 11], [11, 35], [12, 13], [13, 35], [12, 14], [45, 60], [60, 34], [45, 61], [61, 27], [44, 58], [58, 26], [44, 59], [59, 45], [43, 56], [56, 33], [43, 57], [57, 44], [42, 54], [54, 25], [42, 55], [55, 43], [41, 52], [52, 32], [41, 53], [53, 42], [14, 41], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer3rule3"""
        self["GUID__"] = 4780198711794350442
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3101382154954667321
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5007955445597958422
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 753440428593269190
        self.vs[3]["name"] = """layer3rule3class1"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7706986584708466277
        self.vs[4]["name"] = """layer3rule3class2"""
        self.vs[4]["classtype"] = """ComponentInstance"""
        self.vs[4]["mm__"] = """ComponentInstance"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 5389605540974944234
        self.vs[5]["name"] = """layer3rule3class3"""
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1959584029855056101
        self.vs[6]["name"] = """layer3rule3class4"""
        self.vs[6]["classtype"] = """ProvidedPort"""
        self.vs[6]["mm__"] = """ProvidedPort"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 2991040779960777481
        self.vs[7]["name"] = """layer3rule3class5"""
        self.vs[7]["classtype"] = """ClientServerInterface"""
        self.vs[7]["mm__"] = """ClientServerInterface"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5711480361286484068
        self.vs[8]["name"] = """layer3rule3class7"""
        self.vs[8]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[8]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 3006611179629207988
        self.vs[9]["name"] = """layer3rule3class8"""
        self.vs[9]["classtype"] = """TypeDef"""
        self.vs[9]["mm__"] = """TypeDef"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8635833156451077967
        self.vs[10]["name"] = """layer3rule3class9"""
        self.vs[10]["classtype"] = """TypeDefType"""
        self.vs[10]["mm__"] = """TypeDefType"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 7640926579529260393
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 2709924637053806186
        self.vs[12]["name"] = """eq_"""
        self.vs[12]["mm__"] = """Equation"""
        self.vs[12]["GUID__"] = 5995065665529161052
        self.vs[13]["mm__"] = """leftExpr"""
        self.vs[13]["GUID__"] = 3639959955702701857
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 8645514775411408364
        self.vs[15]["name"] = """layer3rule3class0"""
        self.vs[15]["classtype"] = """ImplementationModule"""
        self.vs[15]["mm__"] = """ImplementationModule"""
        self.vs[15]["cardinality"] = """+"""
        self.vs[15]["GUID__"] = 5035652146599792797
        self.vs[16]["name"] = """layer3rule3class6"""
        self.vs[16]["classtype"] = """ImplementationModule"""
        self.vs[16]["mm__"] = """ImplementationModule"""
        self.vs[16]["cardinality"] = """1"""
        self.vs[16]["GUID__"] = 5720362238657072413
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["GUID__"] = 5385306454088359250
        self.vs[18]["mm__"] = """backward_link"""
        self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["GUID__"] = 3619539212367724755
        self.vs[19]["associationType"] = """contents"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = 5295149113687797985
        self.vs[20]["associationType"] = """type"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = 1216376656660052331
        self.vs[21]["associationType"] = """typeDef"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = 4952904614257260332
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = 1600652482334227197
        self.vs[23]["mm__"] = """hasAttribute_S"""
        self.vs[23]["GUID__"] = 7964981285695272822
        self.vs[24]["mm__"] = """hasAttribute_S"""
        self.vs[24]["GUID__"] = 6258993700427060409
        self.vs[25]["name"] = """_"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["GUID__"] = 3121007579936409381
        self.vs[26]["name"] = """_"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6354037962563037902
        self.vs[27]["name"] = """__ops"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 1422319906167846086
        self.vs[28]["mm__"] = """apply_contains"""
        self.vs[28]["GUID__"] = 2348884809932016307
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = 1815007377035251938
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = 6297247554835341419
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = 173309260632495564
        self.vs[32]["name"] = """name"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["GUID__"] = 4594342212182124634
        self.vs[33]["name"] = """name"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["GUID__"] = 8290118007964424748
        self.vs[34]["name"] = """name"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["GUID__"] = 3651226980253001193
        self.vs[35]["name"] = """name"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["GUID__"] = 7492706273114963306
        self.vs[36]["associationType"] = """contents"""
        self.vs[36]["mm__"] = """directLink_S"""
        self.vs[36]["GUID__"] = 3934220924957117655
        self.vs[37]["associationType"] = """contents"""
        self.vs[37]["mm__"] = """directLink_S"""
        self.vs[37]["GUID__"] = 8179865885723024745
        self.vs[38]["associationType"] = """component"""
        self.vs[38]["mm__"] = """directLink_S"""
        self.vs[38]["GUID__"] = 5800294334072116611
        self.vs[39]["associationType"] = """contents"""
        self.vs[39]["mm__"] = """directLink_S"""
        self.vs[39]["GUID__"] = 5185096623970089735
        self.vs[40]["associationType"] = """intf"""
        self.vs[40]["mm__"] = """directLink_S"""
        self.vs[40]["GUID__"] = 8652580153737744936
        self.vs[41]["name"] = """Concatlayer3rule3class7attribute044"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["mm__"] = """Concat"""
        self.vs[41]["GUID__"] = 5289441725216714612
        self.vs[42]["name"] = """Concatlayer3rule3class7attribute047"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["mm__"] = """Concat"""
        self.vs[42]["GUID__"] = 4586711024890595042
        self.vs[43]["name"] = """Concatlayer3rule3class7attribute051"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["mm__"] = """Concat"""
        self.vs[43]["GUID__"] = 2787959414751113286
        self.vs[44]["name"] = """Concatlayer3rule3class7attribute054"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["mm__"] = """Concat"""
        self.vs[44]["GUID__"] = 5946714818104064725
        self.vs[45]["name"] = """Concatlayer3rule3class7attribute058"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["mm__"] = """Concat"""
        self.vs[45]["GUID__"] = 8341286265252271667
        self.vs[46]["mm__"] = """match_contains"""
        self.vs[46]["GUID__"] = 3736030040574416967
        self.vs[47]["mm__"] = """match_contains"""
        self.vs[47]["GUID__"] = 1355936439513161269
        self.vs[48]["mm__"] = """match_contains"""
        self.vs[48]["GUID__"] = 5468371027867960479
        self.vs[49]["mm__"] = """match_contains"""
        self.vs[49]["GUID__"] = 6301623438076705936
        self.vs[50]["mm__"] = """match_contains"""
        self.vs[50]["GUID__"] = 903831174497915277
        self.vs[51]["mm__"] = """match_contains"""
        self.vs[51]["GUID__"] = 649171404014063122
        self.vs[52]["mm__"] = """hasArgs"""
        self.vs[52]["GUID__"] = 6783659240170609647
        self.vs[53]["mm__"] = """hasArgs"""
        self.vs[53]["GUID__"] = 9101407149276683115
        self.vs[54]["mm__"] = """hasArgs"""
        self.vs[54]["GUID__"] = 79827765939782847
        self.vs[55]["mm__"] = """hasArgs"""
        self.vs[55]["GUID__"] = 3111282700665594714
        self.vs[56]["mm__"] = """hasArgs"""
        self.vs[56]["GUID__"] = 284668971448770980
        self.vs[57]["mm__"] = """hasArgs"""
        self.vs[57]["GUID__"] = 1212701985236784008
        self.vs[58]["mm__"] = """hasArgs"""
        self.vs[58]["GUID__"] = 3173732861251920737
        self.vs[59]["mm__"] = """hasArgs"""
        self.vs[59]["GUID__"] = 8042518793408558627
        self.vs[60]["mm__"] = """hasArgs"""
        self.vs[60]["GUID__"] = 76630824049083750
        self.vs[61]["mm__"] = """hasArgs"""
        self.vs[61]["GUID__"] = 5808060804151483906

