

from core.himesis import Himesis

class Hlayer0rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule1, self).__init__(name='Hlayer0rule1', num_nodes=34, edges=[])
        
        # Add the edges
        self.add_edges([[0, 12], [12, 3], [0, 13], [13, 4], [1, 6], [6, 5], [4, 7], [7, 3], [3, 14], [14, 16], [4, 15], [15, 17], [5, 8], [8, 18], [9, 10], [10, 18], [9, 11], [25, 32], [32, 20], [25, 33], [33, 21], [24, 30], [30, 16], [24, 31], [31, 25], [23, 28], [28, 19], [23, 29], [29, 24], [22, 26], [26, 17], [22, 27], [27, 23], [11, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule1"""
        self["GUID__"] = 7307003920251855937
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3329973901254323263
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4944970949051568607
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6968604482054683449
        self.vs[3]["name"] = """layer0rule1class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 2324471115382268137
        self.vs[4]["name"] = """layer0rule1class1"""
        self.vs[4]["classtype"] = """ImplementationModule"""
        self.vs[4]["mm__"] = """ImplementationModule"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4097738427848440983
        self.vs[5]["name"] = """layer0rule1class2"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 463301428011662707
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 5230631487770051599
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 3692907047831033229
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 7553096463607073515
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 8533657115700972746
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 5812494823803201410
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 3123265854482680416
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = 2790881576361314336
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 4986227035816942452
        self.vs[14]["mm__"] = """hasAttribute_S"""
        self.vs[14]["GUID__"] = 71658955231357873
        self.vs[15]["mm__"] = """hasAttribute_S"""
        self.vs[15]["GUID__"] = 6596983467929462125
        self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 7283071071212644725
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 8053634176610264630
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 7930515503224962339
        self.vs[19]["name"] = """_"""
        self.vs[19]["mm__"] = """Constant"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 1725090962428092951
        self.vs[20]["name"] = """__"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 8860045072912870453
        self.vs[21]["name"] = """idata"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["GUID__"] = 4585817538010170404
        self.vs[22]["name"] = """Concatlayer0rule1class2attribute019"""
        self.vs[22]["mm__"] = """Concat"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 260480964917587772
        self.vs[23]["name"] = """Concatlayer0rule1class2attribute022"""
        self.vs[23]["mm__"] = """Concat"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["GUID__"] = 2884477739111719062
        self.vs[24]["name"] = """Concatlayer0rule1class2attribute026"""
        self.vs[24]["mm__"] = """Concat"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 6399311427716174475
        self.vs[25]["name"] = """Concatlayer0rule1class2attribute029"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 5758830202455933537
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = 7534258879342438883
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = 3778094916591390413
        self.vs[28]["mm__"] = """hasArgs"""
        self.vs[28]["GUID__"] = 6153861151647324147
        self.vs[29]["mm__"] = """hasArgs"""
        self.vs[29]["GUID__"] = 9213141913387165605
        self.vs[30]["mm__"] = """hasArgs"""
        self.vs[30]["GUID__"] = 6233595387361407726
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = 7293563508004729371
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 2733280831187335579
        self.vs[33]["mm__"] = """hasArgs"""
        self.vs[33]["GUID__"] = 1076574681364246621

