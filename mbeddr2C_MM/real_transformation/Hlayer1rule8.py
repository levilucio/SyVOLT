

from core.himesis import Himesis

class Hlayer1rule8(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule8.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule8, self).__init__(name='Hlayer1rule8', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([[0, 8], [8, 7], [0, 9], [9, 3], [1, 11], [11, 10], [1, 12], [12, 4], [7, 5], [5, 3], [10, 6], [6, 4], [10, 13], [13, 7], [4, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule8"""
        self["GUID__"] = 5795851293942256199
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2418631587889340768
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3592132357254655191
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4594710405302730604
        self.vs[3]["name"] = """layer1rule8class1"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 3258875222047190235
        self.vs[4]["name"] = """layer1rule8class3"""
        self.vs[4]["classtype"] = """TypeDef"""
        self.vs[4]["mm__"] = """TypeDef"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 2525883380586434613
        self.vs[5]["associationType"] = """contents"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 7208480847988659264
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 6584099005837835541
        self.vs[7]["name"] = """layer1rule8class0"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7114092404835825265
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 1408765999994994671
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 679596801109254366
        self.vs[10]["name"] = """layer1rule8class2"""
        self.vs[10]["classtype"] = """ImplementationModule"""
        self.vs[10]["mm__"] = """ImplementationModule"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 163814367942699432
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 2336303213213847966
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6448264693081541880
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 5040749843429362955
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 7382233070841505639

