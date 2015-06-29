

from core.himesis import Himesis

class Hlayer0rule11(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule11, self).__init__(name='Hlayer0rule11', num_nodes=53, edges=[])
        
        # Add the edges
        self.add_edges([[0, 25], [25, 3], [0, 26], [26, 4], [0, 27], [27, 5], [0, 28], [28, 6], [0, 29], [29, 7], [1, 9], [9, 8], [4, 17], [17, 3], [3, 18], [18, 5], [5, 19], [19, 6], [7, 20], [20, 4], [3, 21], [21, 30], [4, 22], [22, 31], [6, 23], [23, 32], [7, 24], [24, 33], [8, 10], [10, 34], [11, 12], [12, 34], [11, 13], [40, 51], [51, 16], [40, 52], [52, 32], [39, 49], [49, 30], [39, 50], [50, 40], [38, 47], [47, 15], [38, 48], [48, 39], [37, 45], [45, 31], [37, 46], [46, 38], [36, 43], [43, 14], [36, 44], [44, 37], [35, 41], [41, 33], [35, 42], [42, 36], [13, 35], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule11"""
        self["GUID__"] = 2542720957060804670
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9024730435580767756
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7517995910954205050
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4238121795322460018
        self.vs[3]["name"] = """layer0rule11class0"""
        self.vs[3]["classtype"] = """ProvidedPort"""
        self.vs[3]["mm__"] = """ProvidedPort"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8150205469071434092
        self.vs[4]["name"] = """layer0rule11class1"""
        self.vs[4]["classtype"] = """AtomicComponent"""
        self.vs[4]["mm__"] = """AtomicComponent"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4462138160291391619
        self.vs[5]["name"] = """layer0rule11class2"""
        self.vs[5]["classtype"] = """ClientServerInterface"""
        self.vs[5]["mm__"] = """ClientServerInterface"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5103347109764697641
        self.vs[6]["name"] = """layer0rule11class3"""
        self.vs[6]["classtype"] = """Operation"""
        self.vs[6]["mm__"] = """Operation"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 4657273579472131248
        self.vs[7]["name"] = """layer0rule11class4"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3065538869614267685
        self.vs[8]["name"] = """layer0rule11class5"""
        self.vs[8]["classtype"] = """FunctionPrototype"""
        self.vs[8]["mm__"] = """FunctionPrototype"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5045807374466761763
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 8364855779416292974
        self.vs[10]["mm__"] = """hasAttribute_T"""
        self.vs[10]["GUID__"] = 1330245642671745095
        self.vs[11]["name"] = """eq_"""
        self.vs[11]["mm__"] = """Equation"""
        self.vs[11]["GUID__"] = 6847277776404658988
        self.vs[12]["mm__"] = """leftExpr"""
        self.vs[12]["GUID__"] = 7602369010203027091
        self.vs[13]["mm__"] = """rightExpr"""
        self.vs[13]["GUID__"] = 1264276880519807027
        self.vs[14]["name"] = """_"""
        self.vs[14]["mm__"] = """Constant"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 4435928275190896073
        self.vs[15]["name"] = """_"""
        self.vs[15]["mm__"] = """Constant"""
        self.vs[15]["Type"] = """'String'"""
        self.vs[15]["GUID__"] = 6367095725749859442
        self.vs[16]["name"] = """_"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 1192968059409857832
        self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = 4359162297089429082
        self.vs[18]["associationType"] = """intf"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = 7154011497748097093
        self.vs[19]["associationType"] = """contents"""
        self.vs[19]["mm__"] = """directLink_S"""
        self.vs[19]["GUID__"] = 4593138386084221528
        self.vs[20]["associationType"] = """contents"""
        self.vs[20]["mm__"] = """directLink_S"""
        self.vs[20]["GUID__"] = 2386723711171580871
        self.vs[21]["mm__"] = """hasAttribute_S"""
        self.vs[21]["GUID__"] = 1198860948865270484
        self.vs[22]["mm__"] = """hasAttribute_S"""
        self.vs[22]["GUID__"] = 2976489265044939062
        self.vs[23]["mm__"] = """hasAttribute_S"""
        self.vs[23]["GUID__"] = 7743803938415655410
        self.vs[24]["mm__"] = """hasAttribute_S"""
        self.vs[24]["GUID__"] = 3710539866976605028
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 5218902330955159439
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 8496662744482956799
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 6328046252076501114
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = 6273637768157676116
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = 2294154243968962555
        self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = 918435752665945741
        self.vs[31]["name"] = """name"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = 8578968338810645267
        self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 5362505778934959293
        self.vs[33]["name"] = """name"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 1374680159373891785
        self.vs[34]["name"] = """name"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 7236143702649506524
        self.vs[35]["name"] = """Concatlayer0rule11class5attribute032"""
        self.vs[35]["mm__"] = """Concat"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["GUID__"] = 2864274254869243593
        self.vs[36]["name"] = """Concatlayer0rule11class5attribute035"""
        self.vs[36]["mm__"] = """Concat"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 6913267642597809232
        self.vs[37]["name"] = """Concatlayer0rule11class5attribute039"""
        self.vs[37]["mm__"] = """Concat"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 7167836846496510157
        self.vs[38]["name"] = """Concatlayer0rule11class5attribute042"""
        self.vs[38]["mm__"] = """Concat"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 5208459195207512564
        self.vs[39]["name"] = """Concatlayer0rule11class5attribute046"""
        self.vs[39]["mm__"] = """Concat"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 2966782500944209378
        self.vs[40]["name"] = """Concatlayer0rule11class5attribute049"""
        self.vs[40]["mm__"] = """Concat"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 978901506531858635
        self.vs[41]["mm__"] = """hasArgs"""
        self.vs[41]["GUID__"] = 8849333800104391206
        self.vs[42]["mm__"] = """hasArgs"""
        self.vs[42]["GUID__"] = 1562791071050154385
        self.vs[43]["mm__"] = """hasArgs"""
        self.vs[43]["GUID__"] = 3697424980623993387
        self.vs[44]["mm__"] = """hasArgs"""
        self.vs[44]["GUID__"] = 7782912017379696783
        self.vs[45]["mm__"] = """hasArgs"""
        self.vs[45]["GUID__"] = 6988685646008222054
        self.vs[46]["mm__"] = """hasArgs"""
        self.vs[46]["GUID__"] = 5879028121340526435
        self.vs[47]["mm__"] = """hasArgs"""
        self.vs[47]["GUID__"] = 3301599956500684384
        self.vs[48]["mm__"] = """hasArgs"""
        self.vs[48]["GUID__"] = 7570512239790371583
        self.vs[49]["mm__"] = """hasArgs"""
        self.vs[49]["GUID__"] = 135855327193071862
        self.vs[50]["mm__"] = """hasArgs"""
        self.vs[50]["GUID__"] = 3288255919631715813
        self.vs[51]["mm__"] = """hasArgs"""
        self.vs[51]["GUID__"] = 7571293974932540548
        self.vs[52]["mm__"] = """hasArgs"""
        self.vs[52]["GUID__"] = 7246971074626241723

