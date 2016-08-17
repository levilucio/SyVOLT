

from core.himesis import Himesis

class HEGenericType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEGenericType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEGenericType, self).__init__(name='HEGenericType', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 11], [1, 4], [4, 12], [12, 5], [5, 6], [7, 8], [8, 6], [7, 9], [9, 10], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EGenericType"""
        self["GUID__"] = 4610662454465074422
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5302232807056058057
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6639401560986707789
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8823656757970803871
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 6848396959330481101
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 682794952484916451
        self.vs[5]["mm__"] = """hasAttribute_T"""
        self.vs[5]["GUID__"] = 932585748818711410
        self.vs[6]["name"] = """ApplyAttribute"""
        self.vs[6]["mm__"] = """Attribute"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 6280434910045919354
        self.vs[7]["name"] = """eq_"""
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = 7333482970623920520
        self.vs[8]["mm__"] = """leftExpr"""
        self.vs[8]["GUID__"] = 6111771901181699771
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = 1619373095735528820
        self.vs[10]["name"] = """solveRef"""
        self.vs[10]["mm__"] = """Constant"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = 6529977820373345548
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EGenericType"""
        self.vs[11]["mm__"] = """EGenericType"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = 2276252857991260619
        self.vs[12]["name"] = """"""
        self.vs[12]["classtype"] = """EGenericType"""
        self.vs[12]["mm__"] = """EGenericType"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 300391440760436126

