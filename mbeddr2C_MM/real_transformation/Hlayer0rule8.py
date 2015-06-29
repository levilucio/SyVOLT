

from core.himesis import Himesis

class Hlayer0rule8(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule8.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule8, self).__init__(name='Hlayer0rule8', num_nodes=37, edges=[])
        
        # Add the edges
        self.add_edges([[0, 13], [13, 3], [0, 14], [14, 4], [1, 15], [15, 5], [1, 16], [16, 6], [4, 7], [7, 3], [5, 8], [8, 6], [3, 17], [17, 19], [4, 18], [18, 20], [5, 9], [9, 21], [10, 11], [11, 21], [10, 12], [28, 35], [35, 23], [28, 36], [36, 24], [27, 33], [33, 19], [27, 34], [34, 28], [26, 31], [31, 22], [26, 32], [32, 27], [25, 29], [29, 20], [25, 30], [30, 26], [12, 25], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule8"""
        self["GUID__"] = 939274848717554792
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3477005691988949200
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1282065071082730651
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4069134612997099709
        self.vs[3]["name"] = """layer0rule8class0"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 3725723404846490905
        self.vs[4]["name"] = """layer0rule8class1"""
        self.vs[4]["classtype"] = """ImplementationModule"""
        self.vs[4]["mm__"] = """ImplementationModule"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 1306172311845693094
        self.vs[5]["name"] = """layer0rule8class2"""
        self.vs[5]["classtype"] = """TypeDef"""
        self.vs[5]["mm__"] = """TypeDef"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 287325861492409238
        self.vs[6]["name"] = """layer0rule8class3"""
        self.vs[6]["classtype"] = """StructType"""
        self.vs[6]["mm__"] = """StructType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8689168566205620701
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 2099408639027225003
        self.vs[8]["associationType"] = """original"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 860838550009319889
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 7698464571428725806
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 7472435512952741002
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 2941066422536232380
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 7309626085194259425
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 5384235245398691371
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 8448901032167638363
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 106125826832589970
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = 3725685328674861687
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = 2164388527432522370
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = 6837487482025678991
        self.vs[19]["name"] = """name"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 6297252783791045352
        self.vs[20]["name"] = """name"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 8157537066950210018
        self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["GUID__"] = 6299988636516955985
        self.vs[22]["name"] = """_"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 2544590675703309053
        self.vs[23]["name"] = """__"""
        self.vs[23]["mm__"] = """Constant"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["GUID__"] = 7327461013538134102
        self.vs[24]["name"] = """cdata_t"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 298305271053444410
        self.vs[25]["name"] = """Concatlayer0rule8class2attribute022"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 2378767392465143164
        self.vs[26]["name"] = """Concatlayer0rule8class2attribute025"""
        self.vs[26]["mm__"] = """Concat"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 8145711372727549109
        self.vs[27]["name"] = """Concatlayer0rule8class2attribute029"""
        self.vs[27]["mm__"] = """Concat"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 6865725689587203849
        self.vs[28]["name"] = """Concatlayer0rule8class2attribute032"""
        self.vs[28]["mm__"] = """Concat"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 4384926287376273781
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = 2007892114732518196
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = 5770119311810886735
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = 5185361967587902392
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 5502325948315567652
        self.vs[33]["mm__"] = """hasArgs"""
        self.vs[33]["GUID__"] = 7744484751757727481
        self.vs[34]["mm__"] = """hasArgs"""
        self.vs[34]["GUID__"] = 3555235197878900683
        self.vs[35]["mm__"] = """hasArgs"""
        self.vs[35]["GUID__"] = 488148763988111332
        self.vs[36]["mm__"] = """hasArgs"""
        self.vs[36]["GUID__"] = 80975724904071406

