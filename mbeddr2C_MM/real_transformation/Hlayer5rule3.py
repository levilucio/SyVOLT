

from core.himesis import Himesis

class Hlayer5rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer5rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule3, self).__init__(name='Hlayer5rule3', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 19], [19, 3], [0, 20], [20, 9], [0, 21], [21, 4], [0, 22], [22, 5], [1, 23], [23, 10], [1, 24], [24, 6], [1, 25], [25, 7], [1, 26], [26, 8], [3, 13], [13, 9], [9, 14], [14, 4], [4, 15], [15, 5], [10, 16], [16, 6], [6, 17], [17, 7], [7, 18], [18, 8], [10, 11], [11, 3], [8, 12], [12, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule3"""
        self["GUID__"] = 6018570213547247165
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8837701791382003838
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8321713293228461173
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5243782266433102559
        self.vs[3]["name"] = """layer5rule3class0"""
        self.vs[3]["classtype"] = """TestCase"""
        self.vs[3]["mm__"] = """TestCase"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8764935725910691577
        self.vs[4]["name"] = """layer5rule3class2"""
        self.vs[4]["classtype"] = """InitializeConfiguration"""
        self.vs[4]["mm__"] = """InitializeConfiguration"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 7098573999961288724
        self.vs[5]["name"] = """layer5rule3class3"""
        self.vs[5]["classtype"] = """InstanceConfiguration"""
        self.vs[5]["mm__"] = """InstanceConfiguration"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1634451572400415300
        self.vs[6]["name"] = """layer5rule3class5"""
        self.vs[6]["classtype"] = """ExpressionStatement"""
        self.vs[6]["mm__"] = """ExpressionStatement"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 2835138067965300303
        self.vs[7]["name"] = """layer5rule3class6"""
        self.vs[7]["classtype"] = """FunctionCall"""
        self.vs[7]["mm__"] = """FunctionCall"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 8986783094526370827
        self.vs[8]["name"] = """layer5rule3class7"""
        self.vs[8]["classtype"] = """FunctionPrototype"""
        self.vs[8]["mm__"] = """FunctionPrototype"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 7086533737468980354
        self.vs[9]["name"] = """layer5rule3class1"""
        self.vs[9]["classtype"] = """StatementList"""
        self.vs[9]["mm__"] = """StatementList"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = 7844630876079929512
        self.vs[10]["name"] = """layer5rule3class4"""
        self.vs[10]["classtype"] = """StatementList"""
        self.vs[10]["mm__"] = """StatementList"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 4488739910730172846
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 6989855752118061649
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = 138323538880268831
        self.vs[13]["associationType"] = """body"""
        self.vs[13]["mm__"] = """directLink_S"""
        self.vs[13]["GUID__"] = 8488093956845977087
        self.vs[14]["associationType"] = """statements"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = 2143720421474475297
        self.vs[15]["associationType"] = """config"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = 793014014494040735
        self.vs[16]["associationType"] = """statements"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 2329001922006328067
        self.vs[17]["associationType"] = """expr"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 5678848339153240113
        self.vs[18]["associationType"] = """function"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = 7224244882222694738
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = 195300450986432221
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = 6645970520437968192
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = 448871555050909251
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = 714992834186226747
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 2424098737504988239
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 4456444635493012710
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = 6430038259820044345
        self.vs[26]["mm__"] = """apply_contains"""
        self.vs[26]["GUID__"] = 8935170676408349912

