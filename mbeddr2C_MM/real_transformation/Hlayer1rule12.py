

from core.himesis import Himesis

class Hlayer1rule12(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule12.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule12, self).__init__(name='Hlayer1rule12', num_nodes=12, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 8], [8, 7], [1, 9], [9, 4], [7, 5], [5, 4], [7, 10], [10, 6], [4, 11], [11, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule12"""
        self["GUID__"] = 6293860965890758322
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6812880937194523829
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7951929899688944257
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6358178422783252136
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 5077427920831333998
        self.vs[4]["name"] = """layer1rule12class2"""
        self.vs[4]["classtype"] = """FunctionPrototype"""
        self.vs[4]["mm__"] = """FunctionPrototype"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 2222013134830405593
        self.vs[5]["associationType"] = """contents"""
        self.vs[5]["mm__"] = """directLink_T"""
        self.vs[5]["GUID__"] = 3094014564133798603
        self.vs[6]["name"] = """layer1rule12class0"""
        self.vs[6]["classtype"] = """ImplementationModule"""
        self.vs[6]["mm__"] = """ImplementationModule"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 5328146191868472161
        self.vs[7]["name"] = """layer1rule12class1"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 3402227083395178446
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 2391869126726498447
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 2301127662993280819
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["GUID__"] = 7375002193898598278
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 6115383368763216925

