

from core.himesis import Himesis

class Hlayer1rule14(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule14.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule14, self).__init__(name='Hlayer1rule14', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([[0, 8], [8, 3], [0, 10], [10, 9], [1, 11], [11, 4], [1, 13], [13, 12], [3, 5], [5, 9], [4, 6], [6, 12], [4, 7], [7, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule14"""
        self["GUID__"] = 268358001243616061
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5204684991743153442
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1132800574081772806
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2748718890700411658
        self.vs[3]["name"] = """layer1rule14class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 1376153292098478130
        self.vs[4]["name"] = """layer1rule14class2"""
        self.vs[4]["classtype"] = """FunctionPrototype"""
        self.vs[4]["mm__"] = """FunctionPrototype"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 1641867173618670421
        self.vs[5]["associationType"] = """type"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 4629406764841536051
        self.vs[6]["associationType"] = """type"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 3903507805425231097
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 2130394293862377267
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4129707848539384109
        self.vs[9]["name"] = """layer1rule14class1"""
        self.vs[9]["classtype"] = """StringType"""
        self.vs[9]["mm__"] = """StringType"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = 169029886202469289
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 1343847994011312661
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 8358314392290495247
        self.vs[12]["name"] = """layer1rule14class3"""
        self.vs[12]["classtype"] = """StringType"""
        self.vs[12]["mm__"] = """StringType"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 1576724591188333218
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 8403531937757598535

