

from core.himesis import Himesis

class HEEnum(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEEnum.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEEnum, self).__init__(name='HEEnum', num_nodes=41, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 32], [6, 9], [9, 33], [6, 10], [10, 34], [6, 11], [11, 35], [7, 12], [12, 36], [13, 14], [14, 36], [13, 15], [15, 32], [7, 16], [16, 37], [17, 18], [18, 37], [17, 19], [19, 33], [7, 20], [20, 38], [21, 22], [22, 38], [21, 23], [23, 34], [7, 24], [24, 39], [25, 26], [26, 39], [25, 27], [27, 35], [7, 28], [28, 40], [29, 30], [30, 40], [29, 31], [31, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EEnum"""
        self["GUID__"] = 7654161894967553874
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1307303483444417734
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3504163004540724927
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5726761322004392716
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 971648018768726432
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 553989825117412628
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 8129336481298719663
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EEnum"""
        self.vs[6]["mm__"] = """EEnum"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 4452859244075915800
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EEnum"""
        self.vs[7]["mm__"] = """EEnum"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 7939553005770725094
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 611489334023751963
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 8556568753334853994
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 767130501981851133
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 3855434591641882583
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = 515184369805836064
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 2948338452213920919
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 46637178724164708
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 4338582618187923895
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 861030570117443596
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6151982392055898063
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1609113787377456741
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 444037790205565412
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = 481267516306685126
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 4727491185378819236
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 3037886333904471379
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 8261777769425074135
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = 1293936003138066239
        self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        self.vs[25]["GUID__"] = 7801521492907750953
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = 4846782441602656687
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = 6787192741022691846
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = 3746637733830018153
        self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = 3412135983838302268
        self.vs[30]["mm__"] = """leftExpr"""
        self.vs[30]["GUID__"] = 5978595871180659885
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = 4472642673142270151
        self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 7264718490474641399
        self.vs[33]["name"] = """instanceClassName"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 8783955521896071225
        self.vs[34]["name"] = """instanceTypeName"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 3186768817090548018
        self.vs[35]["name"] = """serializable"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["GUID__"] = 7526899069599200399
        self.vs[36]["name"] = """name"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 3008455561639940624
        self.vs[37]["name"] = """instanceClassName"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 4528943186717645528
        self.vs[38]["name"] = """instanceTypeName"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 5356737330693104171
        self.vs[39]["name"] = """serializable"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 3090344177434721216
        self.vs[40]["name"] = """ApplyAttribute"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 1205462576710215199

