

from core.himesis import Himesis

class Hlayer2rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer2rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule2, self).__init__(name='Hlayer2rule2', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 8], [0, 10], [10, 3], [1, 12], [12, 11], [1, 13], [13, 4], [3, 5], [5, 8], [4, 6], [6, 11], [4, 7], [7, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer2rule2"""
        self["GUID__"] = 7234933100294607637
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9037011019073771219
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8300276758138686995
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 9042897917184592523
        self.vs[3]["name"] = """layer2rule2class1"""
        self.vs[3]["classtype"] = """OperationParameter"""
        self.vs[3]["mm__"] = """OperationParameter"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8707417637409327230
        self.vs[4]["name"] = """layer2rule2class3"""
        self.vs[4]["classtype"] = """Argument"""
        self.vs[4]["mm__"] = """Argument"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 2231016739216814287
        self.vs[5]["associationType"] = """type"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 3408002388607700757
        self.vs[6]["associationType"] = """type"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 3872947192363278065
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 7653028462372058491
        self.vs[8]["name"] = """layer2rule2class0"""
        self.vs[8]["classtype"] = """VoidType"""
        self.vs[8]["mm__"] = """VoidType"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 5800340777388170783
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 6635987733447237341
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 8619653930003000127
        self.vs[11]["name"] = """layer2rule2class2"""
        self.vs[11]["classtype"] = """VoidType"""
        self.vs[11]["mm__"] = """VoidType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 3736706331170457740
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5704630940335041720
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 7290687490708499392

