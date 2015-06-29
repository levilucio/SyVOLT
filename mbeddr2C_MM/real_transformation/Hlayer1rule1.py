

from core.himesis import Himesis

class Hlayer1rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule1, self).__init__(name='Hlayer1rule1', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 3], [0, 10], [10, 4], [1, 11], [11, 5], [1, 12], [12, 6], [3, 7], [7, 4], [5, 8], [8, 6], [6, 13], [13, 4], [5, 14], [14, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule1"""
        self["GUID__"] = 2747947671990690374
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9219817513348731321
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6493727050826491077
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3475884727218499752
        self.vs[3]["name"] = """layer1rule1class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 6942357286251847066
        self.vs[4]["name"] = """layer1rule1class1"""
        self.vs[4]["classtype"] = """Operation"""
        self.vs[4]["mm__"] = """Operation"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 7252262702099833373
        self.vs[5]["name"] = """layer1rule1class2"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2909822381962991222
        self.vs[6]["name"] = """layer1rule1class3"""
        self.vs[6]["classtype"] = """CFunctionPointerStructMember"""
        self.vs[6]["mm__"] = """CFunctionPointerStructMember"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 7127670685960149005
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 865852835204211302
        self.vs[8]["associationType"] = """members"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 6328354481912680967
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 3633950136411434403
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 2204509493628348488
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 3984364513579303466
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6599857182570544975
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8448327508920822198
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2328925581216226280

