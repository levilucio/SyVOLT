

from core.himesis import Himesis

class Hlayer2rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer2rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule0, self).__init__(name='Hlayer2rule0', num_nodes=12, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 8], [8, 5], [1, 9], [9, 6], [6, 7], [7, 5], [5, 10], [10, 3], [6, 11], [11, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer2rule0"""
        self["GUID__"] = 2414431654776623122
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7946396462006905195
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9124143256168906949
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1177567289520392442
        self.vs[3]["name"] = """layer2rule0class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 5458118181525875251
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 4704659143830141369
        self.vs[5]["name"] = """layer2rule0class1"""
        self.vs[5]["classtype"] = """PointerType"""
        self.vs[5]["mm__"] = """PointerType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5767867373818787382
        self.vs[6]["name"] = """layer2rule0class2"""
        self.vs[6]["classtype"] = """FunctionRefType"""
        self.vs[6]["mm__"] = """FunctionRefType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 3364284483673226429
        self.vs[7]["associationType"] = """argTypes"""
        self.vs[7]["mm__"] = """directLink_T"""
        self.vs[7]["GUID__"] = 4611458155661680952
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 8451541115992597186
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 7496403634985261681
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["GUID__"] = 7588495598398299479
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 3412551437073941915

