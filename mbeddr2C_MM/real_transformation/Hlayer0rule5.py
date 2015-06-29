

from core.himesis import Himesis

class Hlayer0rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule5, self).__init__(name='Hlayer0rule5', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 3], [0, 10], [10, 4], [1, 11], [11, 5], [1, 12], [12, 6], [4, 7], [7, 3], [5, 8], [8, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule5"""
        self["GUID__"] = 3740954869658780496
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7455821649774805763
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 745916373662212663
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 485773445444824707
        self.vs[3]["name"] = """layer0rule5class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 338288484309810316
        self.vs[4]["name"] = """layer0rule5class1"""
        self.vs[4]["classtype"] = """ClientServerInterface"""
        self.vs[4]["mm__"] = """ClientServerInterface"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 368717735755426589
        self.vs[5]["name"] = """layer0rule5class2"""
        self.vs[5]["classtype"] = """PointerType"""
        self.vs[5]["mm__"] = """PointerType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 7488325416180353468
        self.vs[6]["name"] = """layer0rule5class3"""
        self.vs[6]["classtype"] = """VoidType"""
        self.vs[6]["mm__"] = """VoidType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8653977268914084454
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 5639018525663084460
        self.vs[8]["associationType"] = """baseType"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 2817865268507246561
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 361778730186676799
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 6101053914769542521
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 7596694628287229462
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 368701594411872943

