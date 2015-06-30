

from core.himesis import Himesis

class HETypeParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HETypeParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HETypeParameter, self).__init__(name='HETypeParameter', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [1, 4], [4, 8], [7, 5], [5, 17], [8, 9], [9, 18], [10, 11], [11, 18], [10, 12], [12, 17], [8, 13], [13, 19], [14, 15], [15, 19], [14, 16], [16, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ETypeParameter"""
        self["GUID__"] = 3632745135596295002
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4805474184702522050
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 737680187430244968
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8993653848562045012
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 61989416727245689
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 8181580833848054593
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 4760533119359148100
        self.vs[6]["name"] = """solveRef"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 8057296177515621242
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ETypeParameter"""
        self.vs[7]["mm__"] = """ETypeParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 879199421171233428
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """ETypeParameter"""
        self.vs[8]["mm__"] = """ETypeParameter"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5580485170412211124
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 7923194073620387714
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 4032644974783981448
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 1857242510163522598
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 4023000256422245111
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 4315359072403712147
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 1180196765689810892
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 1700435360017908436
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 6906075996137209169
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 8114508805334879303
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 7187756016973194098
        self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 8700632262584088753

