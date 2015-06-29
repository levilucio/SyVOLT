

from core.himesis import Himesis

class HEDataType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEDataType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEDataType, self).__init__(name='HEDataType', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 5], [1, 4], [4, 6], [5, 7], [7, 22], [5, 8], [8, 23], [5, 9], [9, 24], [6, 10], [10, 25], [11, 12], [12, 25], [11, 13], [13, 22], [6, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 23], [6, 18], [18, 27], [19, 20], [20, 27], [19, 21], [21, 24], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EDataType"""
        self["GUID__"] = 5396183599598318015
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2990237569192219384
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3547847299311927949
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6193268605844840475
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 6162069969548376723
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 5594917883970347897
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EDataType"""
        self.vs[5]["mm__"] = """EDataType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 8692334925482624836
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EDataType"""
        self.vs[6]["mm__"] = """EDataType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 2288770650232474329
        self.vs[7]["mm__"] = """hasAttribute_S"""
        self.vs[7]["GUID__"] = 8964077352689818516
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 3035590407882655684
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 7564180306808041665
        self.vs[10]["mm__"] = """hasAttribute_T"""
        self.vs[10]["GUID__"] = 4002714771236125605
        self.vs[11]["name"] = """eq_"""
        self.vs[11]["mm__"] = """Equation"""
        self.vs[11]["GUID__"] = 554248526303184141
        self.vs[12]["mm__"] = """leftExpr"""
        self.vs[12]["GUID__"] = 6163826501411229235
        self.vs[13]["mm__"] = """rightExpr"""
        self.vs[13]["GUID__"] = 1871455270713431375
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 8946138659828679121
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 6911682905243778597
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 2607782029200970103
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 5492771333062366130
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 8633216198795312448
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 7971056818428805315
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 7453624734054402962
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 9098126357278006883
        self.vs[22]["name"] = """name"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 1129417595439594938
        self.vs[23]["name"] = """instanceClassName"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["GUID__"] = 4905985461766583551
        self.vs[24]["name"] = """serializable"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 4466154630665545803
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 1070365084770098460
        self.vs[26]["name"] = """instanceClassName"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 6686757845410634342
        self.vs[27]["name"] = """serializable"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 8031878995780081225

