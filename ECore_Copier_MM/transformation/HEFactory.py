

from core.himesis import Himesis

class HEFactory(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEFactory.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEFactory, self).__init__(name='HEFactory', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 11], [1, 4], [4, 12], [12, 5], [5, 6], [7, 8], [8, 6], [7, 9], [9, 10], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EFactory"""
        self["GUID__"] = 8400196702007158543
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2199636794028666257
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6465093992800657037
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1925928170982035402
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 6165394884001585145
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 4390127527014675222
        self.vs[5]["mm__"] = """hasAttribute_T"""
        self.vs[5]["GUID__"] = 7246573529685747618
        self.vs[6]["name"] = """ApplyAttribute"""
        self.vs[6]["mm__"] = """Attribute"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 1727402299754346048
        self.vs[7]["name"] = """eq_"""
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = 4234650632736433679
        self.vs[8]["mm__"] = """leftExpr"""
        self.vs[8]["GUID__"] = 5493623472562140299
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = 6775017376831886724
        self.vs[10]["name"] = """solveRef"""
        self.vs[10]["mm__"] = """Constant"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = 3528273051462203085
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EFactory"""
        self.vs[11]["mm__"] = """EFactory"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = 8525825851527187361
        self.vs[12]["name"] = """"""
        self.vs[12]["classtype"] = """EFactory"""
        self.vs[12]["mm__"] = """EFactory"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 1822229612345653402

