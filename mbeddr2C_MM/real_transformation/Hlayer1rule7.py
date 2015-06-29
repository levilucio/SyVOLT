

from core.himesis import Himesis

class Hlayer1rule7(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule7.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule7, self).__init__(name='Hlayer1rule7', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([[0, 8], [8, 7], [0, 9], [9, 3], [1, 11], [11, 10], [1, 12], [12, 4], [7, 5], [5, 3], [10, 6], [6, 4], [10, 13], [13, 7], [4, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule7"""
        self["GUID__"] = 6833501714496640505
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5108112627927182122
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1762732740605323009
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8060223352797190758
        self.vs[3]["name"] = """layer1rule7class1"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 3850155108459683478
        self.vs[4]["name"] = """layer1rule7class3"""
        self.vs[4]["classtype"] = """StructDeclaration"""
        self.vs[4]["mm__"] = """StructDeclaration"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 470653140600552276
        self.vs[5]["associationType"] = """contents"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 555585252363993227
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 4765474091454238706
        self.vs[7]["name"] = """layer1rule7class0"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 4335160892147639308
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3856116416254232971
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 7565905245736243265
        self.vs[10]["name"] = """layer1rule7class2"""
        self.vs[10]["classtype"] = """ImplementationModule"""
        self.vs[10]["mm__"] = """ImplementationModule"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 4432717764855681305
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 7794808407448951535
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 93350892345101469
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8530872957629096486
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 684151483209948878

