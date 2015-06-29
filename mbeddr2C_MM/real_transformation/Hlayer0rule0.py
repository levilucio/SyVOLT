

from core.himesis import Himesis

class Hlayer0rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule0, self).__init__(name='Hlayer0rule0', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 10], [1, 4], [4, 11], [10, 5], [5, 12], [11, 6], [6, 13], [7, 8], [8, 13], [7, 9], [9, 12], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule0"""
        self["GUID__"] = 7717147011900028742
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8896196422500755785
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5143723105174968953
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3386045327739679524
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 1981789691901826136
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 7179926147627085480
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 1254504884507630483
        self.vs[6]["mm__"] = """hasAttribute_T"""
        self.vs[6]["GUID__"] = 2770212785335729227
        self.vs[7]["name"] = """eq_"""
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = 439604713193545013
        self.vs[8]["mm__"] = """leftExpr"""
        self.vs[8]["GUID__"] = 3498541900400595126
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = 3101641160832790644
        self.vs[10]["name"] = """layer0rule0class0"""
        self.vs[10]["classtype"] = """ImplementationModule"""
        self.vs[10]["mm__"] = """ImplementationModule"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = 5245548115078725169
        self.vs[11]["name"] = """layer0rule0class1"""
        self.vs[11]["classtype"] = """ImplementationModule"""
        self.vs[11]["mm__"] = """ImplementationModule"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 714870728637050049
        self.vs[12]["name"] = """name"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 1280321023609777133
        self.vs[13]["name"] = """name"""
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["GUID__"] = 4104042922596455826

