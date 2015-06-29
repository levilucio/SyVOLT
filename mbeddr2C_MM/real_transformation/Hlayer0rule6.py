

from core.himesis import Himesis

class Hlayer0rule6(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule6.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule6, self).__init__(name='Hlayer0rule6', num_nodes=37, edges=[])
        
        # Add the edges
        self.add_edges([[0, 13], [13, 3], [0, 14], [14, 4], [1, 15], [15, 5], [1, 16], [16, 6], [4, 7], [7, 3], [5, 8], [8, 6], [3, 17], [17, 19], [4, 18], [18, 20], [5, 9], [9, 21], [10, 11], [11, 21], [10, 12], [28, 35], [35, 23], [28, 36], [36, 24], [27, 33], [33, 19], [27, 34], [34, 28], [26, 31], [31, 22], [26, 32], [32, 27], [25, 29], [29, 20], [25, 30], [30, 26], [12, 25], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule6"""
        self["GUID__"] = 6094203288788595119
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1914828360665727193
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7207059874993209009
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1409156441876016229
        self.vs[3]["name"] = """layer0rule6class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 296845207067533266
        self.vs[4]["name"] = """layer0rule6class1"""
        self.vs[4]["classtype"] = """ImplementationModule"""
        self.vs[4]["mm__"] = """ImplementationModule"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 7958440041572820988
        self.vs[5]["name"] = """layer0rule6class2"""
        self.vs[5]["classtype"] = """TypeDef"""
        self.vs[5]["mm__"] = """TypeDef"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3667510146412206454
        self.vs[6]["name"] = """layer0rule6class3"""
        self.vs[6]["classtype"] = """StructType"""
        self.vs[6]["mm__"] = """StructType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 4071741552804765862
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 8742782634020238118
        self.vs[8]["associationType"] = """original"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 4430005774088583140
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 8115857407678421106
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 6766557891633596548
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 2913250657023545326
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 6549308119644406171
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 8966493479025565733
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 6375797633065527350
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 6329232135736885984
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = 7320161752425398040
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = 1545167346874362454
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = 1125903039712207489
        self.vs[19]["name"] = """name"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 4135083697142588806
        self.vs[20]["name"] = """name"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 6124775944734991940
        self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["GUID__"] = 4297687960745397545
        self.vs[22]["name"] = """_"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 8934443351983657286
        self.vs[23]["name"] = """__"""
        self.vs[23]["mm__"] = """Constant"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["GUID__"] = 7707022612411669339
        self.vs[24]["name"] = """idata_t"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 7280132787171597484
        self.vs[25]["name"] = """Concatlayer0rule6class2attribute022"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 4384246770022688319
        self.vs[26]["name"] = """Concatlayer0rule6class2attribute025"""
        self.vs[26]["mm__"] = """Concat"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 5148643976723188832
        self.vs[27]["name"] = """Concatlayer0rule6class2attribute029"""
        self.vs[27]["mm__"] = """Concat"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 1210978127783846199
        self.vs[28]["name"] = """Concatlayer0rule6class2attribute032"""
        self.vs[28]["mm__"] = """Concat"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 2659654329544091593
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = 5898864159944685793
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = 6370497851329793204
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = 647525357799706145
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 1030479807028706046
        self.vs[33]["mm__"] = """hasArgs"""
        self.vs[33]["GUID__"] = 7406755411691847738
        self.vs[34]["mm__"] = """hasArgs"""
        self.vs[34]["GUID__"] = 8692572837949264086
        self.vs[35]["mm__"] = """hasArgs"""
        self.vs[35]["GUID__"] = 3208590112607134950
        self.vs[36]["mm__"] = """hasArgs"""
        self.vs[36]["GUID__"] = 7531286918854722105

