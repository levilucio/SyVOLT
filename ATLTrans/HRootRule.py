

from core.himesis import Himesis

class HRootRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRootRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRootRule, self).__init__(name='HRootRule', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 6], [6, 5], [5, 7], [7, 8], [9, 10], [10, 8], [9, 11], [11, 12], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """RootRule"""
        self["GUID__"] = 3252311431865822877
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 908134083291013580
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4535829077298787394
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3045847821357108417
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 13664938046745276
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 6256391025411542228
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """CommunityRoot"""
        self.vs[5]["mm__"] = """CommunityRoot"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8896494739195760419
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 1190961904671489656
        self.vs[7]["mm__"] = """hasAttribute_T"""
        self.vs[7]["GUID__"] = 4263402199876873999
        self.vs[8]["name"] = """ApplyAttribute"""
        self.vs[8]["mm__"] = """Attribute"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 1530059649409497295
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 7464250716888200770
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 6882874071983497968
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 47343844567576352
        self.vs[12]["name"] = """root"""
        self.vs[12]["mm__"] = """Constant"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 5904951067270458617

