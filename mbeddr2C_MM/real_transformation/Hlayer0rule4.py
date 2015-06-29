

from core.himesis import Himesis

class Hlayer0rule4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule4, self).__init__(name='Hlayer0rule4', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 5], [1, 4], [4, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule4"""
        self["GUID__"] = 4552447861846335487
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5575631822966330578
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5341662884695358872
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4944731624743136493
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 4387203392444773778
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 5576915868763105145
        self.vs[5]["mm__"] = """VoidType"""
        self.vs[5]["classtype"] = """VoidType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """layer0rule4class0"""
        self.vs[5]["GUID__"] = 6109158671954166163
        self.vs[6]["mm__"] = """VoidType"""
        self.vs[6]["classtype"] = """VoidType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["name"] = """layer0rule4class1"""
        self.vs[6]["GUID__"] = 7890499136855781188

