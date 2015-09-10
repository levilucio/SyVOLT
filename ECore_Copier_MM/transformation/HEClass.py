

from core.himesis import Himesis

class HEClass(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEClass.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEClass, self).__init__(name='HEClass', num_nodes=41, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 32], [6, 9], [9, 33], [6, 10], [10, 34], [6, 11], [11, 35], [7, 12], [12, 36], [13, 14], [14, 36], [13, 15], [15, 32], [7, 16], [16, 37], [17, 18], [18, 37], [17, 19], [19, 33], [7, 20], [20, 38], [21, 22], [22, 38], [21, 23], [23, 34], [7, 24], [24, 39], [25, 26], [26, 39], [25, 27], [27, 35], [7, 28], [28, 40], [29, 30], [30, 40], [29, 31], [31, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EClass"""
        self["GUID__"] = 7513848719461737483
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7679959773369961146
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4663941621232147602
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7558907556437810466
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 8800513298996107035
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 9052645438868860738
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 4333262875930607449
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EClass"""
        self.vs[6]["mm__"] = """EClass"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 7683639633110391658
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClass"""
        self.vs[7]["mm__"] = """EClass"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 47183723416652653
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 5445339977253313156
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 9053346556987227700
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 5826418403940476000
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 5000787305622309502
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = 5700915594120954247
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 8690866683228089299
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 3353914725476301396
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 6293245609835071742
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 4002642293767595999
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 1094737844251642267
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 9114826511704155673
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 7220936787210526438
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = 7538378383704742601
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 4811242076591121311
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 307643592513311574
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 3841534864541630018
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = 8832012500354727809
        self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        self.vs[25]["GUID__"] = 5987712891917623434
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = 5377576155175359417
        self.vs[27]["mm__"] = """rightExpr"""
        self.vs[27]["GUID__"] = 331389620860982694
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = 8969723836954972214
        self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        self.vs[29]["GUID__"] = 2427276364045409035
        self.vs[30]["mm__"] = """leftExpr"""
        self.vs[30]["GUID__"] = 3916513323955017257
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = 3634658502900642701
        self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 3627604332024792641
        self.vs[33]["name"] = """instanceClassName"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 7325535048034329707
        self.vs[34]["name"] = """abstract"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 3148960385473731569
        self.vs[35]["name"] = """interface"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["GUID__"] = 423896392736532409
        self.vs[36]["name"] = """name"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 136369469270777102
        self.vs[37]["name"] = """instanceClassName"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 1268244587319563718
        self.vs[38]["name"] = """abstract"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 8753963199724832211
        self.vs[39]["name"] = """interface"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 8323006992875295818
        self.vs[40]["name"] = """ApplyAttribute"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 3841477311265598622

