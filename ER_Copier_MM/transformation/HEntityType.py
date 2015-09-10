

from core.himesis import Himesis

class HEntityType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEntityType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEntityType, self).__init__(name='HEntityType', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [1, 4], [4, 8], [7, 5], [5, 17], [8, 9], [9, 18], [10, 11], [11, 18], [10, 12], [12, 17], [8, 13], [13, 19], [14, 15], [15, 19], [14, 16], [16, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EntityType"""
        self["GUID__"] = 4924037695297160
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5003278574968237783
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7218827365817520993
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5366880029797864856
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 5653354931984539431
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 1460312432854626397
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 8442692263105171712
        self.vs[6]["name"] = """solveRef"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 8806109927421020423
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EntityType"""
        self.vs[7]["mm__"] = """EntityType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6260458794541233001
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """EntityType"""
        self.vs[8]["mm__"] = """EntityType"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 1804978486371607143
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 8326058652806528721
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 3698899952261154208
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 8587443973046568052
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 7807496258515195098
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 1801243577316989354
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 928220645873206131
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 9068267603561174490
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 470891065691708616
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 1615798800778280838
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 3954014922756901206
        self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 2343449554942441708

