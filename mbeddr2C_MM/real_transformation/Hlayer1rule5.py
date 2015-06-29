

from core.himesis import Himesis

class Hlayer1rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule5, self).__init__(name='Hlayer1rule5', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([[0, 8], [8, 7], [0, 9], [9, 3], [1, 11], [11, 10], [1, 12], [12, 4], [7, 5], [5, 3], [10, 6], [6, 4], [10, 13], [13, 7], [4, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule5"""
        self["GUID__"] = 7121923407450309968
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1368560497777541022
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4751303572630878886
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 845550316249322188
        self.vs[3]["name"] = """layer1rule5class1"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 3357188908807532646
        self.vs[4]["name"] = """layer1rule5class3"""
        self.vs[4]["classtype"] = """TypeDef"""
        self.vs[4]["mm__"] = """TypeDef"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 1999443662273160577
        self.vs[5]["associationType"] = """contents"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 6793073153434534715
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 5532718770908376637
        self.vs[7]["name"] = """layer1rule5class0"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6702350498326781718
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3926902999566832649
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 9135709994621699708
        self.vs[10]["name"] = """layer1rule5class2"""
        self.vs[10]["classtype"] = """ImplementationModule"""
        self.vs[10]["mm__"] = """ImplementationModule"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 7133844888951520284
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 8966194469667547243
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 7888743067633106625
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 614331220517588496
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 1724689244232468927

