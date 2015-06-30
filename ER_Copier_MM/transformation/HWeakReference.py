

from core.himesis import Himesis

class HWeakReference(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HWeakReference.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HWeakReference, self).__init__(name='HWeakReference', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [1, 4], [4, 8], [7, 5], [5, 17], [8, 9], [9, 18], [10, 11], [11, 18], [10, 12], [12, 17], [8, 13], [13, 19], [14, 15], [15, 19], [14, 16], [16, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """WeakReference"""
        self["GUID__"] = 1159945650245741951
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2641605370008881078
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6871342297421699601
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5731437106369180961
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 264761405707787380
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 8693472875799315693
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 1711287051430303785
        self.vs[6]["name"] = """solveRef"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 647445617854741518
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """WeakReference"""
        self.vs[7]["mm__"] = """WeakReference"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1679250802331554492
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """WeakReference"""
        self.vs[8]["mm__"] = """WeakReference"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 8594346861183451122
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 2199801719827206361
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 6750204779463750989
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 4788165479350626816
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 8389578727492800928
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 4685076684057999578
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 7554627074335031130
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 7380674791547810281
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 2847064854877553188
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 7779926516081759395
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 5982397361095303876
        self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 4685982133981347953

