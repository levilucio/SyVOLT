

from core.himesis import Himesis

class Hlayer1rule10(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule10.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule10, self).__init__(name='Hlayer1rule10', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([[0, 7], [7, 3], [0, 8], [8, 4], [1, 13], [13, 5], [1, 14], [14, 9], [1, 15], [15, 10], [3, 6], [6, 4], [5, 11], [11, 9], [5, 12], [12, 10], [5, 16], [16, 3], [9, 17], [17, 4], [10, 18], [18, 4], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule10"""
        self["GUID__"] = 8531948712820480244
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3436774516901524269
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6126379112879559288
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1855423511394674750
        self.vs[3]["name"] = """layer1rule10class0"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 6495682834438773576
        self.vs[4]["name"] = """layer1rule10class1"""
        self.vs[4]["classtype"] = """RequiredPort"""
        self.vs[4]["mm__"] = """RequiredPort"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 6773770656104508069
        self.vs[5]["name"] = """layer1rule10class2"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8494828287628053113
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_S"""
        self.vs[6]["GUID__"] = 3401099258521784196
        self.vs[7]["mm__"] = """match_contains"""
        self.vs[7]["GUID__"] = 4733612348026507301
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 7341317725225154198
        self.vs[9]["name"] = """layer1rule10class3"""
        self.vs[9]["classtype"] = """Member"""
        self.vs[9]["mm__"] = """Member"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8356207754004407836
        self.vs[10]["name"] = """layer1rule10class4"""
        self.vs[10]["classtype"] = """Member"""
        self.vs[10]["mm__"] = """Member"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 5172026416715299708
        self.vs[11]["associationType"] = """members"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 1688543555836129014
        self.vs[12]["associationType"] = """members"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 8301720007241293499
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 804351556096836833
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 7239594995461579352
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 8542274097446686760
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["GUID__"] = 3315928254766865552
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["GUID__"] = 2027375127806969887
        self.vs[18]["mm__"] = """backward_link"""
        self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["GUID__"] = 2743350427868015752

