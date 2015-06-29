

from core.himesis import Himesis

class Hlayer1rule6(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule6.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule6, self).__init__(name='Hlayer1rule6', num_nodes=12, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 8], [8, 5], [1, 9], [9, 6], [6, 7], [7, 5], [6, 10], [10, 3], [5, 11], [11, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule6"""
        self["GUID__"] = 4781031928978731154
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 295494930141656455
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 299069949700588758
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3685951727059184234
        self.vs[3]["name"] = """layer1rule6class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 5565773112197904719
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 7185759847241436708
        self.vs[5]["name"] = """layer1rule6class1"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3857931400207403634
        self.vs[6]["name"] = """layer1rule6class2"""
        self.vs[6]["classtype"] = """StructType"""
        self.vs[6]["mm__"] = """StructType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 6684563054157055038
        self.vs[7]["associationType"] = """struct"""
        self.vs[7]["mm__"] = """directLink_T"""
        self.vs[7]["GUID__"] = 3388475499119083168
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 6658988633652008943
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 4965844723707457808
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["GUID__"] = 4031403542591470617
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 4247384082044663606

