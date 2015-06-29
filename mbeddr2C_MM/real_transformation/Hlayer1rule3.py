

from core.himesis import Himesis

class Hlayer1rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule3, self).__init__(name='Hlayer1rule3', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([[0, 7], [7, 3], [0, 9], [9, 8], [1, 10], [10, 4], [1, 12], [12, 11], [3, 5], [5, 8], [4, 6], [6, 11], [11, 13], [13, 8], [4, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule3"""
        self["GUID__"] = 3245485098502804086
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8725493935933192139
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2342483584289531985
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5992917769456584052
        self.vs[3]["name"] = """layer1rule3class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7057208066092130434
        self.vs[4]["name"] = """layer1rule3class2"""
        self.vs[4]["classtype"] = """FunctionRefType"""
        self.vs[4]["mm__"] = """FunctionRefType"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 7947691149394391154
        self.vs[5]["associationType"] = """type"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 2317228976314925519
        self.vs[6]["associationType"] = """returnType"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 1847343855073359074
        self.vs[7]["mm__"] = """match_contains"""
        self.vs[7]["GUID__"] = 2711113105177838415
        self.vs[8]["name"] = """layer1rule3class1"""
        self.vs[8]["classtype"] = """StringType"""
        self.vs[8]["mm__"] = """StringType"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 8593273929653705316
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 8363762321572191952
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2185257695417982577
        self.vs[11]["name"] = """layer1rule3class3"""
        self.vs[11]["classtype"] = """StringType"""
        self.vs[11]["mm__"] = """StringType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 3735364017836456026
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5668792892488806559
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7345085668980146577
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 738202459785059176

