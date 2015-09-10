

from core.himesis import Himesis

class HEObject(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEObject.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEObject, self).__init__(name='HEObject', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 11], [1, 4], [4, 12], [12, 5], [5, 6], [7, 8], [8, 6], [7, 9], [9, 10], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EObject"""
        self["GUID__"] = 2014903438265108500
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7193012010578658766
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4812619189270165
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5807501311204855918
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 7269777470397348969
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 7364466511855976076
        self.vs[5]["mm__"] = """hasAttribute_T"""
        self.vs[5]["GUID__"] = 8260107687374176187
        self.vs[6]["name"] = """ApplyAttribute"""
        self.vs[6]["mm__"] = """Attribute"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 6099047028054979070
        self.vs[7]["name"] = """eq_"""
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = 8003163520809268770
        self.vs[8]["mm__"] = """leftExpr"""
        self.vs[8]["GUID__"] = 1563705309464035459
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = 1890454714959700534
        self.vs[10]["name"] = """solveRef"""
        self.vs[10]["mm__"] = """Constant"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = 1825166726526655015
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EObject"""
        self.vs[11]["mm__"] = """EObject"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = 4006243618181391604
        self.vs[12]["name"] = """"""
        self.vs[12]["classtype"] = """EObject"""
        self.vs[12]["mm__"] = """EObject"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 2238948824833138603

