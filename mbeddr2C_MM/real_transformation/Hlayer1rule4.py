

from core.himesis import Himesis

class Hlayer1rule4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule4, self).__init__(name='Hlayer1rule4', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([[0, 15], [15, 3], [0, 16], [16, 4], [0, 17], [17, 7], [1, 8], [8, 5], [1, 10], [10, 9], [3, 11], [11, 4], [4, 12], [12, 7], [5, 6], [6, 9], [9, 13], [13, 7], [5, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule4"""
        self["GUID__"] = 2202634188146938449
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4035100179239050307
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7283592638657057315
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1187038649746395629
        self.vs[3]["name"] = """layer1rule4class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7388052534358475110
        self.vs[4]["name"] = """layer1rule4class1"""
        self.vs[4]["classtype"] = """OperationParameter"""
        self.vs[4]["mm__"] = """OperationParameter"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 3153903773675730931
        self.vs[5]["name"] = """layer1rule4class3"""
        self.vs[5]["classtype"] = """FunctionRefType"""
        self.vs[5]["mm__"] = """FunctionRefType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3569904946940159570
        self.vs[6]["associationType"] = """argTypes"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 7887115880321927709
        self.vs[7]["name"] = """layer1rule4class2"""
        self.vs[7]["classtype"] = """StringType"""
        self.vs[7]["mm__"] = """StringType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2395292943536295704
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 2170428081577334866
        self.vs[9]["name"] = """layer1rule4class4"""
        self.vs[9]["classtype"] = """StringType"""
        self.vs[9]["mm__"] = """StringType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6087901807038472326
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2829265621228156770
        self.vs[11]["associationType"] = """parameters"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 413806223085498474
        self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 8530260417727160930
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7588342778580240474
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 7297413234937886953
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 5256989381636655139
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 2055737980818856397
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = 6065842848728336284

