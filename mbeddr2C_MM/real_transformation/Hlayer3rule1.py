

from core.himesis import Himesis

class Hlayer3rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer3rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule1, self).__init__(name='Hlayer3rule1', num_nodes=37, edges=[])
        
        # Add the edges
        self.add_edges([[0, 13], [13, 12], [0, 14], [14, 3], [1, 22], [22, 15], [1, 23], [23, 4], [1, 24], [24, 5], [12, 6], [6, 3], [15, 16], [16, 4], [4, 17], [17, 5], [15, 7], [7, 12], [12, 18], [18, 25], [3, 19], [19, 26], [4, 8], [8, 27], [9, 10], [10, 27], [9, 11], [30, 35], [35, 26], [30, 36], [36, 21], [29, 33], [33, 20], [29, 34], [34, 30], [28, 31], [31, 25], [28, 32], [32, 29], [11, 28], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer3rule1"""
        self["GUID__"] = 2200570761485908566
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7758083835166991734
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8500187561514725465
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6733699874523781220
        self.vs[3]["name"] = """layer3rule1class1"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7175063265706147147
        self.vs[4]["name"] = """layer3rule1class3"""
        self.vs[4]["classtype"] = """FunctionPrototype"""
        self.vs[4]["mm__"] = """FunctionPrototype"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 6950078674838445905
        self.vs[5]["name"] = """layer3rule1class4"""
        self.vs[5]["classtype"] = """VoidType"""
        self.vs[5]["mm__"] = """VoidType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 1117626365280663835
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_S"""
        self.vs[6]["GUID__"] = 3652350193273049450
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 3915568853618640335
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 8315696901262565399
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 7561766415048017888
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 1188098325483919581
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 3423282341391311065
        self.vs[12]["name"] = """layer3rule1class0"""
        self.vs[12]["classtype"] = """ImplementationModule"""
        self.vs[12]["mm__"] = """ImplementationModule"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = 4006451195955109399
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 6009642050652424626
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 490703448977961925
        self.vs[15]["name"] = """layer3rule1class2"""
        self.vs[15]["classtype"] = """ImplementationModule"""
        self.vs[15]["mm__"] = """ImplementationModule"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = 9212025789253181457
        self.vs[16]["associationType"] = """contents"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 8142662385231835919
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 3950256663363015307
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = 3791261578939912943
        self.vs[19]["mm__"] = """hasAttribute_S"""
        self.vs[19]["GUID__"] = 1746775357802340043
        self.vs[20]["name"] = """_"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2198873769894844961
        self.vs[21]["name"] = """__init"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["GUID__"] = 4627545130111809956
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 1234239171159053232
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 8541455553233612687
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 590368976413498960
        self.vs[25]["name"] = """name"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["GUID__"] = 7002711904800852401
        self.vs[26]["name"] = """name"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = 3384018067277019268
        self.vs[27]["name"] = """name"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["GUID__"] = 7915711357189848254
        self.vs[28]["name"] = """Concatlayer3rule1class3attribute026"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Concat"""
        self.vs[28]["GUID__"] = 4211334999657592051
        self.vs[29]["name"] = """Concatlayer3rule1class3attribute029"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["GUID__"] = 5275966311103777407
        self.vs[30]["name"] = """Concatlayer3rule1class3attribute033"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["mm__"] = """Concat"""
        self.vs[30]["GUID__"] = 6400711927230050169
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = 6634839909863435699
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 784373535784712540
        self.vs[33]["mm__"] = """hasArgs"""
        self.vs[33]["GUID__"] = 4942624974148544697
        self.vs[34]["mm__"] = """hasArgs"""
        self.vs[34]["GUID__"] = 6925143274352340673
        self.vs[35]["mm__"] = """hasArgs"""
        self.vs[35]["GUID__"] = 5743669905444965983
        self.vs[36]["mm__"] = """hasArgs"""
        self.vs[36]["GUID__"] = 542255748570118783

