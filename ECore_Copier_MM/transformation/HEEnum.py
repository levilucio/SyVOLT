

from core.himesis import Himesis

class HEEnum(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEEnum.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEEnum, self).__init__(name='HEEnum', num_nodes=34, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 27], [6, 9], [9, 28], [6, 10], [10, 29], [7, 11], [11, 30], [12, 13], [13, 30], [12, 14], [14, 27], [7, 15], [15, 31], [16, 17], [17, 31], [16, 18], [18, 28], [7, 19], [19, 32], [20, 21], [21, 32], [20, 22], [22, 29], [7, 23], [23, 33], [24, 25], [25, 33], [24, 26], [26, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EEnum"""
        self["GUID__"] = 7654161894967553874
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 640237433513332684
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3656809926202298253
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1338700648830182415
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 7557257092347203026
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 8246416654016005084
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 5343435496136415361
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EEnum"""
        self.vs[6]["mm__"] = """EEnum"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 2475672968536113572
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EEnum"""
        self.vs[7]["mm__"] = """EEnum"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 4070674800091320244
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 2660198131957505024
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 8670623572227197506
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 4893610232142395863
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 47477565031182017
        self.vs[12]["name"] = """eq_"""
        self.vs[12]["mm__"] = """Equation"""
        self.vs[12]["GUID__"] = 42430039516967686
        self.vs[13]["mm__"] = """leftExpr"""
        self.vs[13]["GUID__"] = 6933809091343959659
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 483777434788831014
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 6707645376804004769
        self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = 2726708915381394558
        self.vs[17]["mm__"] = """leftExpr"""
        self.vs[17]["GUID__"] = 7955456071658551012
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = 5797574960774404186
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 1853479859813721497
        self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        self.vs[20]["GUID__"] = 144175694961381660
        self.vs[21]["mm__"] = """leftExpr"""
        self.vs[21]["GUID__"] = 7294257573084231050
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 8346002132824948375
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = 4513913527837148673
        self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = 7254500124480143123
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 1155568646395350009
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = 8429665672400294751
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 6558011857976288054
        self.vs[28]["name"] = """instanceClassName"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 6918167232461878953
        self.vs[29]["name"] = """serializable"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 7920787199788902883
        self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = 5701530045453646982
        self.vs[31]["name"] = """instanceClassName"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = 8182713849838156806
        self.vs[32]["name"] = """serializable"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 5526628680568321214
        self.vs[33]["name"] = """ApplyAttribute"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 8092047018596372342

