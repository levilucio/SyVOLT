

from core.himesis import Himesis

class Hlayer2rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer2rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule1, self).__init__(name='Hlayer2rule1', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 8], [0, 10], [10, 3], [1, 12], [12, 11], [1, 13], [13, 4], [3, 5], [5, 8], [4, 6], [6, 11], [4, 7], [7, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer2rule1"""
        self["GUID__"] = 5168436901638684801
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1874240902511291384
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9003689407793330022
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 569856112213347137
        self.vs[3]["name"] = """layer2rule1class1"""
        self.vs[3]["classtype"] = """OperationParameter"""
        self.vs[3]["mm__"] = """OperationParameter"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 6384498093837910865
        self.vs[4]["name"] = """layer2rule1class3"""
        self.vs[4]["classtype"] = """Argument"""
        self.vs[4]["mm__"] = """Argument"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 455639907935890401
        self.vs[5]["associationType"] = """type"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 2479527771868785189
        self.vs[6]["associationType"] = """type"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 2032174838174110702
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 6920338641760909902
        self.vs[8]["name"] = """layer2rule1class0"""
        self.vs[8]["classtype"] = """StringType"""
        self.vs[8]["mm__"] = """StringType"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 2498870357400360740
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 1602056033160384940
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 3348571896679090759
        self.vs[11]["name"] = """layer2rule1class2"""
        self.vs[11]["classtype"] = """StringType"""
        self.vs[11]["mm__"] = """StringType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 6650450268603695952
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 3670348148316736156
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 6730510286812297704

