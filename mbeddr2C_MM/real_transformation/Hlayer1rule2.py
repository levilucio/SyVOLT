

from core.himesis import Himesis

class Hlayer1rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule2, self).__init__(name='Hlayer1rule2', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([[0, 7], [7, 3], [0, 9], [9, 8], [1, 10], [10, 4], [1, 12], [12, 11], [3, 5], [5, 8], [4, 6], [6, 11], [11, 13], [13, 8], [4, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule2"""
        self["GUID__"] = 3572108925803644528
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8108864070077864723
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 312515534578876756
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8152746581147991143
        self.vs[3]["name"] = """layer1rule2class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 30457535529999180
        self.vs[4]["name"] = """layer1rule2class2"""
        self.vs[4]["classtype"] = """FunctionRefType"""
        self.vs[4]["mm__"] = """FunctionRefType"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 7080502000710634831
        self.vs[5]["associationType"] = """type"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 3573145828556764613
        self.vs[6]["associationType"] = """returnType"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 5824550076056852760
        self.vs[7]["mm__"] = """match_contains"""
        self.vs[7]["GUID__"] = 4594269526893613178
        self.vs[8]["name"] = """layer1rule2class1"""
        self.vs[8]["classtype"] = """VoidType"""
        self.vs[8]["mm__"] = """VoidType"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 839378683687919685
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 5766352862038363511
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 3075418104973222195
        self.vs[11]["name"] = """layer1rule2class3"""
        self.vs[11]["classtype"] = """VoidType"""
        self.vs[11]["mm__"] = """VoidType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 843933313076651950
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 7100307948542247055
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6505200676818567399
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 7716498981554784066

