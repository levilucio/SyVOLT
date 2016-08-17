

from core.himesis import Himesis

class HEDataType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEDataType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEDataType, self).__init__(name='HEDataType', num_nodes=41, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 32], [6, 9], [9, 33], [6, 10], [10, 34], [6, 11], [11, 35], [7, 12], [12, 36], [13, 14], [14, 36], [13, 15], [15, 32], [7, 16], [16, 37], [17, 18], [18, 37], [17, 19], [19, 33], [7, 20], [20, 38], [21, 22], [22, 38], [21, 23], [23, 34], [7, 24], [24, 39], [25, 26], [26, 39], [25, 27], [27, 35], [7, 28], [28, 40], [29, 30], [30, 40], [29, 31], [31, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EDataType"""
        self["GUID__"] = 5396183599598318015
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1067585622720708903
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9023050572148924678
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4604967754652708090
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 7038913861194902512
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 7876228595461755021
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 6165192239543984316
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EDataType"""
        self.vs[6]["mm__"] = """EDataType"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 93360005422950726
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EDataType"""
        self.vs[7]["mm__"] = """EDataType"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 2646493541280217838
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 2367506216802068112
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 7548598791140641633
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 1220176681443763407
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 770265390985573196
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = 4183016704028585419
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 832109370145865021
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 7752136684000675580
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 7261262060874607130
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 5256536622949517609
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4071714872447792980
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 5253471974203207987
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6577996693665599902
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = 4160781966827575447
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 1353707105445781324
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 4801677920479105387
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 8279147981595169124
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = 1770422418320390231
        self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        self.vs[25]["GUID__"] = 2729685347842678274
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = 7926083014713402192
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = 5351899490486127218
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = 8086524972958147433
        self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = 6736704815175247026
        self.vs[30]["mm__"] = """leftExpr"""
        self.vs[30]["GUID__"] = 6218966783774053042
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = 4537557062352163433
        self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 2686443993613039057
        self.vs[33]["name"] = """instanceClassName"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 4977528580014127822
        self.vs[34]["name"] = """instanceTypeName"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 4519036695203987516
        self.vs[35]["name"] = """serializable"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["GUID__"] = 1747073793922142579
        self.vs[36]["name"] = """name"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 4247500863154858540
        self.vs[37]["name"] = """instanceClassName"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 5248824937468875365
        self.vs[38]["name"] = """instanceTypeName"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 3186222386860575589
        self.vs[39]["name"] = """serializable"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 7601811651069397060
        self.vs[40]["name"] = """ApplyAttribute"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 2739881814265057067

