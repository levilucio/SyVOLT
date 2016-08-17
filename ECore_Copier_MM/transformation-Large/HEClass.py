

from core.himesis import Himesis

class HEClass(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEClass.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEClass, self).__init__(name='HEClass', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 37], [6, 9], [9, 38], [6, 10], [10, 39], [6, 11], [11, 40], [6, 12], [12, 41], [7, 13], [13, 42], [14, 15], [15, 42], [14, 16], [16, 37], [7, 17], [17, 43], [18, 19], [19, 43], [18, 20], [20, 38], [7, 21], [21, 44], [22, 23], [23, 44], [22, 24], [24, 39], [7, 25], [25, 45], [26, 27], [27, 45], [26, 28], [28, 40], [7, 29], [29, 46], [30, 31], [31, 46], [30, 32], [32, 41], [7, 33], [33, 47], [34, 35], [35, 47], [34, 36], [36, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EClass"""
        self["GUID__"] = 7513848719461737483
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4742423356105061334
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5181436541492304252
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4434945747091075106
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 4989009618805165137
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 5986624910178420165
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 580242660644043333
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EClass"""
        self.vs[6]["mm__"] = """EClass"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 22786086082354646
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClass"""
        self.vs[7]["mm__"] = """EClass"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1272466000560267557
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 6283651994548442189
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 9048676135290437050
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 2602803380974761347
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 8447611663646971915
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 7497873399091937712
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 2988374777112564422
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 6115115672666886032
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 5370290965238461812
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 4328026573727980470
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 5930191671046105503
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 4027767436937871107
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 8198350520857470846
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 56305781236500140
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5816270308432200821
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 3018523247400060675
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 1134675740742584747
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 6391469163412356173
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 2231421643249516077
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        self.vs[26]["GUID__"] = 393270198530292226
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 7959241052684112490
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 9176793662181759298
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 7096832831924373997
        self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 6063714520899510436
        self.vs[31]["mm__"] = """leftExpr"""
        self.vs[31]["GUID__"] = 325653883320794137
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = 8495101061851008361
        self.vs[33]["mm__"] = """hasAttribute_T"""
        self.vs[33]["GUID__"] = 7801276425328862995
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 1784090817628174897
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 1064151979311302782
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 8886965455982764657
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 7429345277418169462
        self.vs[38]["name"] = """instanceClassName"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 5291727197465673332
        self.vs[39]["name"] = """instanceTypeName"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 1532970426105482341
        self.vs[40]["name"] = """abstract"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 3129070758137889662
        self.vs[41]["name"] = """interface"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 1478859906853884304
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 1918273726752043050
        self.vs[43]["name"] = """instanceClassName"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 1539138781819746550
        self.vs[44]["name"] = """instanceTypeName"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 4056093923231812936
        self.vs[45]["name"] = """abstract"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 4353261615111462761
        self.vs[46]["name"] = """interface"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 637324929847536973
        self.vs[47]["name"] = """ApplyAttribute"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 3198182771433055588

