

from core.himesis import Himesis

class Hlayer1rule9(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule9.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule9, self).__init__(name='Hlayer1rule9', num_nodes=12, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 8], [8, 5], [1, 9], [9, 6], [6, 7], [7, 5], [6, 10], [10, 3], [5, 11], [11, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule9"""
        self["GUID__"] = 7728713906686879034
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9152417224915965971
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4666031264313568106
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8078530229669911385
        self.vs[3]["name"] = """layer1rule9class0"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 6709456965990160617
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 2722316732194079345
        self.vs[5]["name"] = """layer1rule9class1"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2289010991542147882
        self.vs[6]["name"] = """layer1rule9class2"""
        self.vs[6]["classtype"] = """StructType"""
        self.vs[6]["mm__"] = """StructType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 2525931335263272349
        self.vs[7]["associationType"] = """struct"""
        self.vs[7]["mm__"] = """directLink_T"""
        self.vs[7]["GUID__"] = 4723906769756873066
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 291380704632004529
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 2616343796332174954
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["GUID__"] = 1084704069982480181
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 2896211903382246620

